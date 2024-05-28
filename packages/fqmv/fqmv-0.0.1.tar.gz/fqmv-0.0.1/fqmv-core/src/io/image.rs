use std::path::Path;
use std::io::{Error, ErrorKind};
use image::{DynamicImage, Pixel, Luma, Rgb, Primitive, ImageBuffer, ImageError};

use crate::Numeric;
use crate::types::Image;
use crate::io::npy::{ArrayType, read_numpy, write_numpy};

/// Read an image from a numpy file
///
/// # Arguments
///
/// * `path` - Path to the numpy file
///
/// # Examples
///
/// ```no_run
/// use std::path::Path;
/// use fqmv_core::io::image::read_image_numpy;
/// let path = Path::new("data/image.npy");
/// let img = read_image_numpy(path).unwrap();
/// ```
pub fn read_image_numpy(path: &Path) -> Result<DynamicImage, ImageError> {
    fn npy_to_luma<S>(data: Vec<S>, width: u32, height: u32) -> Image<Luma<S>>
    where
        S: Numeric + Primitive,
        Luma<S>: Pixel<Subpixel = S>,
    {
        let mut img = ImageBuffer::new(width, height);
        let mut data = data.iter();
        for y in 0..height {
            for x in 0..width {
                img.put_pixel(x, y, Luma([*data.next().unwrap()]));
            }
        }

        img
    }

    fn npy_to_rgb<S>(data: Vec<S>, width: u32, height: u32) -> Image<Rgb<S>>
    where
        S: Numeric + Primitive,
        Rgb<S>: Pixel<Subpixel = S>,
    {
        let mut img = ImageBuffer::new(width, height);
        let mut data = data.iter();
        for y in 0..height {
            for x in 0..width {
                img.put_pixel(x, y, Rgb([
                    *data.next().unwrap(),
                    *data.next().unwrap(),
                    *data.next().unwrap()
                ]));
            }
        }

        img
    }

    let (data, shape) = read_numpy(path.to_str().expect("Path must be valid unicode string."))?;
    let (height, width) = (shape[0] as u32, shape[1] as u32);

    let size = data.len() as u32;
    let format = if size == height * width {
        "grayscale"
    } else if size == height * width * 3 {
        "rgb"
    } else {
        panic!("Invalid image shape. Numpy image must be grayscale or rgb");
    };

    let img = match format {
        "grayscale" => match data {
            ArrayType::U8(data) => { 
                DynamicImage::ImageLuma8(npy_to_luma(data, width, height)) 
            },
            ArrayType::U16(data) => { 
                DynamicImage::ImageLuma16(npy_to_luma(data, width, height)) 
            },
            ArrayType::I32(data) => { 
                let data = data.iter().map(|x| *x as u16).collect();
                DynamicImage::ImageLuma16(npy_to_luma(data, width, height)) 
            },
            ArrayType::I64(data) => { 
                let data = data.iter().map(|x| *x as u16).collect();
                DynamicImage::ImageLuma16(npy_to_luma(data, width, height)) 
            },
            ArrayType::F32(data) => { 
                let data = data.iter().map(|x| x.round() as u16).collect();
                DynamicImage::ImageLuma16(npy_to_luma(data, width, height)) 
            },
            ArrayType::F64(data) => { 
                let data = data.iter().map(|x| x.round() as u16).collect();
                DynamicImage::ImageLuma16(npy_to_luma(data, width, height)) 
            },
        },
        "rgb" => match data {
            ArrayType::U8(data) => {
                DynamicImage::ImageRgb8(npy_to_rgb(data, width, height))
            },
            ArrayType::U16(data) => { 
                DynamicImage::ImageRgb16(npy_to_rgb(data, width, height)) 
            },
            ArrayType::I32(data) => { 
                let data = data.iter().map(|x| *x as u16).collect();
                DynamicImage::ImageRgb16(npy_to_rgb(data, width, height)) 
            },
            ArrayType::I64(data) => { 
                let data = data.iter().map(|x| *x as u16).collect();
                DynamicImage::ImageRgb16(npy_to_rgb(data, width, height)) 
            },
            ArrayType::F32(data) => { 
                let data = data.iter().map(|x| x.round() as u16).collect();
                DynamicImage::ImageRgb16(npy_to_rgb(data, width, height)) 
            },
            ArrayType::F64(data) => { 
                let data = data.iter().map(|x| x.round() as u16).collect();
                DynamicImage::ImageRgb16(npy_to_rgb(data, width, height)) 
            },
        },
        _ => panic!("Unsupported image format")
    };

    Ok(img)
}

