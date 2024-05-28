use polars::prelude::*;
use image::{DynamicImage, ImageBuffer, Pixel, Luma, Rgb};

use crate::types::{Image, Mask};
use crate::geometry::points::resample_points;
use crate::process::{lines, mask, transform::convert_to_gray};
use crate::io::table::write_table;

use crate::process::objects::{
    extract_objects,
    extract_foreground_objects,
    extract_background_objects,
    extract_all_objects,
};

use crate::descriptors::batch::{
    batch_polygon_descriptors_df,
    batch_intensity_descriptors_df,
    batch_moments_descriptors_df,
    batch_texture_descriptors_df,
    batch_zernike_descriptors_df,
};

use crate::io::{write_image, write_polygons, write_boxes, write_labels};

/// A struct for handling processing of generic image buffers and masks (or polygons)
pub struct Processor<P> 
where
    P: Pixel + 'static,
    <P as Pixel>::Subpixel: 'static + From<u8>,
{
    pub image: Image<P>,
    pub mask: Mask,
    pub labels: Vec<u16>,
    pub n_labels: usize,
    pub is_binary: bool,
    pub polygons: Vec<Vec<[f64; 2]>>,
    pub bounding_boxes: Option<Vec<Vec<f64>>>,
    setting: &'static str,
}

/// A struct for storing the output of the Processor
pub struct ProcessorOutput<P> 
where
    P: Pixel + 'static,
    <P as Pixel>::Subpixel: 'static + From<u8>,
{
    pub objects: Option<Vec<Image<P>>>,
    pub foreground_objects: Option<Vec<Image<P>>>,
    pub background_objects: Option<Vec<Image<P>>>,
    pub binary_objects: Option<Vec<Image<Luma<u16>>>>,
    pub polygons: Option<Vec<Vec<[f64; 2]>>>,
    pub bounding_boxes: Option<Vec<Vec<f64>>>,
    pub labels: Option<Vec<u16>>,
    pub n_labels: usize,
    pub has_error: bool,
    pub mode: String,
}

/// A struct for storing the measurements of the Processor
pub struct ProcessorMeasurements {
    pub descriptors: DataFrame,
    pub n_labels: usize,
    pub has_error: bool,
    pub mode: String,
}

