use std::sync::Mutex;
use std::io::{Error, ErrorKind};
use rayon::prelude::*;
use kdam::TqdmParallelIterator;
use image::ColorType;

use crate::types::Mask;
use crate::data::ImageContainer;
use crate::io::read_image;
use crate::data::processor::{Processor, ProcessorContainer};
use crate::helpers::{progress_log, progress_bar, thousands_format, is_valid_string};

/// Load an image and its associated mask from disk
///
/// # Arguments
///
/// * `image_path` - A string slice that holds the path to the image file
/// * `mask_path` - A string slice that holds the path to the mask file
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::data::runners::load_image_mask;
/// let (image, mask) = load_image_mask("image.png", "mask.png").unwrap();
/// ```
pub fn load_image_mask(
    image_path: &str,
    mask_path: &str,
) -> Result<(ImageContainer, Mask), Error> {
    let image = read_image(image_path)?;
    let mask = read_image(mask_path)?;

    let image = match image.color() {
        ColorType::L8 | ColorType::La8 | ColorType::L16 | ColorType::La16 => {
            ImageContainer::Gray8(image.into_luma8())
        },
        ColorType::Rgb8 | ColorType::Rgba8 | ColorType::Rgb16  | ColorType::Rgba16 => {
            ImageContainer::Rgb8(image.into_rgb8())
        },
        _ => return Err(Error::new(
            ErrorKind::InvalidData,
            "Unsupported image type".to_string(),
        )),
    };

    let mask = match mask.color() {
        ColorType::L8 | ColorType::La8 | ColorType::L16 | ColorType::La16 => {
            let bytes_per_pixel = mask.color().bytes_per_pixel();
            let mut data = mask.into_luma16();
            if bytes_per_pixel == 1 {
                for p in data.pixels_mut() {
                    p[0] /= 257; 
                }
            }
            data
        },
        _ => return Err(Error::new(
            ErrorKind::InvalidData,
            "Unsupported mask type".to_string(),
        )),
    };

    Ok((image, mask))
}

