use std::fmt::Debug;
use std::sync::Mutex;
use std::marker::{Send, Sync};
use rand::Rng;
use rand::SeedableRng;
use rand_chacha::ChaCha20Rng;
use rand::distributions::uniform::SampleUniform;
use rayon::iter::ParallelIterator;
use kdam::{rayon::prelude::*, TqdmParallelIterator};
use image::{DynamicImage, ImageBuffer, Luma};

use crate::Numeric;
use crate::helpers::progress_bar;
use crate::draw::random_polygons;
use crate::geometry::points::point_in_polygon;

/// Generate random binary masks
///
/// # Arguments
///
/// * `n_masks` - The number of masks to generate
/// * `height` - The height of the mask
/// * `width` - The width of the mask
/// * `pad_fraction_min` - The minimum padding fraction to add around binary mask
/// * `pad_fraction_max` - The maximum padding fraction to add around binary mask
/// * `n_points` - The number of initial points to sample for each polygon
/// * `min_dist` - The minimum distance between points
/// * `n_interp` - The number of points to interpolate between initial points
/// * `mode` - The interpolation mode to use (linear or bezier)
/// * `sigma` - The standard deviation of the noise to add to the polygon
/// * `smooth` - The standard deviation of the Gaussian filter to smooth the polygon
/// * `seed` - The seed for the random number generator
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::draw::random_masks;
/// let masks = random_masks(10000, 64, 64, 0.2, 0.2, 5, 0.5, 10, "bezier", 0.05, 3.0, 0);
/// ```
pub fn random_masks<T: Numeric + SampleUniform + Send + Sync + Debug>(
    n_masks: usize,
    height: u32,
    width: u32,
    pad_fraction_min: T,
    pad_fraction_max: T,
    n_points: usize,
    min_dist: T,
    n_interp: usize,
    mode: &str,
    sigma: T,
    smooth: T, 
    seed: u64,
) -> Vec<DynamicImage> {
    if n_masks < 1 {
        println!("n_masks must be greater than or equal to 1");
        std::process::exit(1);
    }

    if height < 1 || width < 1 {
        println!("height and width must be greater than or equal to 1");
        std::process::exit(1);
    }

    if pad_fraction_max < pad_fraction_min {
        println!("pad_fraction_max must be greater than pad_fraction_min");
        std::process::exit(1);
    }

    if pad_fraction_min < T::zero() || pad_fraction_max > T::one() {
        println!("pad_fraction_min and pad_fraction_max must be between 0.0 and 1.0");
        std::process::exit(1);
    }
    
    let pb = progress_bar(n_masks, "Sampling random binary masks");

    let length = if height < width {
        T::from_u32(height)
    } else { 
        T::from_u32(width)
    };

    // Randomly sample polygons to draw onto grid
    let polygons: Vec<Vec<[T; 2]>> = random_polygons(
        n_masks,
        n_points,
        min_dist, 
        T::from_f64(5.0), 
        T::from_f64(5.0), 
        n_interp, 
        mode,
        sigma,
        smooth, 
        true,
        seed
    );

    let masks = Mutex::new(Vec::new());
    (0..n_masks)
        .into_par_iter()
        .tqdm_with_bar(pb)
        .for_each(|i| {
            let polygon = &polygons[i];
            let mut rng = ChaCha20Rng::seed_from_u64(seed);
            rng.set_stream(i as u64);

            // Sample a padding fraction to add around the binary mask
            let pad_fraction = if pad_fraction_min == pad_fraction_max {
                pad_fraction_min
            } else {
                rng.gen_range(pad_fraction_min..pad_fraction_max)
            };

            // Initialize mask
            let mut mask = ImageBuffer::from_fn(
                height, width, |_, _| { Luma([0]) }
            );

            // Find bounding box and centroid of polygon
            let (xmin, xmax, ymin, ymax) = polygon.iter().fold(
                (T::infinity(), T::neg_infinity(), T::infinity(), T::neg_infinity()),
                |(xmin, xmax, ymin, ymax), point| {
                    (
                        xmin.min(point[0]), xmax.max(point[0]),
                        ymin.min(point[1]), ymax.max(point[1])
                    )
                }
            );

            let (cx, cy) = ((xmin + xmax) / T::two(), (ymin + ymax) / T::two());
            let scale = if (xmax - xmin) > (ymax - ymin) { xmax - xmin } else { ymax - ymin };

            // Scale and center polygon inside mask
            let polygon = polygon.iter().map(|point| {
                [
                    (point[0] - cx) / scale * (length * (T::one() - pad_fraction)) + length / T::two(),
                    (point[1] - cy) / scale * (length * (T::one() - pad_fraction)) + length / T::two() 
                ]
            }).collect::<Vec<[T; 2]>>();

            // Draw polygon onto mask
            for y in 0..height {
                for x in 0..width {
                    let inside = point_in_polygon::<T>(
                        &[T::from_u32(x), T::from_u32(y)], 
                        &polygon
                    ); 

                    if inside {
                        mask[(y,x)] = Luma([255]);
                    }
                }
            }

            let mask = DynamicImage::ImageLuma8(mask);
            masks.lock().unwrap().push(mask);
    });

    masks.into_inner().unwrap()
}
