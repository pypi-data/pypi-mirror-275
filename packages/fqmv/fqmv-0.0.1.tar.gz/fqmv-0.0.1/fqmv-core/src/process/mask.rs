use std::cmp::Ordering;
use imageproc::point::Point;
use imageproc::drawing::draw_polygon_mut;
use image::{GenericImage, ImageBuffer, Luma, Pixel, Primitive};

use crate::types::{Image, Mask};

/// Apply a mask to an image using an ordering against zero mask values
///
/// # Arguments
///
/// * `image` - A reference to the image to be masked
/// * `mask` - A reference to the mask to be applied
/// * `order` - The ordering to use against zero mask values
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::utils::toy;
/// use fqmv_core::process::mask::mask_image;
///
/// let img = toy::rgb_image();
/// let mask = toy::mask();
///
/// let masked = mask_image(&img, &mask, std::cmp::Ordering::Equal);
/// ```
pub fn mask_image<I, P>(image: &I, mask: &Mask, order: Ordering) -> Image<P> 
where
    I: GenericImage<Pixel = P>,
    P: Pixel + 'static,
    <P as Pixel>::Subpixel: 'static + From<u8>,
{
    let (width, height) = image.dimensions();
    let mut out = ImageBuffer::new(width, height);

    for x in 0..width {
        for y in 0..height {
            let blank = mask.get_pixel(x, y).0[0];
            let pixel = image.get_pixel(x, y);

            out.put_pixel(x, y, pixel);
            if blank.cmp(&0) == order {
                for channel in out.get_pixel_mut(x, y).channels_mut() {
                    *channel = <P as Pixel>::Subpixel::from(0);
                }
            }
        }
    }

    out
}

/// Mask the background of an image using a mask
///
/// # Arguments
///
/// * `image` - A reference to the image to be masked
/// * `mask` - A reference to the mask to be applied
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::utils::toy;
/// use fqmv_core::process::mask::mask_background;
///
/// let mut img = toy::rgb_image();
/// let mut mask = toy::mask();
///
/// let masked = mask_background(&img, &mask);
/// ```
pub fn mask_background<I, P>(image: &I, mask: &Mask) -> Image<P> 
where
    I: GenericImage<Pixel = P>,
    P: Pixel + 'static,
    <P as Pixel>::Subpixel: 'static + From<u8>,
{
    mask_image(image, mask, Ordering::Equal)
}

/// Mask the foreground of an image using a mask
///
/// # Arguments
///
/// * `image` - A reference to the image to be masked
/// * `mask` - A reference to the mask to be applied
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::utils::toy;
/// use fqmv_core::process::mask::mask_foreground;
///
/// let img = toy::rgb_image();
/// let mask = toy::mask();
///
/// let masked = mask_foreground(&img, &mask);
/// ```
pub fn mask_foreground<I, P>(image: &I, mask: &Mask) -> Image<P> 
where
    I: GenericImage<Pixel = P>,
    P: Pixel + 'static,
    <P as Pixel>::Subpixel: 'static + From<u8>,
{
    mask_image(image, mask, Ordering::Greater)
}

/// Convert a mask to a binary mask
///
/// # Arguments
///
/// * `mask` - A reference to the mask to be converted
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::utils::toy;
/// use fqmv_core::process::mask::binary_mask;
///
/// let mask = toy::mask();
///
/// let binary_mask = binary_mask::<u16>(&mask);
/// ```
pub fn binary_mask<R>(mask: &Mask) -> Image<Luma<R>> 
where
    R: Primitive + 'static,
{
    let (width, height) = mask.dimensions();
    let mut out = ImageBuffer::new(width, height);

    for x in 0..width {
        for y in 0..height {
            let pixel = mask.get_pixel(x, y);
            if pixel[0] > 0 {
                out.put_pixel(x, y, Luma([R::from(1).unwrap()]));
            } else {
                out.put_pixel(x, y, Luma([R::from(0).unwrap()]));
            }
        }
    }

    out
}