/// Perform batch collection of morphological readouts from image-mask pairs
///
/// # Arguments
///
/// * `image_path` - Path to the directory containing images
/// * `masks_path` - Path to the directory containing image masks
/// * `image_suffix` - The suffix denoting image files (e.g. "_image")
/// * `masks_suffix` - The suffix denoting mask files (e.g. "_mask")
/// * `resize_width` - Width to resize cropped objects extracted from images
/// * `resize_height` - Height to resize cropped objects extracted from images
/// * `resize_filter` - Filter to use for resizing
/// * `pad` - Optional padding to add around cropped objects and bounding boxes
/// * `n_resample` - Number of equidistant points to resample polygon outlines to
/// * `exclude_borders` - If True, exclude objects that touch the image border
/// * `mode` - Processing mode (default: "ombpl"); can be any combination of "o", "m", "b", "c", "l", "y", or "x"
/// * `threads` - Number of threads to use for parallel processing (defaults to all available)
/// * `output_path` - Path to the directory to save output files
/// * `output_image_format` - Format to save output cropped object images (default: "png")
/// * `output_array_format` - Format to save output contours, boxes, and labels (default: "npy")
/// * `output_structure` - Output structure (default: 0); can be 0 (by image) or 1 (by object)
pub fn process_image_mask_runner(
    image_path: Option<String>,
    masks_path: Option<String>,
    image_suffix: Option<String>,
    masks_suffix: Option<String>,
    resize_width: Option<u32>,
    resize_height: Option<u32>,
    resize_filter: Option<String>,
    pad: Option<u32>,
    n_resample: Option<usize>,
    exclude_borders: Option<bool>,
    mode: Option<String>,
    threads: Option<usize>,
    output_path: Option<String>,
    output_image_format: Option<String>,
    output_array_format: Option<String>,
    output_structure: Option<u8>,
) {
    if let Some(threads) = threads {
        if threads < 1 {
            println!("Threads must be set to a positive integer");
            std::process::exit(1);
        }

        rayon::ThreadPoolBuilder::new()
            .num_threads(threads)
            .build_global()
            .unwrap();
    }

    let image_path = image_path.expect("Image path cannot be empty");
    let masks_path = masks_path.unwrap_or(image_path.clone());

    let image_path = std::path::Path::new(&image_path);
    let masks_path = std::path::Path::new(&masks_path);

    let input_structure = match image_path == masks_path {
        true => "same_folder",
        false => "different_folders",
    };

    let (image_suffix, masks_suffix) = match (image_suffix, masks_suffix) {
        (Some(image), Some(mask)) => (image, mask),
        (Some(image), None) => (image, "".to_string()),
        (None, Some(mask)) => ("".to_string(), mask),
        (None, None) => ("".to_string(), "".to_string()),
    }; 

    if input_structure == "same_folder" && image_suffix == masks_suffix {
        println!("When images and masks are stored in same folder, the image and mask suffixes must be different.");
        std::process::exit(1);
    }

    let check_mode = mode.as_deref().unwrap_or("oypbl");
    if !check_mode.contains('o')
        && !check_mode.contains('m') 
        && !check_mode.contains('b') 
        && !check_mode.contains('p') 
        && !check_mode.contains('l') 
        && !check_mode.contains('x')
        && !check_mode.contains('y')
        && is_valid_string(check_mode, &['o', 'm', 'b', 'p', 'l', 'x', 'y'])
    {
        println!("Invalid processing mode. Mode must/can only contain at least one of the following: o, m, b, p, l, x, y.");
        std::process::exit(1);
    }

    progress_log(format!(
        "Processing image-mask pairs using mode {}", 
        mode.as_deref().unwrap_or("ombpl")).as_str()
    );

    let resize = match (resize_width, resize_height) {
        (Some(width), Some(height)) if width < 1 || height < 1 => {
            println!("Invalid resize dimensions. Width and height must be positive integers.");
            std::process::exit(1);
        }
        (Some(_), None) | (None, Some(_)) => {
            println!("Invalid resize dimensions. Both width and height must be provided.");
            std::process::exit(1);
        }
        (Some(width), Some(height)) => Some((width, height)),
        _ => None,
    };
    
    match n_resample {
        Some(n) if n < 3 => {
            println!("Invalid n_resample value. n_resample must be at least 3.");
            std::process::exit(1);
        }
        _ => {}
    }

    let output_path = output_path.expect("Output path cannot be empty");
    let output_path = std::path::Path::new(&output_path);
    if !output_path.exists() {
        std::fs::create_dir_all(output_path).expect("Failed to create directory");
    }

    progress_log(&format!("Initialized output at {}", output_path.to_str().unwrap()));

    let images = std::fs::read_dir(image_path).expect("Failed to read image directory")
        .map(|entry| entry.unwrap().path())
        .filter(|path| {
            path.is_file() && path.file_stem().unwrap().to_str().unwrap().ends_with(&image_suffix)
        })
        .collect::<Vec<_>>();

    let masks = std::fs::read_dir(masks_path).expect("Failed to read mask directory")
        .map(|entry| entry.unwrap().path())
        .filter(|path| {
            path.is_file() && path.file_stem().unwrap().to_str().unwrap().ends_with(&masks_suffix)
        })
        .collect::<Vec<_>>();

    progress_log(&format!(
        "Found {} candidate images and {} candidate segmentation masks.", 
        &thousands_format(images.len()),
        &thousands_format(masks.len())
    ));

    let image_mask_pairs = images.par_iter()
        .map(|image| {
            let image_prefix = image.file_name().unwrap()
                .to_str().unwrap()
                .split(&image_suffix)
                .collect::<Vec<_>>()[0];

            let segment = masks.iter()
                .find(|segment| {
                    segment.to_str().unwrap().contains(image_prefix)
                });

            (image_prefix, image, segment)
        })
        .collect::<Vec<_>>();

    progress_log(&format!(
        "Detected and validated {} image-mask pairs.",
        &thousands_format(image_mask_pairs.len())
    ));

    match images.len().cmp(&image_mask_pairs.len()) {
        std::cmp::Ordering::Less => {
            progress_log(&format!(
                "Warning: {} images were did not have a paired segmentation mask.",
                &thousands_format(images.len() - image_mask_pairs.len())
            ));
        }
        std::cmp::Ordering::Greater => {
            progress_log(&format!(
                "Warning: {} segmentation masks were did not have a paired image.",
                &thousands_format(masks.len() - image_mask_pairs.len())
            ));
        }
        _ => (),
    }

    let pb = progress_bar(image_mask_pairs.len(), "Generating outputs");

    let object_none = Mutex::new(vec![]);
    let object_error = Mutex::new(vec![]);
    let object_counts = Mutex::new(vec![]);
    let object_images = Mutex::new(vec![]);

    (0..image_mask_pairs.len())
        .into_par_iter()
        .tqdm_with_bar(pb)
        .for_each(|i| {
            let image_prefix = image_mask_pairs[i].0;
            if image_mask_pairs[i].2.is_none() {
                object_none.lock().unwrap().push(image_prefix);
                return;
            }

            match load_image_mask(
                image_mask_pairs[i].1.to_str().unwrap(),
                image_mask_pairs[i].2.as_ref().unwrap().to_str().unwrap(),
            ) {
                Err(_) => {
                    object_error.lock().unwrap().push(image_prefix);
                    return;
                }
                Ok((img, mask)) => {
                let processed = match img {
                    ImageContainer::Gray8(img) => {
                        let mut processor = Processor::new_from_mask(img, mask);
                        let output = processor.run(
                            pad,
                            resize,
                            resize_filter.clone(),
                            n_resample,
                            exclude_borders,
                            mode.clone(),
                        );

                        ProcessorContainer::Gray8(output)
                    },
                    ImageContainer::Rgb8(img) => {
                        let mut processor = Processor::new_from_mask(img, mask);
                        let output = processor.run(
                            pad,
                            resize,
                            resize_filter.clone(),
                            n_resample,
                            exclude_borders,
                            mode.clone(),
                        );

                        ProcessorContainer::Rgb8(output)
                    },
                };

                if processed.n_labels() == 0 {
                    object_none.lock().unwrap().push(image_prefix);
                } else if processed.has_error() {
                    object_error.lock().unwrap().push(image_prefix);
                } else {
                    let output_path_ = match output_structure.unwrap_or(0) {
                        0 => output_path.join("data/").join(image_prefix),
                        1 => output_path.to_path_buf(),
                        _ => panic!("Invalid output structure. Must be 0 or 1."),
                    };

                    processed.write(
                        &output_path_,
                        image_prefix,
                        output_image_format.clone(),
                        output_array_format.clone(),
                        output_structure,
                    );

                    object_counts.lock().unwrap().push(processed.n_labels());
                    object_images.lock().unwrap().push(image_prefix);
                }
            }
        }
    });

    let n_none = object_none.lock().unwrap().len();
    let n_error = object_error.lock().unwrap().len();

    if n_none > 0 {
        progress_log(&format!(
            "Warning: No objects identified in {} images (see object_none.txt for identifiers).",
            &thousands_format(object_none.lock().unwrap().len())
        ));

        std::fs::write(
            output_path.join("object_none.txt"),
            object_none.lock().unwrap().join("\n")
        ).unwrap();
    }

    if n_error > 0 {
        progress_log(&format!(
            "Warning: Errors encountered in {} images (see object_error.txt for identifiers).",
            &thousands_format(object_error.lock().unwrap().len())
        ));

        std::fs::write(
            output_path.join("object_error.txt"),
            object_error.lock().unwrap().join("\n")
        ).unwrap();
    }

    let total_images = image_mask_pairs.len() - n_none - n_error;
    let total_objects = object_counts.lock().unwrap().iter().sum::<usize>();
    let mean_objects = total_objects as f64 / total_images as f64;

    std::fs::write(
        output_path.join("object_counts.txt"),
        object_images.lock().unwrap().iter().zip(object_counts.lock().unwrap().iter())
            .map(|(name, count)| format!("{}\t{}", name, count))
            .collect::<Vec<_>>()
            .join("\n")
    ).unwrap();

    std::fs::write(
        output_path.join("object_summary.txt"),
        format!(
            "Detected objects: {}\nRetained objects: {}\nExcluded objects: {}\nTotal images: {}\nMean objects per image: {}",
            total_objects + n_none + n_error,
            total_objects,
            n_none + n_error,
            total_images,
            mean_objects.round() as usize,
        )
    ).unwrap();

    let parameters = serde_json::json!({
        "image_path": image_path.to_str().unwrap(),
        "masks_path": masks_path.to_str().unwrap(),
        "image_suffix": image_suffix,
        "masks_suffix": masks_suffix,
        "resize_width": resize_width,
        "resize_height": resize_height,
        "resize_filter": resize_filter,
        "pad": pad,
        "n_resample": n_resample,
        "exclude_borders": exclude_borders,
        "mode": mode,
        "threads": threads,
        "output_path": output_path.to_str().unwrap(),
        "output_image_format": output_image_format,
        "output_array_format": output_array_format,
        "output_structure": output_structure,
    });

    std::fs::write(
        output_path.join("parameters.json"),
        serde_json::to_string_pretty(&parameters).unwrap(),
    ).unwrap();

    progress_log(&format!(
        "Run complete. Identified {} objects in {} images (mean: {} objects/image).",
        &thousands_format(total_objects),
        &thousands_format(total_images),
        mean_objects.round() as usize,
    ));
}
