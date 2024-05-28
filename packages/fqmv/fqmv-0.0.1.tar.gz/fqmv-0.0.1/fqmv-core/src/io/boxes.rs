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

/// Read bounding boxes from a json file
///
/// # Arguments
///
/// * `path` - Path to the json file
///
/// # Examples
///
/// ```no_run
/// use std::path::Path;
/// use fqmv_core::io::boxes::read_boxes_json;
/// let path = Path::new("data/bounding_boxes.json");
/// let boxes = read_boxes_json(path).unwrap();
/// ```
pub fn read_boxes_json(path: &Path) -> Result<Vec<Vec<f64>>, Error> {
    let mut file = File::open(path)?;
    let mut contents = String::new();
    file.read_to_string(&mut contents)?;

    let data: Value = serde_json::from_str(&contents)?;

    let valid_keys = vec![
        "bounding_boxes",
        "bounding_box",
        "boxes",
        "box",
        "xyxy",
    ];

    for key in valid_keys {
        if let Some(boxes) = data.get(key) {
            let boxes = boxes.as_array().ok_or(Error::new(
                ErrorKind::InvalidData,
                "Invalid bounding box array format",
            ))?;

            let boxes = boxes.iter()
                .filter_map(Value::as_array)
                .map(|b| {
                    b.iter()
                        .filter_map(Value::as_f64)
                        .collect::<Vec<f64>>()
                })
                .collect::<Vec<Vec<f64>>>();

            return Ok(boxes);
        }
    }
    
    Err(Error::new(
        std::io::ErrorKind::InvalidData,
        "Key not found in bounding boxes json data",
    ))
}

/// Write bounding boxes to a json file
///
/// # Arguments
///
/// * `path` - Path to the json file
/// * `boxes` - Vector of bounding boxes
///
/// # Examples
///
/// ```no_run
/// use std::path::Path;
/// use fqmv_core::io::boxes::write_boxes_json;
/// let path = Path::new("data/bounding_boxes.json");
/// let boxes = vec![
///     vec![0.0, 0.0, 1.0, 1.0],
///     vec![0.1, 0.1, 0.9, 0.9],
/// ];
/// write_boxes_json(path, &boxes).unwrap();
/// ```
pub fn write_boxes_json<T>(path: &Path, boxes: &[Vec<T>]) -> Result<(), Error> 
where
    T: Serialize + Display + Debug
{
    let file = File::create(path)?;
    let mut writer = BufWriter::new(file);
    let mut map = HashMap::new();
    map.insert("bounding_boxes", boxes);
    serde_json::to_writer(&mut writer, &map)?;
    writer.flush()
}

/// Read bounding boxes from a numpy file
///
/// # Arguments
///
/// * `path` - Path to the numpy file
///
/// # Examples
///
/// ```no_run
/// use std::path::Path;
/// use fqmv_core::io::boxes::read_boxes_numpy;
/// let path = Path::new("data/bounding_boxes.npy");
/// let boxes = read_boxes_numpy(path).unwrap();
/// ```
pub fn read_boxes_numpy(path: &Path) -> Result<Vec<Vec<f64>>, Error> {
    let (data, shape) = read_numpy(path.to_str().unwrap())?;

    let n_points = shape.get(1).ok_or(Error::new(
        ErrorKind::InvalidData,
        "Invalid bounding box array shape. Must be (n, 4)."
    ))?;

    if *n_points != 4 {
        return Err(Error::new(
            ErrorKind::InvalidData, 
            "Invalid bounding box array shape. Must be (n, 4)."
        ));
    }

    let boxes: Vec<f64> = data.to_f64();

    Ok(boxes.chunks(4).map(Vec::from).collect())
}

/// Write bounding boxes to a numpy file
///
/// # Arguments
///
/// * `path` - Path to the numpy file
/// * `boxes` - Vector of bounding boxes
///
/// # Examples
///
/// ```no_run
/// use std::path::Path;
/// use fqmv_core::io::boxes::write_boxes_numpy;
/// let path = Path::new("data/bounding_boxes.npy");
/// let boxes = vec![
///     vec![0.0, 0.0, 1.0, 1.0],
///     vec![0.1, 0.1, 0.9, 0.9],
/// ];
/// write_boxes_numpy(path, &boxes).unwrap();
/// ```
pub fn write_boxes_numpy<T>(path: &Path, boxes: &[Vec<T>]) -> Result<(), Error> 
where
    T: Numeric + npyz::Serialize + npyz::AutoSerialize
{
    let mut data = Vec::new();
    for box_ in boxes {
        data.push(box_[0]);
        data.push(box_[1]);
        data.push(box_[2]);
        data.push(box_[3]);
    }

    if boxes[0].len() != 4 {
        return Err(Error::new(
            ErrorKind::InvalidData,
            "Invalid bounding box array shape. Must be (n, 4)."
        ));
    }

    let shape = vec![boxes.len() as u64, 4];
    write_numpy(&path.to_str().unwrap(), data, shape)
}

