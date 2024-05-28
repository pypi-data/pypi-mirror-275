use std::fs::File;
use std::path::Path;
use std::collections::HashMap;
use std::fmt::{Display, Debug};
use std::io::{Error, ErrorKind, Read, BufReader, Write, BufWriter};

use serde::Serialize;
use serde_json::value::Value;
use bincode;

use crate::Numeric;
use crate::io::npy::{read_numpy, write_numpy};

/// Read polygons from a json file
///
/// # Arguments
///
/// * `path` - Path to the json file
///
/// # Examples
///
/// ```no_run
/// use std::path::Path;
/// use fqmv_core::io::polygons::read_polygons_json;
/// let path = Path::new("data/polygons.json");
/// let polygons = read_polygons_json(path).unwrap();
/// ```
pub fn read_polygons_json(path: &Path) -> Result<Vec<Vec<[f64; 2]>>, Error> {
    let mut file = File::open(path)?;
    let mut contents = String::new();
    file.read_to_string(&mut contents)?;

    let data: Value = serde_json::from_str(&contents)?;

    let valid_keys = vec![
        "polygons",
        "contours",
        "outlines",
        "shapes",
        "points",
    ];

    for key in valid_keys {
        if let Some(boxes) = data.get(key) {
            let boxes = boxes.as_array().ok_or(Error::new(
                ErrorKind::InvalidData,
                "Invalid polygon/contour array format",
            ))?;

            let boxes = boxes.iter()
                .filter_map(Value::as_array)
                .map(|b| {
                    b.iter()
                        .filter_map(Value::as_array)
                        .map(|xy| { [
                            xy.get(0).and_then(Value::as_f64).unwrap_or(0.0),
                            xy.get(1).and_then(Value::as_f64).unwrap_or(0.0)
                        ] })
                        .collect::<Vec<[f64; 2]>>()
                })
                .collect::<Vec<Vec<[f64; 2]>>>();

            return Ok(boxes);
        }
    }
    
    Err(Error::new(
        std::io::ErrorKind::InvalidData,
        "Key not found in polygon/contour json data",
    ))
}

/// Write polygons to a json file
///
/// # Arguments
///
/// * `path` - Path to the json file
///
/// # Examples
///
/// ```no_run
/// use std::path::Path;
/// use fqmv_core::utils::toy;
/// use fqmv_core::io::polygons::write_polygons_json;
/// let path = Path::new("data/polygons.json");
/// let polygons = toy::polygons();
/// write_polygons_json(path, &polygons).unwrap();
/// ```
pub fn write_polygons_json<T>(path: &Path, polygons: &[Vec<[T; 2]>]) -> Result<(), Error> 
where
    T: Serialize + Display + Debug
{
    let file = File::create(path)?;
    let mut writer = BufWriter::new(&file);
    let mut map = HashMap::new();
    map.insert("polygons", polygons);
    serde_json::to_writer(&mut writer, &map)?;
    writer.flush()
}

/// Read polygons from a numpy file
///
/// # Arguments
///
/// * `path` - Path to the numpy file
///
/// # Examples
///
/// ```no_run
/// use std::path::Path;
/// use fqmv_core::io::polygons::read_polygons_numpy;
/// let path = Path::new("data/polygons.npy");
/// let polygons = read_polygons_numpy(path).unwrap();
/// ```
pub fn read_polygons_numpy(path: &Path) -> Result<Vec<Vec<[f64; 2]>>, Error> {
    let (data, shape) = read_numpy(path.to_str().unwrap())?;

    let (n_polygons, mut n_points, mut n_xy) = (
        shape[0] as u32,
        shape[1] as u32,
        shape[2] as u32
    );
    
    if n_xy != 2 && n_points != 2 {
        return Err(Error::new(
            ErrorKind::InvalidData, 
            "Invalid polygon array shape. First or second dimension must be 2."
        ));
    }

    let mut order = 0;
    if n_points == 2 {
        std::mem::swap(&mut n_points, &mut n_xy);
        order = 1;
    }

    let data: Vec<f64> = data.to_f64();
    let mut polygons = vec![];

    let mut idx = 0;
    for _ in 0..n_polygons {
        let mut polygon = vec![];
        if order == 0 {
            for j in 0..n_points {
                polygon.push([
                    data[idx + 2*j as usize].to_f64(),
                    data[idx + (2*j + 1) as usize].to_f64()
                ]);
            }
        } else { 
            for j in 0..n_points {
                let x = data[idx + j as usize].to_f64();
                let y = data[idx + (n_points + j) as usize].to_f64();
                polygon.push([x, y]);
            }
        }

        idx += n_points as usize * 2;

        polygons.push(polygon);
    }

    Ok(polygons)
}

