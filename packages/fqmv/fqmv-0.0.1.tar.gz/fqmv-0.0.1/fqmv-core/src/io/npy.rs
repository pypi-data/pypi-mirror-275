use std::io::{Error, ErrorKind};
use npyz::{self, NpyFile, DType, TypeChar, WriterBuilder};

use crate::Numeric;

/// A wrapper around the currently accepted numpy array types
pub enum ArrayType {
    U8(Vec<u8>),
    U16(Vec<u16>),
    I32(Vec<i32>),
    I64(Vec<i64>),
    F32(Vec<f32>),
    F64(Vec<f64>),
}

impl ArrayType {
    pub fn new<T: Numeric>(data: Vec<T>) -> Self {
        match T::dtype() {
            "u8" => ArrayType::U8(data.iter().map(|x| x.to_u8()).collect()),
            "u16" => ArrayType::U16(data.iter().map(|x| x.to_u16()).collect()),
            "i32" => ArrayType::I32(data.iter().map(|x| x.to_i32()).collect()),
            "i64" => ArrayType::I64(data.iter().map(|x| x.to_i64()).collect()),
            "f32" => ArrayType::F32(data.iter().map(|x| x.to_f32()).collect()),
            "f64" => ArrayType::F64(data.iter().map(|x| x.to_f64()).collect()),
            _ => panic!("Unsupported data type"),
        }
    }

    pub fn len(&self) -> usize {
        match self {
            ArrayType::U8(x) => x.len(),
            ArrayType::U16(x) => x.len(),
            ArrayType::I32(x) => x.len(),
            ArrayType::I64(x) => x.len(),
            ArrayType::F32(x) => x.len(),
            ArrayType::F64(x) => x.len(),
        }
    }

    pub fn to_u8(&self) -> Vec<u8> {
        match self {
            ArrayType::U8(x) => x.clone(),
            ArrayType::U16(x) => x.iter().map(|x| *x as u8).collect(),
            ArrayType::I32(x) => x.iter().map(|x| *x as u8).collect(),
            ArrayType::I64(x) => x.iter().map(|x| *x as u8).collect(),
            ArrayType::F32(x) => x.iter().map(|x| x.round() as u8).collect(),
            ArrayType::F64(x) => x.iter().map(|x| x.round() as u8).collect(),
        }
    }

    pub fn to_u16(&self) -> Vec<u16> {
        match self {
            ArrayType::U8(x) => x.iter().map(|x| *x as u16).collect(),
            ArrayType::U16(x) => x.clone(),
            ArrayType::I32(x) => x.iter().map(|x| *x as u16).collect(),
            ArrayType::I64(x) => x.iter().map(|x| *x as u16).collect(),
            ArrayType::F32(x) => x.iter().map(|x| x.round() as u16).collect(),
            ArrayType::F64(x) => x.iter().map(|x| x.round() as u16).collect(),
        }
    }

    pub fn to_i32(&self) -> Vec<i32> {
        match self {
            ArrayType::U8(x) => x.iter().map(|x| *x as i32).collect(),
            ArrayType::U16(x) => x.iter().map(|x| *x as i32).collect(),
            ArrayType::I32(x) => x.clone(),
            ArrayType::I64(x) => x.iter().map(|x| *x as i32).collect(),
            ArrayType::F32(x) => x.iter().map(|x| x.round() as i32).collect(),
            ArrayType::F64(x) => x.iter().map(|x| x.round() as i32).collect(),
        }
    }

    pub fn to_i64(&self) -> Vec<i64> {
        match self {
            ArrayType::U8(x) => x.iter().map(|x| *x as i64).collect(),
            ArrayType::U16(x) => x.iter().map(|x| *x as i64).collect(),
            ArrayType::I32(x) => x.iter().map(|x| *x as i64).collect(),
            ArrayType::I64(x) => x.clone(),
            ArrayType::F32(x) => x.iter().map(|x| x.round() as i64).collect(),
            ArrayType::F64(x) => x.iter().map(|x| x.round() as i64).collect(),
        }
    }