/// Read bounding boxes from a binary file
///
/// # Arguments
///
/// * `path` - Path to the binary file
///
/// # Examples
///
/// ```no_run
/// use std::path::Path;
/// use fqmv_core::io::boxes::read_boxes_binary;
/// let path = Path::new("data/bounding_boxes.bin");
/// let boxes = read_boxes_binary(path).unwrap();
/// ```
pub fn read_boxes_binary(path: &Path) -> Result<Vec<Vec<f64>>, Error> {
    let file = File::open(path)?;
    let reader = BufReader::new(file);
    let data: Vec<Vec<f64>> = bincode::deserialize_from(reader)
        .unwrap_or_else(|err| {
            panic!("Error reading bounding box binary data: {:?}", err);
        });

    Ok(data)
}

/// Write bounding boxes to a binary file
///
/// # Arguments
///
/// * `path` - Path to the binary file
/// * `boxes` - Vector of bounding boxes
///
/// # Examples
///
/// ```no_run
/// use std::path::Path;
/// use fqmv_core::io::boxes::write_boxes_binary;
/// let path = Path::new("data/bounding_boxes.bin");
/// let boxes = vec![
///     vec![0.0, 0.0, 1.0, 1.0],
///     vec![0.1, 0.1, 0.9, 0.9],
/// ];
/// write_boxes_binary(path, &boxes).unwrap();
/// ```
pub fn write_boxes_binary<T>(path: &Path, boxes: &[Vec<T>]) -> Result<(), Error> 
where
    T: Numeric + Serialize + Display + Debug
{
    let file = File::create(path)?;
    let writer = BufWriter::new(file);
    bincode::serialize_into(writer, boxes)
        .unwrap_or_else(|err| {
            panic!("Error writing bounding box binary data: {:?}", err);
        });

    Ok(())
}

/// Read bounding boxes from a file
///
/// # Arguments
///
/// * `path` - Path to the bounding box file
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::io::read_boxes;
/// let boxes = read_boxes("data/bounding_boxes.json").unwrap();
/// ```
pub fn read_boxes(path: &str) -> Result<Vec<Vec<f64>>, Error> {
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
            ErrorKind::InvalidData,
            "Invalid or missing file extension"
        ))?;

    match ext.as_str() {
        "json" => read_boxes_json(path),
        "npy" => read_boxes_numpy(path),
        "bin" => read_boxes_binary(path),
        _ => Err(Error::new(
            ErrorKind::InvalidData,
            "Invalid bounding box file format"
        ))
    }
}

/// Write bounding boxes to a file
///
/// # Arguments
///
/// * `path` - Path to the bounding box file
/// * `boxes` - Vector of bounding boxes
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::io::write_boxes;
/// let boxes = vec![
///     vec![0.0, 0.0, 1.0, 1.0],
///     vec![0.1, 0.1, 0.9, 0.9],
/// ];
/// write_boxes("data/bounding_boxes.json", &boxes).unwrap();
/// ```
pub fn write_boxes<T>(path: &str, boxes: &[Vec<T>]) -> Result<(), Error> 
where
    T: npyz::Serialize + npyz::AutoSerialize,
    T: Numeric + Serialize + Display + Debug
{
    let path = Path::new(path);
    let ext = path.extension()
        .and_then(std::ffi::OsStr::to_str)
        .map(|s| s.to_ascii_lowercase())
        .ok_or_else(|| Error::new(
            ErrorKind::InvalidData,
            "Invalid or missing file extension"
        ))?;

    match ext.as_str() {
        "json" => write_boxes_json(path, boxes),
        "npy" => write_boxes_numpy(path, boxes),
        "bin" => write_boxes_binary(path, boxes),
        _ => Err(Error::new(
            ErrorKind::InvalidData,
            "Invalid bounding box file format"
        ))
    }
}