/// Write polygons to a numpy file
///
/// # Arguments
///
/// * `path` - Path to the numpy file
///
/// # Examples
///
/// ```no_run
/// use std::path::Path;
/// use fqmv_core::utils::toy;
/// use fqmv_core::io::polygons::write_polygons_numpy;
/// let path = Path::new("data/polygons.npy");
/// let polygons = toy::polygons();
/// write_polygons_numpy(path, &polygons).unwrap();
/// ```
pub fn write_polygons_numpy<T>(path: &Path, polygons: &[Vec<[T; 2]>]) -> Result<(), Error> 
where
    T: Numeric + npyz::Serialize + npyz::AutoSerialize
{
    let mut data = Vec::new();
    for polygon in polygons {
        for xy in polygon {
            data.push(xy[0]);
            data.push(xy[1]);
        }
    }

    let shape = vec![
        polygons.len() as u64,
        polygons[0].len() as u64,
        2
    ];

    write_numpy(&path.to_str().unwrap(), data, shape)
}

/// Read polygons from a binary file
///
/// # Arguments
///
/// * `path` - Path to the binary file
///
/// # Examples
///
/// ```no_run
/// use std::path::Path;
/// use fqmv_core::io::polygons::read_polygons_binary;
/// let path = Path::new("data/polygons.bin");
/// let polygons = read_polygons_binary(path).unwrap();
/// ```
pub fn read_polygons_binary(path: &Path) -> Result<Vec<Vec<[f64; 2]>>, Error> {
    let file = File::open(path)?;
    let reader = BufReader::new(file);
    let data: Vec<Vec<[f64; 2]>> = bincode::deserialize_from(reader)
        .unwrap_or_else(|err| {
            panic!("Error reading polygon binary data: {:?}", err);
        });

    Ok(data)
}

/// Write polygons to a binary file
///
/// # Arguments
///
/// * `path` - Path to the binary file
/// * `polygons` - Vector of polygons
///
/// # Examples
///
/// ```no_run
/// use std::path::Path;
/// use fqmv_core::utils::toy;
/// use fqmv_core::io::polygons::write_polygons_binary;
/// let path = Path::new("data/polygons.bin");
/// let polygons = toy::polygons();
/// write_polygons_binary(path, &polygons).unwrap();
/// ```
pub fn write_polygons_binary<T>(path: &Path, polygons: &[Vec<[T; 2]>]) -> Result<(), Error> 
where
    T: Numeric + Serialize + Display + Debug
{
    let file = File::create(path)?;
    let writer = BufWriter::new(file);
    bincode::serialize_into(writer, polygons)
        .unwrap_or_else(|err| {
            panic!("Error writing polygon binary data: {:?}", err);
        });

    Ok(())
}

/// Read polygons from a file
///
/// # Arguments
///
/// * `path` - Path to the file
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::io::read_polygons;
/// let polygons = read_polygons("data/polygons.json").unwrap();
/// ```
pub fn read_polygons(path: &str) -> Result<Vec<Vec<[f64; 2]>>, Error> {
    let path = Path::new(path);
    if !path.exists() {
        return Err(Error::new(
            ErrorKind::NotFound,
            "File not found"
        ));
    }

    let ext = path.extension()
        .and_then(std::ffi::OsStr::to_str)
        .map(|s| s.to_ascii_lowercase())
        .ok_or_else(|| Error::new(
            ErrorKind::InvalidInput,
            "Invalid or missing file extension"
        ))?;

    match ext.as_str() {
        "json" => read_polygons_json(path),
        "npy" | "numpy" => read_polygons_numpy(path),
        "fqmv" | "bin" | "binary" => read_polygons_binary(path),
        _ => Err(Error::new(
            ErrorKind::InvalidData,
            "Unsupported file extension. Must be json, npy, fqmv, or bin."
        ))
    }
}

/// Write polygons to a file
///
/// # Arguments
///
/// * `path` - Path to the file
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::utils::toy;
/// use fqmv_core::io::write_polygons;
/// let polygons = toy::polygons();
/// write_polygons("data/polygons.json", &polygons).unwrap();
/// ```
pub fn write_polygons(path: &str, polygons: &[Vec<[f64; 2]>]) -> Result<(), Error> {
    let path = Path::new(path);
    let ext = path.extension()
        .and_then(std::ffi::OsStr::to_str)
        .map(|s| s.to_ascii_lowercase())
        .ok_or_else(|| Error::new(
            ErrorKind::InvalidInput,
            "Invalid or missing file extension"
        ))?;

    match ext.as_str() {
        "json" => write_polygons_json(path, polygons),
        "npy" | "numpy" => write_polygons_numpy(path, polygons),
        "fqmv" | "bin" | "binary" => write_polygons_binary(path, polygons),
        _ => Err(Error::new(
            ErrorKind::InvalidData,
            "Unsupported file extension. Must be json, npy, fqmv, or bin."
        ))
    }
}
