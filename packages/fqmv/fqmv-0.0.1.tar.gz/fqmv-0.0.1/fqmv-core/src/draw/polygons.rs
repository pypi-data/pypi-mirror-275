use std::fmt::Debug;
use std::sync::Mutex;
use std::marker::{Send, Sync};
use rand::Rng;
use rand::SeedableRng;
use rand_chacha::ChaCha20Rng;
use rand::distributions::uniform::SampleUniform;
use rayon::iter::ParallelIterator;
use kdam::{rayon::prelude::*, TqdmParallelIterator};

use crate::Numeric;
use crate::helpers::progress_bar;
use crate::geometry::points::{
    sample_points,
    noisy_points,
    order_points,
    connect_points_linear,
    connect_points_bezier,
    smooth_points,
    resample_points,
};

/// Generate random polygons
///
/// # Arguments
///
/// * `n_polygons` - The number of polygons to generate
/// * `n_points` - The number of initial points to sample for each polygon
/// * `min_dist` - The minimum distance between points
/// * `min_scale` - The minimum scale of the polygon
/// * `max_scale` - The maximum scale of the polygon
/// * `n_interp` - The number of points to interpolate between initial points
/// * `mode` - The interpolation mode to use (linear or bezier)
/// * `sigma` - The standard deviation of the noise to add to the polygon
/// * `smooth` - The standard deviation of the Gaussian filter to smooth the polygon
/// * `close_polygon` - Whether to close the polygon
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::draw::random_polygons;
/// let points = random_polygons(10000, 5, 0.5, 1.0, 7.0, 20, "bezier", 0.05, 3.0, true, 0);
/// ```
///
/// # Notes
///
/// The total number of points in the sampled polygons will be n_points * n_interp
pub fn random_polygons<T: Numeric + SampleUniform + Send + Sync + Debug>(
    n_polygons: usize,
    n_points: usize,
    min_dist: T,
    min_scale: T,
    max_scale: T,
    n_interp: usize,
    mode: &str,
    sigma: T,
    smooth: T,
    close_polygon: bool,
    seed: u64,
) -> Vec<Vec<[T; 2]>> {
    let pb = progress_bar(n_polygons, "Sampling random polygons");

    if n_polygons < 1 {
        println!("n_polygons must be greater than or equal to 1");
        std::process::exit(1);
    }

    if n_points < 3 {
        println!("n_points must be greater than or equal to 3");
        std::process::exit(1);
    }

    if min_scale > max_scale {
        println!("min_scale must be less than or equal to max_scale");
        std::process::exit(1);
    }

    if min_scale < T::from_f64(0.1) {
        println!("min_scale must be greater than or equal to 0.1");
        std::process::exit(1);
    }

    if n_interp < 1 {
        println!("n_interp must be greater than or equal to 2");
        std::process::exit(1);
    }

    if mode != "linear" && mode != "bezier" {
        println!("mode must be either linear or bezier");
        std::process::exit(1);
    }

    if sigma < T::zero() {
        println!("sigma must be greater than or equal to 0.0");
        std::process::exit(1);
    }

    if smooth < T::zero() {
        println!("smooth must be greater than or equal to 0.0");
        std::process::exit(1);
    }

    if n_points * n_interp < (sigma * T::from_f64(4.0)).ceil().to_usize() {
        println!("n_points * n_interp must be greater than or equal to 4 * sigma");
        std::process::exit(1);
    }

    let polygons = Mutex::new(Vec::new());
    (0..n_polygons)
        .into_par_iter()
        .tqdm_with_bar(pb)
        .for_each(|i| {
            let mut rng = ChaCha20Rng::seed_from_u64(seed);
            rng.set_stream(i as u64);

            let scale = if min_scale == max_scale {
                min_scale
            } else {
                rng.gen_range(min_scale..max_scale)
            };

            // Sample initial point defining polygon
            let points = sample_points(n_points, min_dist, &mut rng);
            let points = match points {
                Ok(points) => points,
                Err(err) => {
                    println!("{}", err);
                    std::process::exit(1);
                }
            };

            // Re-order then add more points between initial polygon points
            let points = order_points(points);
            let points = match mode {
                "linear" => connect_points_linear(points, n_interp),
                "bezier" => connect_points_bezier(points, n_interp, &mut rng),
                _ => points,
            };
            
            // Add noise and perform a final re-ordering
            let points = noisy_points(points, sigma, &mut rng);
            let mut points = order_points(points);

            
            // Shift to origin
            let centroid = points.iter().fold(
                [T::zero(); 2], |acc, p| {[
                    acc[0] + p[0] / T::from_usize(points.len()),
                    acc[1] + p[1] / T::from_usize(points.len())
            ]});
            
            points = points
                .iter()
                .map(|p| [p[0] - centroid[0], p[1] - centroid[1]])
                .collect();

            // Scale polygon from unit norm
            let norm = points.iter().fold(
                T::zero(), |acc, p| {
                    acc + p[0] * p[0] + p[1] * p[1]    
            }).sqrt();

            points = points
                .iter()
                .map(|p| [p[0] * scale / norm, p[1] * scale / norm])
                .collect();

            // Smooth points using a Gaussian filter
            if smooth > T::zero() {
                points = smooth_points(points, smooth);
            }

            // Resample points to ensure a consistent number of points
            points = resample_points(points, n_points * n_interp);

            if close_polygon && points[0] != points[points.len() - 1] {
                points.push(points[0]);
            }

            polygons.lock().unwrap().push(points);
         });

    polygons.into_inner().unwrap()
}