    pub fn to_f32(&self) -> Vec<f32> {
        match self {
            ArrayType::U8(x) => x.iter().map(|x| *x as f32).collect(),
            ArrayType::U16(x) => x.iter().map(|x| *x as f32).collect(),
            ArrayType::I32(x) => x.iter().map(|x| *x as f32).collect(),
            ArrayType::I64(x) => x.iter().map(|x| *x as f32).collect(),
            ArrayType::F32(x) => x.clone(),
            ArrayType::F64(x) => x.iter().map(|x| *x as f32).collect(),
        }
    }

    pub fn to_f64(&self) -> Vec<f64> {
        match self {
            ArrayType::U8(x) => x.iter().map(|x| *x as f64).collect(),
            ArrayType::U16(x) => x.iter().map(|x| *x as f64).collect(),
            ArrayType::I32(x) => x.iter().map(|x| *x as f64).collect(),
            ArrayType::I64(x) => x.iter().map(|x| *x as f64).collect(),
            ArrayType::F32(x) => x.iter().map(|x| *x as f64).collect(),
            ArrayType::F64(x) => x.clone(),
        }
    }

    pub fn to_numeric<T: Numeric>(&self) -> Vec<T> {
        match T::dtype() {
            "u8" => self.to_u8().iter().map(|x| T::from_u8(*x)).collect(),
            "u16" => self.to_u16().iter().map(|x| T::from_u16(*x)).collect(),
            "i32" => self.to_i32().iter().map(|x| T::from_i32(*x)).collect(),
            "i64" => self.to_i64().iter().map(|x| T::from_i64(*x)).collect(),
            "f32" => self.to_f32().iter().map(|x| T::from_f32(*x)).collect(),
            "f64" => self.to_f64().iter().map(|x| T::from_f64(*x)).collect(),
            _ => panic!("Unsupported data type"),
        }
    }
}

/// Read a numpy file
///
/// # Arguments
///
/// * `path` - Path to the numpy file
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::io::npy::read_numpy;
/// let (data, shape) = read_numpy("data/data.npy").unwrap();
/// ```
pub fn read_numpy(path: &str) -> Result<(ArrayType, Vec<u64>), Error> {
    let bytes = std::fs::read(path)?;
    let npy = NpyFile::new(&bytes[..])?;
    let shape = npy.shape().to_vec();
    
    let npy_data = match npy.dtype() {
        DType::Plain(x) => match (x.type_char(), x.size_field()) {
            (TypeChar::Uint, 1) => ArrayType::U8(npy.into_vec()?),
            (TypeChar::Uint, 2) => ArrayType::U16(npy.into_vec()?),
            (TypeChar::Int, 4) => ArrayType::I32(npy.into_vec()?),
            (TypeChar::Int, 8) => ArrayType::I64(npy.into_vec()?),
            (TypeChar::Float, 4) => ArrayType::F32(npy.into_vec()?),
            (TypeChar::Float, 8) => ArrayType::F64(npy.into_vec()?),
            _ => return Err(Error::new(ErrorKind::Other, "Unsupported numpy data type")),
        },
        _ => return Err(Error::new(ErrorKind::Other, "Only plain numpy arrays are supported")),
    };

    Ok((npy_data, shape))
}

/// Write a numpy file
///
/// # Arguments
///
/// * `path` - Path to the numpy file
/// * `data` - Data to write
/// * `shape` - Shape of the data
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::io::npy::write_numpy;
/// let data = vec![1, 2, 3, 4, 5];
/// let shape = vec![5, 0];
/// write_numpy("data/data.npy", data, shape).unwrap();
/// ```
pub fn write_numpy<T>(path: &str, data: Vec<T>, shape: Vec<u64>) -> Result<(), std::io::Error> 
where
    T: Numeric + npyz::Serialize + npyz::AutoSerialize
{
    let mut buffer = vec![];
    let mut writer = npyz::WriteOptions::<T>::new()
            .default_dtype()
            .shape(&shape)
            .writer(&mut buffer)
            .begin_nd()?; 

    for d in data {
        let _ = writer.push(&d);
    }

    writer.finish()?;
    std::fs::write(path, buffer)?;
    Ok(())
}