/// Write an image to a numpy file
///
/// # Arguments
///
/// * `path` - Path to the numpy file
/// * `data` - Image data
///
/// # Examples
///
/// ```no_run
/// use std::path::Path;
/// use image::DynamicImage;
/// use fqmv_core::io::image::write_image_numpy;
/// let path = Path::new("data/image.npy");
/// let img = DynamicImage::new_rgb8(512, 512);
/// write_image_numpy(path, img).unwrap();
/// ```
pub fn write_image_numpy(path: &Path, data: DynamicImage) -> Result<(), Error> {
    fn luma_to_npy<S>(img: &Image<Luma<S>>) -> Vec<S>
    where
        S: Numeric + Primitive,
        Luma<S>: Pixel<Subpixel = S>,
    {
        img.pixels().map(|p| p[0]).collect()
    }

    fn rgb_to_npy<S>(img: &Image<Rgb<S>>) -> Vec<S>
    where
        S: Numeric + Primitive,
        Rgb<S>: Pixel<Subpixel = S>,
    {
        let mut data = vec![];
        for p in img.pixels() {
            data.push(p[0]);
            data.push(p[1]);
            data.push(p[2]);
        }

        data
    }

    let path = path.to_str().expect("Path must be valid unicode string.");
    let mut shape = vec![data.height() as u64, data.width() as u64];

    match data {
        DynamicImage::ImageLuma8(img) => {
            let data = luma_to_npy(&img);
            write_numpy(path, data, shape)
        },
        DynamicImage::ImageLuma16(img) => {
            let data = luma_to_npy(&img);
            write_numpy(path, data, shape)
        },
        DynamicImage::ImageRgb8(img) => {
            let data = rgb_to_npy(&img);
            shape.push(3);
            write_numpy(path, data, shape)
        },
        DynamicImage::ImageRgb16(img) => {
            let data = rgb_to_npy(&img);
            shape.push(3);
            write_numpy(path, data, shape)
        },
        _ => panic!("Unsupported image type detected. Must be 8 or 16 bit luma or rgb")
    }
}

/// Read an image from a file
///
/// # Arguments
///
/// * `path` - Path to the image file
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::io::read_image;
/// let img = read_image("data/image.jpg").unwrap();
/// ```
pub fn read_image(path: &str) -> Result<DynamicImage, Error> {
    let path = Path::new(path);
    if !path.exists() {
        return Err(Error::new(
            ErrorKind::NotFound,
            format!("Path does not exist: {}", path.display())
        ));
    }

    let ext = path.extension()
        .and_then(|e| e.to_str())
        .map(|e| e.to_ascii_lowercase())
        .ok_or_else(|| Error::new(
            ErrorKind::InvalidInput,
            "Invalid or missing file extension"
        ))?;

    let img = match ext.as_str() {
        "jpeg" | "jpg" | "png" | "bmp" | 
        "tiff" | "tif" | "hdr" | "pbm" | 
        "avif" | "tga" | "qoi" | "exr" | 
        "webp" => image::open(path),
        "npy" | "numpy" => read_image_numpy(path),
        _ => return Err(Error::new(
            ErrorKind::InvalidInput,
            format!("Unsupported image format: {}", ext)
        ))
    };

    img.map_err(|e| Error::new(
        ErrorKind::Other,
        format!("Could not open image: {}", e)
    ))
}

/// Write an image to a file
///
/// # Arguments
///
/// * `path` - Path to the image file
/// * `img` - Image data
///
/// # Examples
///
/// ```no_run
/// use image::DynamicImage;
/// use fqmv_core::io::write_image;
/// let img = DynamicImage::new_rgb8(512, 512);
/// write_image("data/image.jpg", img).unwrap();
/// ```
pub fn write_image(path: &str, img: DynamicImage) -> Result<(), String> {
    let path = Path::new(path);
    let ext = path.extension()
        .and_then(std::ffi::OsStr::to_str)
        .map(|s| s.to_ascii_lowercase())
        .ok_or_else(|| "Failed to extract or convert the file extension".to_string())?;

    match ext.as_str() {
        "jpeg" | "jpg" | "png" | "bmp" |
        "tiff" | "tif" | "hdr" | "pbm" |
        "avif" | "tga" | "qoi" | "exr" |
        "webp" => img.save(path).map_err(|e| format!("Could not save image: {}", e)),
        "npy" | "numpy" => write_image_numpy(path, img).map_err(|e| 
            format!("Could not save image as numpy: {}", e)
        ),
        _ => Err(format!("Unsupported image format: {}", ext))
    }
}
