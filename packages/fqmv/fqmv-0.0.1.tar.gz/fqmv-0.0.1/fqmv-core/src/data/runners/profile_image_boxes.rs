use std::sync::Mutex;
use rayon::prelude::*;
use polars::prelude::*;
use kdam::TqdmParallelIterator;

use crate::data::ImageContainer;
use crate::data::processor::Processor;
use crate::io::table::write_table;
use crate::helpers::{progress_log, progress_bar, thousands_format, is_valid_string};

use crate::data::runners::load_image_boxes;

/// Perform batch morphological profiling from image-boxes pairs
///
/// # Arguments
///
/// * `image_path` - Path to the directory containing images
/// * `boxes_path` - Path to the directory containing image boxes
/// * `image_suffix` - The suffix denoting image files (e.g. "_image")
/// * `boxes_suffix` - The suffix denoting boxes files (e.g. "_boxes")
/// * `resize_width` - Width to resize cropped objects extracted from images
/// * `resize_height` - Height to resize cropped objects extracted from images
/// * `resize_filter` - Filter to use for resizing
/// * `pad` - Optional padding to add around cropped objects and bounding boxes
/// * `exclude_borders` - If True, exclude objects that touch the image border
/// * `mode` - Processing mode (default: "obly"); can be any combination of "o", "b", "l", or "y"
/// * `bins` - Number of bins to use for computing certain intensity histogram descriptors
/// * `with_zeros` - If True, include zero values when computing intensity descriptors
/// * `with_max` - Maximum value to use when normalizing intensity descriptors
/// * `threads` - Number of threads to use for parallel processing (defaults to all available)
/// * `output_path` - Path to the directory to save output files
/// * `concatenate` - If True, concatenate descriptors into single dataframe instead of saving one table per image (defaults to true)
pub fn profile_image_boxes_runner(
    image_path: Option<String>,
    boxes_path: Option<String>,
    image_suffix: Option<String>,
    boxes_suffix: Option<String>,
    resize_width: Option<u32>,
    resize_height: Option<u32>,
    resize_filter: Option<String>,
    pad: Option<u32>,
    exclude_borders: Option<bool>,
    mode: Option<String>,
    bins: Option<usize>,
    with_zeros: Option<bool>,
    with_max: Option<f64>,
    threads: Option<usize>,
    output_path: Option<String>,
    concatenate: Option<bool>,
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
    let boxes_path = boxes_path.unwrap_or(image_path.clone());

    let image_path = std::path::Path::new(&image_path);
    let boxes_path = std::path::Path::new(&boxes_path);

    let concatenate = concatenate.unwrap_or(true);

    let input_structure = match image_path == boxes_path {
        true => "same_folder",
        false => "different_folders",
    };

    let (image_suffix, boxes_suffix) = match (image_suffix, boxes_suffix) {
        (Some(image), Some(boxes)) => (image, boxes),
        (Some(image), None) => (image, "".to_string()),
        (None, Some(boxes)) => ("".to_string(), boxes),
        (None, None) => ("".to_string(), "".to_string()),
    }; 

    if input_structure == "same_folder" && image_suffix == boxes_suffix {
        println!("When images and boxes are stored in same folder, the image and boxes suffixes must be different.");
        std::process::exit(1);
    }

    let check_mode = mode.as_deref().unwrap_or("obl");
    if !check_mode.contains('o')
        && !check_mode.contains('b') 
        && !check_mode.contains('l') 
        && is_valid_string(check_mode, &['o', 'b', 'l'])
    {
        println!("Invalid processing mode. Mode must/can only contain at least one of the following: o, b, l.");
        std::process::exit(1);
    }

    progress_log(format!(
        "Processing image-boxes pairs using mode {}", 
        mode.as_deref().unwrap_or("obl")).as_str()
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
    
    let output_path = output_path.expect("Output path cannot be empty");
    let output_path = std::path::Path::new(&output_path);
    if !output_path.exists() {
        std::fs::create_dir_all(output_path).expect("Failed to create directory");

        if !concatenate {
            std::fs::create_dir_all(output_path.join("descriptors")).expect("Failed to create directory");
        }
    }

    progress_log(&format!("Initialized output at {}", output_path.to_str().unwrap()));

    let images = std::fs::read_dir(image_path).expect("Failed to read image directory")
        .map(|entry| entry.unwrap().path())
        .filter(|path| {
            path.is_file() && path.file_stem().unwrap().to_str().unwrap().ends_with(&image_suffix)
        })
        .collect::<Vec<_>>();

    let boxes = std::fs::read_dir(boxes_path).expect("Failed to read boxes directory")
        .map(|entry| entry.unwrap().path())
        .filter(|path| {
            path.is_file() && path.file_stem().unwrap().to_str().unwrap().ends_with(&boxes_suffix)
        })
        .collect::<Vec<_>>();

    progress_log(&format!(
        "Found {} candidate images and {} candidate segmentation boxes.", 
        &thousands_format(images.len()),
        &thousands_format(boxes.len())
    ));

    let image_boxes_pairs = images.par_iter()
        .map(|image| {
            let image_prefix = image.file_name().unwrap()
                .to_str().unwrap()
                .split(&image_suffix)
                .collect::<Vec<_>>()[0];

            let segment = boxes.iter()
                .find(|segment| {
                    segment.to_str().unwrap().contains(image_prefix)
                });

            (image_prefix, image, segment)
        })
        .collect::<Vec<_>>();

    progress_log(&format!(
        "Detected and validated {} image-boxes pairs.",
        &thousands_format(image_boxes_pairs.len())
    ));

    match images.len().cmp(&image_boxes_pairs.len()) {
        std::cmp::Ordering::Less => {
            progress_log(&format!(
                "Warning: {} images were did not have a paired segmentation boxes.",
                &thousands_format(images.len() - image_boxes_pairs.len())
            ));
        }
        std::cmp::Ordering::Greater => {
            progress_log(&format!(
                "Warning: {} segmentation boxes were did not have a paired image.",
                &thousands_format(boxes.len() - image_boxes_pairs.len())
            ));
        }
        _ => (),
    }

    let pb = progress_bar(image_boxes_pairs.len(), "Computing measurements");

    let object_none = Mutex::new(vec![]);
    let object_error = Mutex::new(vec![]);
    let object_counts = Mutex::new(vec![]);
    let object_images = Mutex::new(vec![]);
    let descriptors = Mutex::new(vec![]);

    (0..image_boxes_pairs.len())
        .into_par_iter()
        .tqdm_with_bar(pb)
        .for_each(|i| {
            let image_prefix = image_boxes_pairs[i].0;
            if image_boxes_pairs[i].2.is_none() {
                object_none.lock().unwrap().push(image_prefix);
                return;
            }

            match load_image_boxes(
                image_boxes_pairs[i].1.to_str().unwrap(),
                image_boxes_pairs[i].2.as_ref().unwrap().to_str().unwrap(),
            ) {
                Err(_) => {
                    object_error.lock().unwrap().push(image_prefix);
                    return;
                }
                Ok((img, boxes)) => {
                let mut measurements = match img {
                    ImageContainer::Gray8(img) => {
                        let mut processor = Processor::new_from_boxes(img, boxes);
                        let output = processor.profile(
                            pad,
                            resize,
                            resize_filter.clone(),
                            None,
                            exclude_borders,
                            mode.clone(),
                            bins,
                            with_zeros,
                            with_max,
                        );

                        output
                    },
                    ImageContainer::Rgb8(img) => {
                        let mut processor = Processor::new_from_boxes(img, boxes);
                        let output = processor.profile(
                            pad,
                            resize,
                            resize_filter.clone(),
                            None,
                            exclude_borders,
                            mode.clone(),
                            bins,
                            with_zeros,
                            with_max,
                        );

                        output
                    },
                };

                if measurements.n_labels == 0 {
                    object_none.lock().unwrap().push(image_prefix);
                } else if measurements.has_error {
                    object_error.lock().unwrap().push(image_prefix);
                } else {
                    let output_path_ = output_path
                        .join("descriptors")
                        .join(format!("{}.csv", image_prefix));

                    if !concatenate {
                        measurements.write(
                            &output_path_.to_str().unwrap(),
                            Some(image_prefix),
                        );
                    } else {
                        measurements.add_id(image_prefix);
                        descriptors.lock().unwrap().push(measurements.descriptors);
                    }

                    object_counts.lock().unwrap().push(measurements.n_labels);
                    object_images.lock().unwrap().push(image_prefix);
                }
            }
        }
    });

    if concatenate {
        let descriptors = descriptors.lock().unwrap();

        let descriptors = descriptors.iter()
            .map(|df| df.clone().lazy())
            .collect::<Vec<_>>();

        let mut descriptors = concat(
            descriptors,
            UnionArgs::default()
        ).unwrap().collect().unwrap();

        write_table(
            &mut descriptors,
            format!("{}/{}", output_path.to_str().unwrap(), "descriptors.csv").as_str(),
        );
    }

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

    let total_images = image_boxes_pairs.len() - n_none - n_error;
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
        "boxes_path": boxes_path.to_str().unwrap(),
        "image_suffix": image_suffix,
        "boxes_suffix": boxes_suffix,
        "resize_width": resize_width,
        "resize_height": resize_height,
        "resize_filter": resize_filter,
        "pad": pad,
        "exclude_borders": exclude_borders,
        "mode": mode,
        "threads": threads,
        "output_path": output_path.to_str().unwrap(),
    });

    std::fs::write(
        output_path.join("parameters.json"),
        serde_json::to_string_pretty(&parameters).unwrap(),
    ).unwrap();

    progress_log(&format!(
        "Run complete. Computed descriptors for {} objects in {} images (mean: {} objects/image).",
        &thousands_format(total_objects),
        &thousands_format(total_images),
        mean_objects.round() as usize,
    ));
}