impl<P> Processor<P>
where
    P: Pixel<Subpixel = u8> + 'static,
    <P as Pixel>::Subpixel: 'static + From<u8>,
{
    /// Create a new Processor from an image and mask pair
    ///
    /// # Arguments
    ///
    /// * `image` - An image buffer
    /// * `mask` - A mask buffer
    ///
    /// # Examples
    ///
    /// ```no_run
    /// use fqmv_core::utils::toy;
    /// use fqmv_core::data::Processor;
    ///
    /// let image = toy::rgb_image();
    /// let mask = toy::mask();
    ///
    /// let mut processor = Processor::new_from_mask(image, mask);
    /// ```
    pub fn new_from_mask(image: Image<P>, mut mask: Mask) -> Self {
        let (iw, ih) = image.dimensions();
        let (mw, mh) = mask.dimensions();

        if iw != mw || ih != mh {
            panic!("Image and mask dimensions do not match");
        }

        let (mut labels, n_labels, is_binary) = mask::count_labels(&mask);

        let polygons = if is_binary {
            lines::extract_contours::<f64>(&mask, None)
        } else {
            lines::extract_contours::<f64>(&mask, Some(&labels))
        };

        if is_binary {
            // TO-DO: We re-generate mask with integer labels if the mask is binary
            // This assumes objects in the binary mask aren't touching edges.
            // This obviously isn't the best way to handle int vs binary 
            // masks; this is just a temporary hack to ensure all masks are 
            // integer-labeled and not binary for downstream processing
            (mask, labels) = mask::draw_mask(&polygons, iw, ih);
        }

        Processor {
            image,
            mask,
            labels,
            n_labels,
            is_binary,
            polygons,
            bounding_boxes: None,
            setting: "mask",
        }
    }

    /// Create a new Processor from an image and a vector of polygons
    ///
    /// # Arguments
    ///
    /// * `image` - An image buffer
    /// * `polygons` - A vector of polygons
    ///
    /// # Examples
    ///
    /// ```no_run
    /// use fqmv_core::utils::toy;
    /// use fqmv_core::data::Processor;
    ///
    /// let image = toy::rgb_image();
    /// let polygons = toy::polygons();
    ///
    /// let mut processor = Processor::new_from_polygons(image, polygons);
    /// ```
    pub fn new_from_polygons(image: Image<P>, polygons: Vec<Vec<[f64; 2]>>) -> Self {
        Processor {
            image,
            mask: Mask::new(0, 0),
            labels: vec![],
            n_labels: 0,
            is_binary: false,
            polygons,
            bounding_boxes: None,
            setting: "polygons",
        }
    }

    /// Create a new Processor from an image and a vector of bounding boxes
    ///
    /// # Arguments
    ///
    /// * `image` - An image buffer
    /// * `bounding_boxes` - A vector of bounding boxes
    ///
    /// # Examples
    ///
    /// ```no_run
    /// use fqmv_core::utils::toy;
    /// use fqmv_core::data::Processor;
    ///
    /// let image = toy::rgb_image();
    /// let bounding_boxes = vec![vec![0.0, 0.0, 10.0, 10.0]];
    ///
    /// let mut processor = Processor::new_from_boxes(image, bounding_boxes);
    /// ```
    pub fn new_from_boxes(image: Image<P>, bounding_boxes: Vec<Vec<f64>>) -> Self {
        Processor {
            image,
            mask: Mask::new(0, 0),
            labels: (0..bounding_boxes.len() as u16).collect(),
            n_labels: bounding_boxes.len(),
            is_binary: false,
            polygons: vec![],
            bounding_boxes: Some(bounding_boxes),
            setting: "boxes",
        }
    }

    /// Run the processor on image-mask pair to generate various object-level outputs
    ///
    /// # Arguments
    ///
    /// * `pad` - Padding to add around the bounding boxes/objects
    /// * `resize` - Resize the objects to a specific size
    /// * `filter` - Filter to use for resizing
    /// * `n_resample` - Number of points to resample for each contour
    /// * `exclude_borders` - Exclude objects that touch the image borders
    /// * `mode` - A string specifying the output mode (default: "omcbl")
    /// 
    /// # Examples
    ///
    /// ```no_run
    /// use fqmv_core::utils::toy;
    /// use fqmv_core::data::Processor;
    ///
    /// let image = toy::rgb_image();
    /// let mask = toy::mask();
    ///
    /// let mut processor = Processor::new_from_mask(image, mask);
    ///
    /// let processed = processor.run(
    ///     Some(0),
    ///     Some((2, 2)),
    ///     Some("nearest".to_string()),
    ///     Some(32),
    ///     Some(false),
    ///     Some("omcbl".to_string())
    /// );
    pub fn run(&mut self,
        pad: Option<u32>,
        resize: Option<(u32, u32)>,
        filter: Option<String>,
        n_resample: Option<usize>,
        exclude_borders: Option<bool>,
        mode: Option<String>,
    ) -> ProcessorOutput<P> {
        let mode = if self.bounding_boxes.is_none() {
            mode.unwrap_or("oypbl".to_string())
        } else {
            mode.unwrap_or("obl".to_string())
        };

        let mut bounding_boxes = if self.bounding_boxes.is_none() {
            lines::extract_bounding_boxes::<f64>(&self.polygons, pad)
        } else {
            self.bounding_boxes.clone().unwrap()
        };

        let mut to_remove = vec![];
        for (i, bbox) in bounding_boxes.iter().enumerate() {
            let min_x = if bbox[0] <= 0.0 { 0_u32 } else { bbox[0] as u32 };
            let min_y = if bbox[1] <= 0.0 { 0_u32 } else { bbox[1] as u32 };
            let max_x = if bbox[2] <= 0.0 { 0_u32 } else { bbox[2] as u32 };
            let max_y = if bbox[3] <= 0.0 { 0_u32 } else { bbox[3] as u32 };

            let diff_x = max_x - min_x;
            let diff_y = max_y - min_y;

            if exclude_borders.unwrap_or(false) {
                if min_x == 0
                    || min_y == 0
                    || max_x >= self.image.width()
                    || max_y >= self.image.height()
                {
                    to_remove.push(i);
                    continue;
                }
            }
            
            if !self.polygons.is_empty() {
                if self.polygons[i].len() < 3
                    || diff_x < 2
                    || diff_y < 2
                    || self.polygons[i].iter().all(|x| x == &self.polygons[i][0])
                {
                    to_remove.push(i);
                }
            }
        }

        for i in to_remove.iter().rev() {
            bounding_boxes.remove(*i);

            if !self.polygons.is_empty() {
                self.polygons.remove(*i);
            }

            if self.setting == "mask" || self.setting == "boxes" {
                self.labels.remove(*i);
                self.n_labels -= 1;
            }
        }

        if self.setting == "polygons" {
            let (iw, ih) = self.image.dimensions();
            let (mask, labels) = mask::draw_mask(&self.polygons, iw, ih);
            self.n_labels = labels.len();
            self.labels = labels;
            self.mask = mask;
        }

        let (
            objects,
            objects_error,
            foreground_objects,
            foreground_objects_error,
            background_objects,
            background_objects_error,
            binary_objects,
            binary_objects_error,
        ) = if mode.contains('o') && mode.contains('m') && mode.contains('x') && mode.contains('y') {
            let (_objects, _foreground_objects, _background_objects, _binary_objects) = extract_all_objects(
                &mut self.image,
                &mut self.mask,
                &bounding_boxes,
                &self.labels,
                resize,
                filter.as_deref(),
            );

            let objects_error = _objects.len() != self.n_labels;
            let foreground_objects_error = _foreground_objects.len() != self.n_labels;
            let background_objects_error = _background_objects.len() != self.n_labels;
            let binary_objects_error = _binary_objects.len() != self.n_labels;

            (
                Some(_objects), objects_error,
                Some(_foreground_objects), foreground_objects_error,
                Some(_background_objects), background_objects_error,
                Some(_binary_objects), binary_objects_error
            )
        } else if mode.contains('o') || mode.contains('m') || mode.contains('x') || mode.contains('y') {
            let mut objects = None;
            let mut foreground_objects = None;
            let mut background_objects = None;
            let mut binary_objects = None;

            let mut objects_error = false;
            let mut foreground_objects_error = false;
            let mut background_objects_error = false;
            let mut binary_objects_error = false;

            if mode.contains('o') {
                let _objects = extract_objects(
                    &mut self.image,
                    &bounding_boxes,
                    resize,
                    filter.as_deref(),
                );

                objects_error = _objects.len() != self.n_labels;
                objects = Some(_objects);
            }

            if mode.contains('m') {
                let _foreground_objects = extract_foreground_objects(
                    &mut self.image,
                    &mut self.mask,
                    &bounding_boxes,
                    &self.labels,
                    resize,
                    filter.as_deref(),
                );

                foreground_objects_error = _foreground_objects.len() != self.n_labels;
                foreground_objects = Some(_foreground_objects);
            }

            if mode.contains('x') {
                let _background_objects = extract_background_objects(
                    &mut self.image,
                    &mut self.mask,
                    &bounding_boxes,
                    &self.labels,
                    resize,
                    filter.as_deref(),
                );

                background_objects_error = _background_objects.len() != self.n_labels;
                background_objects = Some(_background_objects);
            }

            if mode.contains('y') {
                let _binary_objects = extract_objects(
                    &mut self.mask,
                    &bounding_boxes,
                    resize,
                    filter.as_deref(),
                );

                binary_objects_error = _binary_objects.len() != self.n_labels;
                binary_objects = Some(_binary_objects);
            }

            (
                objects, objects_error,
                foreground_objects, foreground_objects_error,
                background_objects, background_objects_error,
                binary_objects, binary_objects_error
            )
        } else {
            (None, false, None, false, None, false, None, false)
        };

        let (polygons, polygons_error) = if mode.contains('p') {
            let contours = self.polygons.iter()
                .map(|polygon| {
                    resample_points(polygon.to_vec(), n_resample.unwrap_or(32))
                }).collect::<Vec<Vec<[f64; 2]>>>();
            
            let n_contours = contours.len();

            (Some(contours), n_contours != self.n_labels)
        } else {
            (None, false)
        };

        let (bounding_boxes, bounding_boxes_error) = if mode.contains('b') {
            let n_bounding_boxes = bounding_boxes.len();
            (Some(bounding_boxes), n_bounding_boxes != self.n_labels)
        } else {
            (None, false)
        };

        let labels = Some(self.labels.to_vec());

        let has_error = objects_error
            || foreground_objects_error
            || background_objects_error
            || binary_objects_error
            || polygons_error
            || bounding_boxes_error;
            
        ProcessorOutput {
            objects,
            foreground_objects,
            background_objects,
            binary_objects,
            polygons,
            bounding_boxes,
            labels,
            n_labels: self.n_labels,
            has_error,
            mode,
        }
    }

    pub fn profile(&mut self,
        pad: Option<u32>,
        resize: Option<(u32, u32)>,
        filter: Option<String>,
        n_resample: Option<usize>,
        exclude_borders: Option<bool>,
        mode: Option<String>,
        bins: Option<usize>,
        with_zeros: Option<bool>,
        with_max: Option<f64>,
    ) -> ProcessorMeasurements {
        // TO-DO: There's a lot of redundant code here -- I should probably clean it up
        // and move some of the repeated code into a method or separate function when
        // I get a chance
        let output: ProcessorOutput<P> = self.run(
            pad,
            resize,
            filter,
            n_resample,
            exclude_borders,
            mode,
        );

        if output.has_error || output.n_labels == 0 {
            return ProcessorMeasurements {
                descriptors: DataFrame::new_no_checks(vec![]),
                n_labels: 0,
                has_error: output.has_error,
                mode: output.mode,
            };
        }

        let bins = bins.unwrap_or(256);
        let with_zeros = with_zeros.unwrap_or(false);
        let with_max = Some(with_max.unwrap_or(255.0));

        let mut descriptors = vec![];

        if output.objects.is_some() {
            let gray_objects = convert_to_gray(&output.objects.unwrap());
            let intensity = batch_intensity_descriptors_df(
                &gray_objects,
                bins,
                with_zeros,
                with_max,
            );

            let texture = batch_texture_descriptors_df(&gray_objects);
            let zernike = batch_zernike_descriptors_df(&gray_objects, true);

            let mut object_descriptors = polars::functions::concat_df_horizontal(&[
                intensity,
                texture,
                zernike,
            ]).unwrap();

            let column_names: Vec<String> = object_descriptors
                .get_column_names()
                .iter()
                .map(|s| s.to_owned().to_owned())
                .collect();

            column_names
                .iter()
                .for_each(|old| {
                    object_descriptors
                    .rename(old, format!("object_{}", old).as_str())
                    .expect(format!("cannot rename column {old}").as_str());
                });

            descriptors.push(object_descriptors);
        }

        if output.foreground_objects.is_some() {
            let gray_foreground_objects = convert_to_gray(&output.foreground_objects.unwrap());
            let intensity = batch_intensity_descriptors_df(
                &gray_foreground_objects,
                bins,
                with_zeros,
                with_max,
            );

            let texture = batch_texture_descriptors_df(&gray_foreground_objects);
            let zernike = batch_zernike_descriptors_df(&gray_foreground_objects, true);

            let mut foreground_descriptors = polars::functions::concat_df_horizontal(&[
                intensity,
                texture,
                zernike,
            ]).unwrap();

            let column_names: Vec<String> = foreground_descriptors
                .get_column_names()
                .iter()
                .map(|s| s.to_owned().to_owned())
                .collect();

            column_names
                .iter()
                .for_each(|old| {
                    foreground_descriptors
                    .rename(old, format!("foreground_{}", old).as_str())
                    .expect(format!("cannot rename column {old}").as_str());
                });

            descriptors.push(foreground_descriptors);
        }

        if output.background_objects.is_some() {
            let gray_background_objects = convert_to_gray(&output.background_objects.unwrap());
            let intensity = batch_intensity_descriptors_df(
                &gray_background_objects,
                bins,
                with_zeros,
                with_max,
            );

            let texture = batch_texture_descriptors_df(&gray_background_objects);
            let zernike = batch_zernike_descriptors_df(&gray_background_objects, true);

            let mut background_descriptors = polars::functions::concat_df_horizontal(&[
                intensity,
                texture,
                zernike,
            ]).unwrap();

            let column_names: Vec<String> = background_descriptors
                .get_column_names()
                .iter()
                .map(|s| s.to_owned().to_owned())
                .collect();

            column_names
                .iter()
                .for_each(|old| {
                    background_descriptors
                    .rename(old, format!("background_{}", old).as_str())
                    .expect(format!("cannot rename column {old}").as_str());
                });

            descriptors.push(background_descriptors);
        }

        if output.binary_objects.is_some() {
            let binary_objects = mask::batch_binary_mask(&output.binary_objects.unwrap());
            let moments = batch_moments_descriptors_df(&binary_objects);
            let zernike = batch_zernike_descriptors_df(&binary_objects, true);

            let mut binary_descriptors = polars::functions::concat_df_horizontal(&[
                moments,
                zernike,
            ]).unwrap();

            let column_names: Vec<String> = binary_descriptors
                .get_column_names()
                .iter()
                .map(|s| s.to_owned().to_owned())
                .collect();

            column_names
                .iter()
                .for_each(|old| {
                    binary_descriptors
                    .rename(old, format!("binary_{}", old).as_str())
                    .expect(format!("cannot rename column {old}").as_str());
                });

            descriptors.push(binary_descriptors);
        }

        if output.polygons.is_some() {
            let polygons = output.polygons.unwrap();
            let polygons_descriptors = batch_polygon_descriptors_df(&polygons);
            descriptors.push(polygons_descriptors);
        }

        let descriptors = if descriptors.is_empty() {
            println!("No detect objects were available for computing descriptors. Please check the mode");
            DataFrame::new_no_checks(vec![])
        } else {
            let mut merged = polars::functions::concat_df_horizontal(&descriptors).unwrap();
            let labels = output.labels.unwrap().iter().map(|x| x.to_string()).collect::<Vec<String>>();
            let labels = Series::new("label", labels);
            let labels_df = DataFrame::new(vec![labels]).unwrap();
            merged = polars::functions::concat_df_horizontal(&[labels_df, merged]).unwrap();
            merged
        };

        ProcessorMeasurements {
            descriptors,
            n_labels: output.n_labels,
            has_error: output.has_error,
            mode: output.mode,
        }
    }
}

