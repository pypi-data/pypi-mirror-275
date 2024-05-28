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

/// Read labels from a json file
///
/// # Arguments
///
/// * `path` - Path to the json file
///
/// # Examples
///
/// ```no_run
/// use std::path::Path;
/// use fqmv_core::io::labels::read_labels_json;
/// let path = Path::new("data/labels.json");
/// let labels = read_labels_json::<u16>(path).unwrap();
/// ```
pub fn read_labels_json<T: Numeric>(path: &Path) -> Result<Vec<T>, Error> {
    let mut file = File::open(path)?;
    let mut contents = String::new();
    file.read_to_string(&mut contents)?;

    let data: Value = serde_json::from_str(&contents)?;

    let valid_keys = vec![
        "labels",
        "label",
    ];

    for key in valid_keys {
        if let Some(vec) = data.get(key) {
            let vec = vec.as_array().ok_or(Error::new(
                ErrorKind::InvalidData,
                "Invalid vector array format",
            ))?;

            let vec = vec.iter()
                .filter_map(Value::as_f64)
                .map(T::from_f64)
                .collect::<Vec<T>>();

            return Ok(vec);
        }
    }
    
    Err(Error::new(
        std::io::ErrorKind::InvalidData,
        "Key not found in vector json data",
    ))
}

/// Write labels to a json file
///
/// # Arguments
///
/// * `path` - Path to the json file
/// * `labels` - Vector of labels
///
/// # Examples
///
/// ```no_run
/// use std::path::Path;
/// use fqmv_core::io::labels::write_labels_json;
/// let path = Path::new("data/labels.json");
/// let labels = vec![1, 2, 3, 4, 5];
/// write_labels_json(path, &labels).unwrap();
/// ```
pub fn write_labels_json<T>(path: &Path, labels: &[T]) -> Result<(), Error> 
where
    T: Serialize + Display + Debug
{
    let file = File::create(path)?;
    let mut writer = BufWriter::new(file);
    let mut map = HashMap::new();
    map.insert("labels", labels);
    serde_json::to_writer(&mut writer, &map)?;
    writer.flush()
}

/// Read labels from a numpy file
///
/// # Arguments
///
/// * `path` - Path to the numpy file
///
/// # Examples
///
/// ```no_run
/// use std::path::Path;
/// use fqmv_core::io::labels::read_labels_numpy;
/// let path = Path::new("data/labels.npy");
/// let labels = read_labels_numpy::<u16>(path).unwrap();
/// ```
pub fn read_labels_numpy<T: Numeric>(path: &Path) -> Result<Vec<T>, Error> {
    let (data, _) = read_numpy(path.to_str().unwrap())?;
    Ok(data.to_numeric())
}

/// Write labels to a numpy file
///
/// # Arguments
///
/// * `path` - Path to the numpy file
/// * `labels` - Vector of labels
///
/// # Examples
///
/// ```no_run
/// use std::path::Path;
/// use fqmv_core::io::labels::write_labels_numpy;
/// let path = Path::new("data/labels.npy");
/// let labels = vec![1, 2, 3, 4, 5];
/// write_labels_numpy(path, &labels).unwrap();
/// ```
pub fn write_labels_numpy<T>(path: &Path, labels: &[T]) -> Result<(), Error> 
where
    T: Numeric + npyz::Serialize + npyz::AutoSerialize
{
    let shape = vec![labels.len() as u64];
    write_numpy(&path.to_str().unwrap(), labels.to_vec(), shape)
}

/// Read labels from a binary file
///
/// # Arguments
///
/// * `path` - Path to the binary file
///
/// # Examples
///
/// ```no_run
/// use std::path::Path;
/// use fqmv_core::io::labels::read_labels_binary;
/// let path = Path::new("data/labels.bin");
/// let labels = read_labels_binary::<u16>(path).unwrap();
/// ```
pub fn read_labels_binary<T>(path: &Path) -> Result<Vec<T>, Error> 
where 
    T: Numeric + serde::de::DeserializeOwned,
{
    let file = File::open(path)?;
    let reader = BufReader::new(file);
    let data: Vec<T> = bincode::deserialize_from(reader)
        .unwrap_or_else(|err| {
            panic!("Error reading vector binary data: {:?}", err);
        });

    Ok(data)
}

/// Write labels to a binary file
///
/// # Arguments
///
/// * `path` - Path to the binary file
/// * `labels` - Vector of labels
///
/// # Examples
///
/// ```no_run
/// use std::path::Path;
/// use fqmv_core::io::labels::write_labels_binary;
/// let path = Path::new("data/labels.bin");
/// let labels = vec![1, 2, 3, 4, 5];
/// write_labels_binary(path, &labels).unwrap();
/// ```
pub fn write_labels_binary<T>(path: &Path, vector: &[T]) -> Result<(), Error> 
where
    T: Numeric + Serialize + Display + Debug
{
    let file = File::create(path)?;
    let writer = BufWriter::new(file);
    bincode::serialize_into(writer, vector)
        .unwrap_or_else(|err| {
            panic!("Error writing vector binary data: {:?}", err);
        });

    Ok(())
}

/// Read labels from a file
///
/// # Arguments
///
/// * `path` - Path to the file
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::io::read_labels;
/// let labels = read_labels("data/labels.json").unwrap();
/// ```
pub fn read_labels(path: &str) -> Result<Vec<u16>, Error> {
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
        "json" => read_labels_json(path),
        "npy" => read_labels_numpy(path),
        "fqmv" | "bin" | "binary" => read_labels_binary(path),
        _ => Err(Error::new(
            ErrorKind::InvalidData,
            "Invalid file extension. Only json, npy, bin, or fqmv are supported."
        )),
    }
}

/// Write labels to a file
///
/// # Arguments
///
/// * `path` - Path to the file
/// * `labels` - Vector of labels
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::io::write_labels;
/// let labels = vec![1, 2, 3, 4, 5];
/// write_labels("data/labels.json", &labels).unwrap();
/// ```
pub fn write_labels(path: &str, labels: &[u16]) -> Result<(), Error> {
    let path = Path::new(path);
    let ext = path.extension()
        .and_then(std::ffi::OsStr::to_str)
        .map(|s| s.to_ascii_lowercase())
        .ok_or_else(|| Error::new(
            ErrorKind::InvalidData,
            "Invalid or missing file extension"
        ))?;

    match ext.as_str() {
        "json" => write_labels_json(path, labels),
        "npy" | "numpy" => write_labels_numpy(path, labels),
        "fqmv" | "bin" | "binary" => write_labels_binary(path, labels),
        _ => Err(Error::new(
            ErrorKind::InvalidData,
            "Invalid file extension. Only json, npy, bin, or fqmv are supported."
        )),
    }
}
