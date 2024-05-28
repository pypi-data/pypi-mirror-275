use std::cmp::Ordering;
use image::imageops::FilterType;
use image::{GenericImage, Pixel, Luma, Rgb, ImageBuffer, DynamicImage};

use crate::Numeric;
use crate::types::Image;

/// Resize an image to a new width and height using a specified filter
///
/// # Arguments
///
/// * `image` - A reference to the image to be resized
/// * `width` - The new width of the image
/// * `height` - The new height of the image
/// * `filter` - The filter type to use for resizing
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::utils::toy;
/// use fqmv_core::process::transform::resize;
///
/// let img = toy::rgb_image();
///
/// let resized = resize(&img, 2, 2, "nearest");
/// ```
pub fn resize<I, P>(image: &I, width: u32, height: u32, filter: &str) -> Image<P> 
where
    I: GenericImage<Pixel = P>,
    P: Pixel + 'static,
{
    let filter = match filter {
        "linear"   => FilterType::Triangle,
        "nearest"  => FilterType::Nearest,
        "cubic"    => FilterType::CatmullRom,
        "gaussian" => FilterType::Gaussian,
        "lanczos"  => FilterType::Lanczos3,
        _ => panic!(
            "Invalid filter type. Must be one of:
             linear, nearest, cubic, gaussian, lanczos"
        ),
    };

    image::imageops::resize(image, width, height, filter)
}

/// Crop an image to a new width and height
///
/// # Arguments
///
/// * `image` - A reference to the image to be cropped
/// * `x` - The x-coordinate of the top-left corner of the crop
/// * `y` - The y-coordinate of the top-left corner of the crop
/// * `width` - The width of the crop
/// * `height` - The height of the crop
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::utils::toy;
/// use fqmv_core::process::transform::crop;
///
/// let mut img = toy::rgb_image();
///
/// let cropped = crop(&mut img, 1, 1, 2, 2);
/// ```
pub fn crop<I, P>(image: &mut I, x: u32, y: u32, width: u32, height: u32) -> Image<P> 
where
    I: GenericImage<Pixel = P> + 'static,
    P: Pixel + 'static,
{
    image::imageops::crop(image, x, y, width, height).to_image()
}

/// Crop an image to a region defined by a bounding box
///
/// # Arguments
///
/// * `image` - A reference to the image to be cropped
/// * `bounding_box` - Bounding box coordinates (min_x, min_y, max_x, max_y)
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::utils::toy;
/// use fqmv_core::process::transform::crop_box;
///
/// let mut img = toy::rgb_image();
///
/// let cropped = crop_box(&mut img, &vec![1.0, 1.0, 2.0, 2.0]);
/// ```
pub fn crop_box<I, P, T>(image: &mut I, bounding_box: &[T]) -> Image<P> 
where
    I: GenericImage<Pixel = P> + 'static,
    P: Pixel + 'static,
    T: Numeric
{
    if bounding_box.len() != 4 {
        panic!("Bounding box must have 4 elements");
    }

    let (width, height) = image.dimensions();

    let min_x = match bounding_box[0].cmp(T::zero()) {
        Ordering::Less => 0_u32,
        _ => bounding_box[0].to_u32(),
    };

    let min_y = match bounding_box[1].cmp(T::zero()) {
        Ordering::Less => 0_u32,
        _ => bounding_box[1].to_u32(),
    };

    let max_x = match bounding_box[2].cmp(T::from_u32(width)) {
        Ordering::Greater => width,
        _ => bounding_box[2].to_u32(),
    };

    let max_y = match bounding_box[3].cmp(T::from_u32(height)) {
        Ordering::Greater => height,
        _ => bounding_box[3].to_u32(),
    };

    let width = max_x - min_x + 1;
    let height = max_y - min_y + 1;

    if width == 0 || height == 0 {
        panic!("Bounding box must have width/height greater than 0");
    }

    crop(image, min_x, min_y, width, height)
}

/// Center a binary mask within an image
///
/// # Arguments
///
/// * `image` - A reference to the image to be centered
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::utils::toy;
/// use fqmv_core::process::transform::center_mask;
/// let img = toy::gray_image();
/// let centered = center_mask(&img);
/// ```
pub fn center_mask(image: &Image<Luma<u8>>) -> Image<Luma<u8>> {
    let (width, height) = image.dimensions();
    let mut total_mass = 0.0;
    let (mut x_sum, mut y_sum) = (0.0, 0.0);

    for (x, y, pixel) in image.enumerate_pixels() {
        let intensity = pixel[0] as f32;
        total_mass += intensity;
        x_sum += x as f32 * intensity;
        y_sum += y as f32 * intensity;
    }

    let x_center = x_sum / total_mass;
    let y_center = y_sum / total_mass;

    let mut centered_image = Image::new(width, height);

    let x_shift = (width as f32 / 2.0 - x_center).round() as i32;
    let y_shift = (height as f32 / 2.0 - y_center).round() as i32;

    for (x, y, pixel) in image.enumerate_pixels() {
        let new_x = (x as i32 + x_shift).rem_euclid(width as i32) as u32;
        let new_y = (y as i32 + y_shift).rem_euclid(height as i32) as u32;
        centered_image.put_pixel(new_x, new_y, *pixel);
    }

    centered_image
}

/// Convert a vector of images with identical type to grayscale
///
/// # Arguments
///
/// * `images` - A reference to a vector of images to be converted
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::utils::toy;
/// use fqmv_core::process::transform::convert_to_gray;
///
/// let images = vec![toy::rgb_image(), toy::rgb_image()];
/// let gray_images = convert_to_gray(&images);
/// ```
pub fn convert_to_gray<P>(images: &Vec<Image<P>>) -> Vec<Image<Luma<u8>>> 
where
    P: Pixel<Subpixel = u8> + 'static,
    <P as Pixel>::Subpixel: 'static + From<u8>,
{
    match P::CHANNEL_COUNT {
        1 => {
            images.iter().map(|object| {
                let buffer: Image<Luma<u8>> = ImageBuffer::from_raw(
                    object.width(),
                    object.height(),
                    object.to_vec()
                ).unwrap();

                buffer
            }).collect()
        },
        3 => {
            images.iter().map(|object| {
                let buffer: Image<Rgb<u8>> = ImageBuffer::from_raw(
                    object.width(),
                    object.height(),
                    object.to_vec()
                ).unwrap();

                DynamicImage::ImageRgb8(buffer).into_luma8()
            }).collect()
        },
        _ => {
            panic!("Unsupported number of channels");
        }
    }
}