impl<P> ProcessorOutput<P> 
where
    P: Pixel<Subpixel = u8> + 'static,
    <P as Pixel>::Subpixel: 'static + From<u8>,
{
    fn _get_dynamic(&self, object: &Image<P>) -> DynamicImage {
        // TO-DO: Ideally we would just save images when they are in buffer format
        // as we can avoid overhead of converting them to DynamicImage; however,
        // this change will require a refactor of the numpy image writing since
        // we use the DynamicImage information to determine what type of image
        // is being written (see io/npy.rs)
        match P::CHANNEL_COUNT {
            1 => {
                let buffer: Image<Luma<u8>> = ImageBuffer::from_raw(
                    object.width(),
                    object.height(),
                    object.to_vec()
                ).unwrap();

                DynamicImage::ImageLuma8(buffer)
            },
            3 => {
                let buffer: Image<Rgb<u8>> = ImageBuffer::from_raw(
                    object.width(),
                    object.height(),
                    object.to_vec()
                ).unwrap();

                DynamicImage::ImageRgb8(buffer)
            },
            _ => {
                panic!("Unsupported number of channels");
            }
        }
    }

    fn _create_dir(&self, path: &std::path::Path) {
        if !path.exists() {
            std::fs::create_dir_all(path).expect("Failed to create directory");
        }
    }

    /// Write the output of the Processor to disk
    ///
    /// # Arguments
    ///
    /// * `path` - Path to write output data
    /// * `prefix` - Prefix to add to output filenames
    /// * `image_format` - Image format to save cropped object images (e.g. png)
    /// * `array_format` - Array format to save polygons, bounding boxes, and/or labels (e.g. json)
    /// * `folder_structure` - Folder structure when saving output data; 0, default; 1, each output in separate folder
    ///
    /// # Examples
    ///
    /// ```no_run
    /// use std::path::Path;
    /// use fqmv_core::utils::toy;
    /// use fqmv_core::data::Processor;
    ///
    /// let image = toy::rgb_image();
    /// let mask = toy::mask();
    ///
    /// let mut processor = Processor::new_from_mask(image, mask);
    /// let processed = processor.run(
    ///     Some(0),
    ///     Some((2, 2)),
    ///     Some("nearest".to_string()),
    ///     Some(32),
    ///     Some(false),
    ///     Some("omcbl".to_string())
    /// );
    ///
    /// processed.write(
    ///     Path::new("output"),
    ///     "image2",
    ///     Some("png".to_string()),
    ///     Some("json".to_string()),
    ///     Some(1),
    /// );
    /// ```
    pub fn write(&self,
        path: &std::path::Path,
        prefix: &str,
        image_format: Option<String>,
        array_format: Option<String>,
        folder_structure: Option<u8>,
    ) {
        if !path.exists() {
            std::fs::create_dir_all(path).expect("Failed to create directory");
        }

        if self.n_labels > 0 && !self.has_error {
            let image_format = image_format.unwrap_or("png".to_string());
            let array_format = array_format.unwrap_or("json".to_string());

            let labels = self.labels.clone().unwrap();

            if self.mode.contains('o') {
                for (i, object) in self.objects.clone().unwrap().iter().enumerate() {
                    self._create_dir(&path.join("objects"));

                    let i = labels[i];
                    let ext = format!("{}_object_{}.{}", prefix, i, image_format);

                    write_image(
                        path.join("objects").join(ext).to_str().unwrap(),
                        self._get_dynamic(object)
                    ).unwrap();
                }
            }

            if self.mode.contains('m') {
                for (i, masked_object) in self.foreground_objects.clone().unwrap().iter().enumerate() {
                    self._create_dir(&path.join("objects_foreground"));

                    let i = labels[i];
                    let ext = format!("{}_foreground_{}.{}", prefix, i, image_format);

                    write_image(
                        path.join("objects_foreground").join(ext).to_str().unwrap(),
                        self._get_dynamic(masked_object)
                    ).unwrap();
                }
            }

            if self.mode.contains('x') {
                for (i, masked_object) in self.background_objects.clone().unwrap().iter().enumerate() {
                    self._create_dir(&path.join("objects_background"));

                    let i = labels[i];
                    let ext = format!("{}_background_{}.{}", prefix, i, image_format);

                    write_image(
                        path.join("objects_background").join(ext).to_str().unwrap(),
                        self._get_dynamic(masked_object)
                    ).unwrap();
                }
            }

            if self.mode.contains('y') {
                for (i, binary_object) in self.binary_objects.clone().unwrap().iter().enumerate() {
                    self._create_dir(&path.join("objects_binary"));

                    let i = labels[i];
                    let ext = format!("{}_binary_{}.{}", prefix, i, image_format);

                    write_image(
                        path.join("objects_binary").join(ext).to_str().unwrap(),
                        DynamicImage::ImageLuma16(binary_object.clone())
                    ).unwrap();
                }
            }

            if self.mode.contains('p') {
                let mut ext = format!("{}_polygons.{}", prefix, array_format);
                if folder_structure.unwrap_or(0) == 1 {
                    self._create_dir(&path.join("polygons"));
                    ext = format!("polygons/{}", ext);
                }

                write_polygons(
                    path.join(ext).to_str().unwrap(),
                    &self.polygons.clone().unwrap()
                ).unwrap();
            }

            if self.mode.contains('b') {
                let mut ext = format!("{}_bounding_boxes.{}", prefix, array_format);
                if folder_structure.unwrap_or(0) == 1 {
                    self._create_dir(&path.join("bounding_boxes"));
                    ext = format!("bounding_boxes/{}", ext);
                }

                write_boxes(
                    path.join(ext).to_str().unwrap(),
                    &self.bounding_boxes.clone().unwrap()
                ).unwrap();
            }

            if self.mode.contains('l') {
                let mut ext = format!("{}_labels.{}", prefix, array_format);
                if folder_structure.unwrap_or(0) == 1 {
                    if !path.join("labels").exists() {
                        std::fs::create_dir_all(path.join("labels")).expect("Failed to create directory");
                    }
                    ext = format!("labels/{}", ext);
                }

                write_labels(
                    &path.join(ext).to_str().unwrap(),
                    &labels
                ).unwrap();
            }
        }
    }
}

