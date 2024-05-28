use imageproc::contours::find_contours;

use crate::Numeric;
use crate::types::Mask;
use crate::process::mask::{binary_mask, binary_object};

/// Get the contours outlining objects in a mask
///
/// # Arguments
///
/// * `mask` - A reference to the mask to be processed
/// * `labels` - An optional list of object labels to isolate
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::utils::toy;
/// use fqmv_core::process::lines::extract_contours;
///
/// let mask = toy::mask();
///
/// let contours = extract_contours::<u32>(&mask, None);
/// ```
pub fn extract_contours<T>(
    mask: &Mask,
    labels: Option<&Vec<u16>>,
) -> Vec<Vec<[T; 2]>>
where
    T: Numeric,
{
    if labels.is_some() {
        let labels = labels.unwrap();
        let mut contours = Vec::new();
        for label in labels.iter() {
            let binary = binary_object(mask, *label);
            let contour = find_contours::<i64>(&binary);
            let contour = contour[0].points.iter()
                .map(|p| [T::from_i64(p.x), T::from_i64(p.y)])
                .collect::<Vec<[T; 2]>>();
            
            contours.push(contour);
        }
        
        contours
    } else {
        let binary_mask = binary_mask(mask);
        let contours = find_contours::<i64>(&binary_mask);
        
        contours.iter().map(|c| {
            c.points.iter()
                .map(|p| [T::from_i64(p.x), T::from_i64(p.y)])
                .collect::<Vec<[T; 2]>>()
        }).collect::<Vec<Vec<[T; 2]>>>()
    }
}

/// Get the bounding boxes of objects in a mask
///
/// # Arguments
///
/// * `mask` - A reference to the mask to be processed
/// * `pad` - An optional padding value to add to the bounding boxes
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::utils::toy;
/// use fqmv_core::process::lines::{extract_contours, extract_bounding_boxes};
///
/// let mask = toy::mask();
///
/// let contours = extract_contours::<f64>(&mask, None);
/// let bounding_boxes = extract_bounding_boxes::<f64>(&contours, None);
/// ```
pub fn extract_bounding_boxes<T>(
    contours: &[Vec<[T; 2]>],
    pad: Option<u32>,
) -> Vec<Vec<T>>
where
    T: Numeric,
{
    contours.iter().map(|c| {
        let mut min_x = T::max_value();
        let mut min_y = T::max_value();
        let mut max_x = T::min_value();
        let mut max_y = T::min_value();

        for p in c {
            if p[0] < min_x { min_x = p[0]; }
            if p[1] < min_y { min_y = p[1]; }
            if p[0] > max_x { max_x = p[0]; }
            if p[1] > max_y { max_y = p[1]; }
        }

        let pad = T::from_u32(pad.unwrap_or(0));
        min_x -= pad;
        min_y -= pad;
        max_x += pad;
        max_y += pad;

        vec![min_x, min_y, max_x, max_y]
    }).collect::<Vec<Vec<T>>>()
}
