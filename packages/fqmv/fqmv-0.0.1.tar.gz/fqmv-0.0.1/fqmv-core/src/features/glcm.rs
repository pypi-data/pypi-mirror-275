use image::{Pixel, Luma};

use crate::types::Image;
use crate::utils::matrix::Matrix;

/// Creates a gray level co-occurence matrix from a dynamic image
///
/// # Arguments
///
/// * `img` - A dynamic image to be converted
/// * `distance` - The distance used to assign neighbours in co-level matrix
/// * `angle` - The angle used to assign neighbours in co-level matrix
/// * `levels` - The number of levels to build the co-matrix
/// * `symmetric` - Whether to use a symmetric co-matrix
/// * `normalize` - Whether to normalize the co-matrix to sum to 1
/// * `rescale` - Rescale input image to the range (0, levels - 1.0)
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::features::glcm;
/// let img = image::open("path/to/image.png").unwrap().to_luma8();
/// let comatrix = glcm(&img, 1.0, 0.0, 256, true, true, true);
/// ```
pub fn glcm(
    img: &Image<Luma<u8>>,
    distance: f32,
    angle: f32,
    levels: usize,
    symmetric: bool,
    normalize: bool,
    rescale: bool,
) -> Matrix {
    if levels > 256 {
        println!("Warning: The maximum number of levels is 256.");
        std::process::exit(1);
    }

    let radians = angle.to_radians();
    let (width, height) = img.dimensions();

    let (sa, sb, sc) = if rescale {
        let (imin, imax) = img.pixels().fold((u8::MAX, u8::MIN), |(imin, imax), p| {
            let val = p.channels()[0];
            (imin.min(val), imax.max(val))
        });

        let imin = imin as f64;
        let imax = imax as f64;

        if imax != levels as f64 - 1.0 || imin != 0.0 {
            (imin, imax, levels as f64 - 1.0)
        } else if imin == imax {
            // Homogeneous images are set to zero
            (0.0, 1.0, 0.0)
        } else {
            (0.0, 1.0, 1.0)
        }
    } else {
        (0.0, 1.0, 1.0)
    };

    let (width, height) = (width as i32, height as i32);
    let offset_x = (radians.cos() * distance).round() as i32;
    let offset_y = (radians.sin() * distance).round() as i32;

    let mut comatrix = Matrix::new(levels, levels);

    let mut pixel_values: Vec<u8> = Vec::with_capacity((width * height) as usize);
    for pixel in img.pixels() {
        pixel_values.push(pixel.channels()[0]);
    }

    let scale_pixel = |pixel: u8| -> usize {
        ((pixel as f64 - sa) / (sb - sa) * sc).round() as usize
    };

    for y in 0..height {
        for x in 0..width {
            let idx = (y * width + x) as usize;
            let root = pixel_values[idx];
            let i_offset = x + offset_x;
            let j_offset = y + offset_y;

            if i_offset >= width || i_offset < 0 || j_offset >= height || j_offset < 0 {
                continue;
            }

            let neighbour_idx = (j_offset * width + i_offset) as usize;
            let neighbour = pixel_values[neighbour_idx];

            let root_scaled = scale_pixel(root);
            let neighbour_scaled = scale_pixel(neighbour);

            comatrix[(root_scaled, neighbour_scaled)] += 1.0;

            if symmetric {
                comatrix[(neighbour_scaled, root_scaled)] += 1.0;
            }
        }
    }

    if normalize {
        comatrix.normalize();
    }

    comatrix
}
