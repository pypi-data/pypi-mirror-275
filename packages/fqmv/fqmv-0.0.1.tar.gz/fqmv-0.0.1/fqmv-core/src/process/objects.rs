use image::{GenericImage, Pixel, Luma};

use crate::types::{Image, Mask};
use crate::process::transform;
use crate::process::mask::binary_object;
use crate::process::mask::{mask_background, mask_foreground};

/// Extract full objects from an image using bounding boxes
///
/// # Arguments
///
/// * `image` - A reference to the image to be processed
/// * `bounding_boxes` - A list of bounding boxes to extract objects
/// * `resize` - An optional tuple of new width and height for resizing
/// * `filter` - An optional filter type for resizing
///
/// # Examples
///
/// ```no_run
/// use image::{ImageBuffer, Luma};
/// use fqmv_core::process::objects::extract_objects;
///
/// let mut img = ImageBuffer::from_fn(4, 4, |x, y| {
///     if x % 2 == 0 {
///         Luma([0u16])
///     } else {
///         Luma([255u16])
///     }
/// });
///
/// let bounding_boxes = vec![
///     vec![0.0, 1.0, 0.0, 1.0],
///     vec![2.0, 3.0, 2.0, 3.0],
/// ];
///
/// let objects = extract_objects(&mut img, &bounding_boxes, Some((2, 2)), Some("nearest"));
/// ```
pub fn extract_objects<I, P>(
    image: &mut I,
    bounding_boxes: &[Vec<f64>],
    resize: Option<(u32, u32)>,
    filter: Option<&str>
) -> Vec<Image<P>> 
where
    I: GenericImage<Pixel = P> + 'static,
    P: Pixel + 'static,
{
    if resize.is_some() && filter.is_none() {
        panic!("Resize filter type must be specified when resizing images");
    }

    let mut objects = Vec::new();
    for bbox in bounding_boxes.iter() {
        let object = transform::crop_box(image, bbox);
        let (ow, oh) = resize.unwrap_or((0, 0));

        if ow == 0 || oh == 0 {
            objects.push(object);
        } else {
            objects.push(transform::resize(&object, ow, oh, filter.unwrap()));
        };
    }

    objects
}

/// Extract foreground objects from an image using bounding boxes
///
/// # Arguments
///
/// * `image` - A reference to the image to be processed
/// * `mask` - A reference to the mask to be applied
/// * `bounding_boxes` - A list of bounding boxes to extract objects
/// * `labels` - A list of object labels to isolate
/// * `resize` - An optional tuple of new width and height for resizing
/// * `filter` - An optional filter type for resizing
///
/// # Examples
///
/// ```no_run
/// use image::{ImageBuffer, Luma};
/// use fqmv_core::process::objects::extract_foreground_objects;
///
/// let mut img = ImageBuffer::from_fn(4, 4, |x, y| {
///     if x % 2 == 0 {
///         Luma([0u16])
///     } else {
///         Luma([255u16])
///     }
/// });
///
/// let mut mask = ImageBuffer::from_fn(4, 4, |x, y| { Luma([0u16]) });
/// for i in 0..4 {
///     mask.put_pixel(1, i, Luma([1u16]));
///     mask.put_pixel(3, i, Luma([2u16]));
/// }
///
///
/// let bounding_boxes = vec![
///     vec![1.0, 0.0, 2.0, 3.0],
///     vec![3.0, 0.0, 4.0, 3.0],
/// ];
///
/// let labels = vec![1, 2];
///
/// let objects = extract_foreground_objects(
///     &mut img,
///     &mut mask,
///     &bounding_boxes,
///     &labels,
///     Some((2, 2)),
///     Some("nearest"),
/// );
/// ```
pub fn extract_foreground_objects<I, P>(
    image: &mut I,
    mask: &mut Mask,
    bounding_boxes: &[Vec<f64>],
    labels: &[u16],
    resize: Option<(u32, u32)>,
    filter: Option<&str>
) -> Vec<Image<P>> 
where
    I: GenericImage<Pixel = P> + 'static,
    P: Pixel + 'static,
    <P as Pixel>::Subpixel: 'static + From<u8>,
{
    let mut objects = Vec::new();
    for (label, bbox) in labels.iter().zip(bounding_boxes.iter()) {
        let background = transform::crop_box(mask, bbox);
        let background = binary_object::<u16>(&background, *label);

        let object = mask_background(
            &transform::crop_box(image, bbox),
            &background
        );

        let (ow, oh) = resize.unwrap_or((0, 0));

        if ow == 0 || oh == 0 {
            objects.push(object);
        } else {
            objects.push(transform::resize(&object, ow, oh, filter.unwrap()));
        };
    }

    objects
}