impl ProcessorMeasurements {
    /// Write measurements as DataFrame to disk
    pub fn write(&mut self, output: &str, id: Option<&str>) {
        if id.is_some() {
            let ids = Series::new("id", vec![id.unwrap(); self.descriptors.height()]);
            let ids_df = DataFrame::new(vec![ids]).unwrap();
            let mut descriptors = polars::functions::concat_df_horizontal(&[
                ids_df,
                self.descriptors.to_owned()
            ]).unwrap();

            write_table(&mut descriptors, output);
        } else {
            write_table(&mut self.descriptors, output);
        }
    }
    
    pub fn add_id(&mut self, id: &str) {
        let ids = Series::new("id", vec![id; self.descriptors.height()]);
        let ids_df = DataFrame::new(vec![ids]).unwrap();
        self.descriptors = polars::functions::concat_df_horizontal(&[
            ids_df,
            self.descriptors.to_owned()
        ]).unwrap();
    }
}

/// A container for holding the current valid processor outputs
pub enum ProcessorContainer {
    Gray8(ProcessorOutput<Luma<u8>>),
    Rgb8(ProcessorOutput<Rgb<u8>>),
}

impl ProcessorContainer {
    /// Return the number of labels in the ProcessorOutput
    pub fn n_labels(&self) -> usize {
        match self {
            ProcessorContainer::Gray8(output) => output.n_labels,
            ProcessorContainer::Rgb8(output) => output.n_labels,
        }
    }

    /// Return whether the ProcessorOutput has an error
    pub fn has_error(&self) -> bool {
        match self {
            ProcessorContainer::Gray8(output) => output.has_error,
            ProcessorContainer::Rgb8(output) => output.has_error,
        }
    }

    /// Write the ProcessorOutput to disk
    pub fn write(&self,
        path: &std::path::Path,
        prefix: &str,
        image_format: Option<String>,
        array_format: Option<String>,
        folder_structure: Option<u8>,
    ) {
        match self {
            ProcessorContainer::Gray8(output) => {
                output.write(
                    path,
                    prefix,
                    image_format,
                    array_format,
                    folder_structure,
                );
            },
            ProcessorContainer::Rgb8(output) => {
                output.write(
                    path,
                    prefix,
                    image_format,
                    array_format,
                    folder_structure,
                );
            },
        }
    }
}