/// Convert a batch of masks to binary masks
///
/// # Arguments
///
/// * `masks` - A reference to the masks to be converted
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::utils::toy;
/// use fqmv_core::process::mask::batch_binary_mask;
///
/// let masks = vec![toy::mask(), toy::mask()];
/// let binary_masks = batch_binary_mask::<u16>(&masks);
/// ```
pub fn batch_binary_mask<R>(masks: &Vec<Mask>) -> Vec<Image<Luma<R>>>
where
    R: Primitive + 'static,
{
    masks.iter()
        .map(|mask| binary_mask::<R>(mask))
        .collect()
}

/// Generate a binary mask for a specific object label in a mask
///
/// # Arguments
///
/// * `mask` - A reference to the mask to be converted
/// * `object_id` - The object label to isolate within the mask
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::utils::toy;
/// use fqmv_core::process::mask::binary_object;
///
/// let mask = toy::mask();
///
/// let binary_object = binary_object::<u16>(&mask, 1);
/// ```
pub fn binary_object<R>(mask: &Mask, object_id: u16) -> Image<Luma<R>> 
where
    R: Primitive + 'static,
{
    let (width, height) = mask.dimensions();
    let mut out = ImageBuffer::new(width, height);

    for x in 0..width {
        for y in 0..height {
            let pixel = mask.get_pixel(x, y);
            if pixel[0] == object_id {
                out.put_pixel(x, y, Luma([R::from(1).unwrap()]));
            } else {
                out.put_pixel(x, y, Luma([R::from(0).unwrap()]));
            }
        }
    }

    out
}

/// Count the number of unique labels in a mask
///
/// # Arguments
///
/// * `mask` - A reference to the mask to be processed
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::utils::toy;
/// use fqmv_core::process::mask::count_labels;
///
/// let mask = toy::mask();
///
/// let (labels, n_labels, is_binary) = count_labels(&mask);
/// ```
pub fn count_labels(mask: &Mask) -> (Vec<u16>, usize, bool) {
    let mut labels = mask.clone().iter()
        .copied()
        .collect::<Vec<u16>>();

    labels.retain(|x| *x > 0);
    labels.sort();
    labels.dedup();

    let n_labels = labels.len();
    let is_binary = n_labels <= 1;

    (labels, n_labels, is_binary)
}

/// Draw a mask from a vector of polygons
///
/// # Arguments
///
/// * `polygons` - A vector of polygons to draw
/// * `width` - The width of the mask
/// * `height` - The height of the mask
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::process::mask::draw_mask;
///
/// let polygons = vec![
///     vec![[0.0, 0.0], [0.0, 1.0], [1.0, 1.0], [1.0, 0.0]],
///     vec![[2.0, 2.0], [2.0, 3.0], [3.0, 3.0], [3.0, 2.0]],
/// ];
///
/// let (mask, labels) = draw_mask(&polygons, 4, 4);
/// ```
pub fn draw_mask(polygons: &[Vec<[f64; 2]>], width: u32, height: u32) -> (Mask, Vec<u16>) {
    let mut mask = ImageBuffer::from_pixel(width, height, Luma([0u16]));
    let mut labels = Vec::new();
    for (i, polygon) in polygons.iter().enumerate() {
        let mut points = Vec::new();
        for point in polygon.iter() {
            points.push(Point::new(
                point[0].round() as i32,
                point[1].round() as i32
            ));
        }

        if points[0].x == points[points.len()-1].x 
        && points[0].y == points[points.len()-1].y {
            let mut i = 0;
            while i < points.len() - 1 {
                if points[i].x != points[i+1].x || points[i].y != points[i+1].y {
                    break;
                }
                i += 1;
            }

            let mut new_points = points[i+1..].to_vec();
            new_points.append(&mut points[..i+1].to_vec());
            points = new_points;
        }

        draw_polygon_mut(&mut mask, &points, Luma([i as u16 + 1]));

        labels.push(i as u16 + 1);
    }

    (mask, labels)
}