/// Extract background objects from an image using bounding boxes
///
/// # Arguments
///
/// * `image` - A reference to the image to be processed
/// * `mask` - A reference to the mask to be applied
/// * `bounding_boxes` - A list of bounding boxes to extract objects
/// * `labels` - A list of object labels to isolate
/// * `resize` - An optional tuple of new width and height for resizing
/// * `filter` - An optional filter type for resizing
///
/// # Examples
///
/// ```no_run
/// use image::{ImageBuffer, Luma};
/// use fqmv_core::process::objects::extract_background_objects;
///
/// let mut img = ImageBuffer::from_fn(4, 4, |x, y| {
///     if x % 2 == 0 {
///         Luma([0u16])
///     } else {
///         Luma([255u16])
///     }
/// });
///
/// let mut mask = ImageBuffer::from_fn(4, 4, |x, y| { Luma([0u16]) });
/// for i in 0..4 {
///     mask.put_pixel(1, i, Luma([1u16]));
///     mask.put_pixel(3, i, Luma([2u16]));
/// }
///
/// let bounding_boxes = vec![
///     vec![1.0, 0.0, 2.0, 3.0],
///     vec![3.0, 0.0, 4.0, 3.0],
/// ];
///
/// let labels = vec![1, 2];
/// let objects = extract_background_objects(
///     &mut img,
///     &mut mask,
///     &bounding_boxes,
///     &labels,
///     Some((2, 2)),
///     Some("nearest"),
/// );
/// ```
pub fn extract_background_objects<I, P>(
    image: &mut I,
    mask: &mut Mask,
    bounding_boxes: &[Vec<f64>],
    labels: &[u16],
    resize: Option<(u32, u32)>,
    filter: Option<&str>
) -> Vec<Image<P>> 
where
    I: GenericImage<Pixel = P> + 'static,
    P: Pixel + 'static,
    <P as Pixel>::Subpixel: 'static + From<u8>,
{
    let mut objects = Vec::new();
    for (label, bbox) in labels.iter().zip(bounding_boxes.iter()) {
        let foreground = transform::crop_box(mask, bbox);
        let foreground = binary_object::<u16>(&foreground, *label);

        let object = mask_foreground(
            &transform::crop_box(image, bbox),
            &foreground
        );

        let (ow, oh) = resize.unwrap_or((0, 0));

        if ow == 0 || oh == 0 {
            objects.push(object);
        } else {
            objects.push(transform::resize(&object, ow, oh, filter.unwrap()));
        };
    }

    objects
}

/// Extract all objects from an image using bounding boxes
/// 
/// # Arguments
///
/// * `image` - A reference to the image to be processed
/// * `mask` - A reference to the mask to be applied
/// * `bounding_boxes` - A list of bounding boxes to extract objects
/// * `labels` - A list of object labels to isolate
/// * `resize` - An optional tuple of new width and height for resizing
/// * `filter` - An optional filter type for resizing
///
/// # Examples
///
/// ```no_run
/// use image::{ImageBuffer, Luma};
/// use fqmv_core::process::objects::extract_all_objects;
///
/// let mut img = ImageBuffer::from_fn(4, 4, |x, y| {
///     if x % 2 == 0 {
///         Luma([0u16])
///     } else {
///         Luma([255u16])
///     }
/// });
///
/// let mut mask = ImageBuffer::from_fn(4, 4, |x, y| { Luma([0u16]) });
/// for i in 0..4 {
///     mask.put_pixel(1, i, Luma([1u16]));
///     mask.put_pixel(3, i, Luma([2u16]));
/// }
///
/// let bounding_boxes = vec![
///     vec![1.0, 0.0, 2.0, 3.0],
///     vec![3.0, 0.0, 4.0, 3.0],
/// ];
///
/// let labels = vec![1, 2];
/// let (objects, foreground_objects, background_objects, binary_objects) = extract_all_objects(
///     &mut img,
///     &mut mask,
///     &bounding_boxes,
///     &labels,
///     Some((2, 2)),
///     Some("nearest"),
/// );
/// ```
pub fn extract_all_objects<I, P>(
    image: &mut I,
    mask: &mut Mask,
    bounding_boxes: &[Vec<f64>],
    labels: &[u16],
    resize: Option<(u32, u32)>,
    filter: Option<&str>
) -> (Vec<Image<P>>, Vec<Image<P>>, Vec<Image<P>>, Vec<Image<Luma<u16>>>) 
where
    I: GenericImage<Pixel = P> + 'static,
    P: Pixel + 'static,
    <P as Pixel>::Subpixel: 'static + From<u8>,
{
    let mut objects = Vec::new();
    let mut foreground_objects = Vec::new();
    let mut background_objects = Vec::new();
    let mut binary_objects = Vec::new();

    for (label, bbox) in labels.iter().zip(bounding_boxes.iter()) {
        let object = transform::crop_box(image, bbox);

        let background = transform::crop_box(mask, bbox);
        let background = binary_object::<u16>(&background, *label);
        let foreground_object = mask_background(
            &transform::crop_box(image, bbox),
            &background
        );

        let foreground = transform::crop_box(mask, bbox);
        let foreground = binary_object::<u16>(&foreground, *label);
        let background_object = mask_foreground(
            &transform::crop_box(image, bbox),
            &foreground
        );

        let binary = transform::crop_box(mask, bbox);
        let binary_object = binary_object::<u16>(&binary, *label);

        let (ow, oh) = resize.unwrap_or((0, 0));

        if ow == 0 || oh == 0 {
            objects.push(object);
            foreground_objects.push(foreground_object);
            background_objects.push(background_object);
            binary_objects.push(binary_object);
        } else {
            objects.push(transform::resize(&object, ow, oh, filter.unwrap()));
            foreground_objects.push(transform::resize(&foreground_object, ow, oh, filter.unwrap()));
            background_objects.push(transform::resize(&background_object, ow, oh, filter.unwrap()));
        };
    }

    (objects, foreground_objects, background_objects, binary_objects)
}
