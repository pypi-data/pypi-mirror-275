use std::sync::Mutex;
use rayon::prelude::*;
use kdam::TqdmParallelIterator;

use crate::io::read_polygons;
use crate::io::{read_table, write_table_descriptors};
use crate::helpers::{progress_log, progress_bar, does_parent_dir_exist};

use crate::descriptors::form::polygon_descriptors;
use crate::descriptors::batch::batch_polygon_descriptors;
use crate::descriptors::names::POLYGON_DESCRIPTOR_NAMES;

/// Compute morphometric descriptors for polygon shapes
///
/// # Arguments
///
/// * `polygons_path` - A string containing the path to the polygons file
/// * `identifiers_path` - A string containing the path to the identifiers file
/// * `output_path` - A string containing the path to the output file
/// * `threads` - An optional integer specifying the number of threads to use
///
/// # Examples
/// ```no_run
/// use fqmv_core::data::runners::measure_polygons_runner;
///
/// measure_polygons_runner(
///     Some("polygons.json".to_string()),
///     Some("identifiers.csv".to_string()),
///     Some("polygon_descriptors.csv".to_string()),
///     None
/// );
/// ```
pub fn measure_polygons_runner(
    polygons_path: Option<String>,
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

    if polygons_path.is_none() {
        println!("Polygons input path must be specified");
        std::process::exit(1);
    }

    if output_path.is_none() {
        println!("Output path must be specified");
        std::process::exit(1);
    }

    let check = [
        (
            polygons_path.as_deref(),
            "Polygons parent directory does not exist",
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

    let polygons_path = polygons_path.expect("Polygons path cannot be empty");
    let polygons_path = std::path::Path::new(&polygons_path);

    progress_log("Measuring polygon descriptors");

    let identifiers = identifiers_path.as_deref();
    let identifiers = match identifiers {
        Some(id) => Some(read_table(id).unwrap()),
        None => None,
    };

    if polygons_path.is_dir() {
        progress_log("Input path is a directory. Assuming all .json, .npy, .bin, and .fqmv files are polygons.");

        let files = std::fs::read_dir(polygons_path)
            .expect("Failed to read directory")
            .map(|res| res.map(|e| e.path()))
            .collect::<Result<Vec<_>, std::io::Error>>()
            .expect("Failed to collect files");

        let files = files
            .iter()
            .filter(|f| {
                f.extension().is_some()
                    && (f.extension().unwrap() == "json"
                        || f.extension().unwrap() == "npy"
                        || f.extension().unwrap() == "bin"
                        || f.extension().unwrap() == "fqmv")
            })
            .collect::<Vec<_>>();

        if files.is_empty() {
            println!("No valid polygon files found in provided directory");
            std::process::exit(1);
        }

        let pb = progress_bar(files.len(), "Computing polygon descriptors");

        let descriptors = Mutex::new(vec![]);

        (0..files.len())
            .into_par_iter()
            .tqdm_with_bar(pb)
            .for_each(|i| {
                let polygons = read_polygons(files[i].to_str().unwrap())
                    .expect("Failed to read polygons file");

                for polygon in polygons.iter() {
                    let descriptor = polygon_descriptors(polygon);
                    descriptors.lock().unwrap().push(descriptor);
                }
        });

        let filenames = files
            .iter()
            .map(|f| f.file_name().unwrap().to_str().unwrap())
            .collect::<Vec<_>>();

        let descriptors = descriptors.into_inner().unwrap();

        write_table_descriptors(
            &descriptors,
            &POLYGON_DESCRIPTOR_NAMES.iter().map(|&s| s).collect(),
            identifiers.as_ref(),
            Some(filenames),
            output_path.as_deref().unwrap(),
        );

    } else {
        let polygons = read_polygons(polygons_path.to_str().unwrap())
            .expect("Failed to read polygons file");

        let descriptors: Vec<Vec<f64>> = batch_polygon_descriptors(&polygons, true);

        write_table_descriptors(
            &descriptors,
            &POLYGON_DESCRIPTOR_NAMES.iter().map(|&s| s).collect(),
            identifiers.as_ref(),
            None,
            output_path.as_deref().unwrap(),
        );
    }

    progress_log("Run complete.");
}
