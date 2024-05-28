use rayon::prelude::*;
use kdam::TqdmParallelIterator;

use crate::io::read_image;
use crate::io::{read_table, write_table_descriptors};
use crate::helpers::{progress_log, progress_bar, thousands_format, does_parent_dir_exist};

use crate::descriptors::moments::moments_descriptors;
use crate::descriptors::names::MOMENTS_DESCRIPTOR_NAMES;

/// Compute moments descriptors from object images
///
/// # Arguments
///
/// * `objects_path` - A string containing the path to the objects file
/// * `identifiers_path` - A string containing the path to the identifiers file
/// * `output_path` - A string containing the path to the output file
/// * `threads` - An optional integer specifying the number of threads to use
///
/// # Examples
/// ```no_run
/// use fqmv_core::data::runners::measure_moments_runner;
///
/// measure_moments_runner(
///     Some("object.png".to_string()),
///     Some("identifiers.csv".to_string()),
///     Some("descriptors.csv".to_string()),
///     None,
/// );
/// ```
pub fn measure_moments_runner(
    objects_path: Option<String>,
    identifiers_path: Option<String>,
    output_path: Option<String>,
    threads: Option<usize>,
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

    if objects_path.is_none() {
        println!("Objects input path must be specified");
        std::process::exit(1);
    }

    if output_path.is_none() {
        println!("Output path must be specified");
        std::process::exit(1);
    }

    let check = [
        (
            objects_path.as_deref(),
            "Objects parent directory does not exist",
        ),
        (
            output_path.as_deref(),
            "Output parent directory does not exist",
        ),
        (
            identifiers_path.as_deref(),
            "Identifiers parent directory does not exist",
        ),
    ];

    for (path, parent_error) in check.iter() {
        if let Some(path) = path {
            does_parent_dir_exist(path, parent_error);
        }
    }

    let objects_path = objects_path.expect("objects path cannot be empty");
    let objects_path = std::path::Path::new(&objects_path);

    progress_log("Measuring moments descriptors");

    let identifiers = identifiers_path.as_deref();
    let identifiers = match identifiers {
        Some(id) => Some(read_table(id).unwrap()),
        None => None,
    };

    let n_objects = if objects_path.is_dir() {
        progress_log("Input path is a directory. Assuming all valid image formats (including npy) are objects.");

        let files = std::fs::read_dir(objects_path)
            .expect("Failed to read directory")
            .map(|res| res.map(|e| e.path()))
            .collect::<Result<Vec<_>, std::io::Error>>()
            .expect("Failed to collect files");

        let mut files = files
            .iter()
            .filter(|f| {
                f.extension().is_some()
                    && (f.extension().unwrap() == "jpeg"
                        || f.extension().unwrap() == "jpg"
                        || f.extension().unwrap() == "png"
                        || f.extension().unwrap() == "bmp"
                        || f.extension().unwrap() == "tiff"
                        || f.extension().unwrap() == "tif"
                        || f.extension().unwrap() == "hdr"
                        || f.extension().unwrap() == "pbm"
                        || f.extension().unwrap() == "avif"
                        || f.extension().unwrap() == "tga"
                        || f.extension().unwrap() == "qoi"
                        || f.extension().unwrap() == "exr"
                        || f.extension().unwrap() == "webp"
                        || f.extension().unwrap() == "npy")
            })
            .collect::<Vec<_>>();

        if files.is_empty() {
            println!("No valid polygon files found in provided directory");
            std::process::exit(1);
        }

        files.sort();

        let pb = progress_bar(files.len(), "Computing moments descriptors");

        let descriptors: Vec<Vec<f64>> = files
            .par_iter()
            .tqdm_with_bar(pb)
            .map(|file| {
                let object = read_image(file.to_str().unwrap())
                    .expect(format!(
                        "Failed to read object image: {}",
                        file.to_str().unwrap()
                ).as_str());

                let descriptor = moments_descriptors(&object.to_luma8());

                descriptor
        }).collect();

        let filenames = files
            .iter()
            .map(|f| f.file_name().unwrap().to_str().unwrap())
            .collect::<Vec<_>>();

        write_table_descriptors(
            &descriptors,
            &MOMENTS_DESCRIPTOR_NAMES.iter().map(|&s| s).collect(),
            identifiers.as_ref(),
            Some(filenames),
            output_path.as_deref().unwrap(),
        );

        files.len()
    } else {
        let object = read_image(objects_path.to_str().unwrap())
            .expect("Failed to read objects file");

        let descriptors = moments_descriptors(&object.to_luma8());

        write_table_descriptors(
            &vec![descriptors],
            &MOMENTS_DESCRIPTOR_NAMES.iter().map(|&s| s).collect(),
            identifiers.as_ref(),
            None,
            output_path.as_deref().unwrap(),
        );

        1
    };

    progress_log(format!(
        "Run complete. Measured moments for {} objects.",
        thousands_format(n_objects)
    ).as_str());
}
