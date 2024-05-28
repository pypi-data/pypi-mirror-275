use std::cmp::Ordering;
use rand_distr::Normal;
use rand_distr::Distribution;
use rand::{Rng, RngCore};
use rand::distributions::uniform::SampleUniform;
use nalgebra::{DVector, MatrixXx2, Matrix2};

use crate::Numeric;
use crate::helpers::vector_multiply;

/// Order points in base of their angle with respect to the centroid
/// 
/// # Arguments
///
/// * `points` - A vector of 2D points
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::geometry::points::order_points;
/// let points = vec![[0.0, 0.0], [1.0, 0.0], [0.0, 1.0]];
/// let ordered_points = order_points(points);
/// ```
pub fn order_points<T: Numeric>(mut points: Vec<[T; 2]>) -> Vec<[T; 2]> {
    let n = T::from_usize(points.len());
    let centroid = points.iter().fold([T::zero(); 2], |acc, p| {
        [acc[0] + p[0] / n, acc[1] + p[1] / n]
    });

    points.sort_by(|a, b| {
        let dx_a = a[0] - centroid[0];
        let dy_a = a[1] - centroid[1];
        let dx_b = b[0] - centroid[0];
        let dy_b = b[1] - centroid[1];

        if a[0] == b[0] || a[1] == b[1] {
            return (dy_a.atan2(dx_a)).partial_cmp(&(dy_b.atan2(dx_b))).unwrap();
        }

        let cross_product = dx_a * dy_b - dy_a * dx_b;
        if cross_product == T::zero() {
            let da = (dx_a * dx_a + dy_a * dy_a).sqrt(); 
            let db = (dx_b * dx_b + dy_b * dy_b).sqrt();
            if db >= da {
                return Ordering::Greater;
            } else {
                return Ordering::Less;
            }
        }

        (dy_a.atan2(dx_a)).partial_cmp(&(dy_b.atan2(dx_b))).unwrap()
    });

    points
}

/// Randomly sample points defined by x and y coordinates
///
/// # Arguments
///
/// * `n` - Number of points to sample
/// * `min_dist` - Minimum distance between points
/// * `rng` - A random number generator
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::geometry::points::sample_points;
/// use rand::thread_rng;
/// let mut rng = thread_rng();
/// let points = sample_points(100, 0.1, &mut rng);
/// ```
pub fn sample_points<T: Numeric, R: Rng + RngCore>(
    n: usize,
    min_dist: T,
    rng: &mut R,
) -> Result<Vec<[T; 2]>, &'static str> {
    let mut points = vec![[T::zero(); 2]; n];
    
    let mut attempt = 100;
    let mut spacing = false;
    while !spacing {
        attempt -= 1;
        for point in points.iter_mut() {
            *point = [
                T::from_f64(rng.gen_range(-1.0..1.0)),
                T::from_f64(rng.gen_range(-1.0..1.0)),
            ];
        }

        for i in 0..n {
            for j in 0..n {
                let dx = points[i][0] - points[j][0];
                let dy = points[i][1] - points[j][1];
                let dh = (dx * dx + dy * dy).sqrt();
                if i != j && dh < min_dist {
                    spacing = false;
                    break;
                } else {
                    spacing = true;
                }
            }
        }

        if attempt == 0 {
            break;
        }
    }
   
    if !spacing {
        Err("Failed to sample points. Lower min_dist or increase scale.")
    } else {
        Ok(points)
    }
}


/// Add random Gaussian noise to a set of points
///
/// # Arguments
///
/// * `points` - A vector of 2D points
/// * `sigma` - Standard deviation of the Gaussian noise
/// * `rng` - A random number generator
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::geometry::points::noisy_points;
/// use rand::thread_rng;
/// let mut rng = thread_rng();
/// let points = vec![[0.0, 0.0], [1.0, 0.0], [0.0, 1.0]];
/// let noisy_points = noisy_points(points, 0.1, &mut rng);
/// ```
pub fn noisy_points<T: Numeric, R: Rng + RngCore>(
    points: Vec<[T; 2]>,
    sigma: T,
    rng: &mut R,
) -> Vec<[T; 2]> {
    let normal = Normal::new(
        0.0,
        sigma.to_f64()
    ).unwrap();

    points.iter().map(|point| {
        let dx = T::from_f64(normal.sample(rng));
        let dy = T::from_f64(normal.sample(rng));
        [point[0] + dx, point[1] + dy]
    }).collect()
}

/// Connect points with a linear interpolation
///
/// # Arguments
///
/// * `points` - A vector of 2D points
/// * `n_interp` - Number of points to interpolate between each pair of points
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::geometry::points::connect_points_linear;
/// let points = vec![[0.0, 0.0], [1.0, 0.0], [0.0, 1.0]];
/// let connected_points = connect_points_linear(points, 10);
/// ```
pub fn connect_points_linear<T: Numeric>(
    points: Vec<[T; 2]>,
    n_interp: usize,
) -> Vec<[T; 2]> {
    let mut connected_points = Vec::new();
    for (i, point) in points.iter().enumerate() {
        connected_points.push(*point);
        let target = if i == points.len() - 1 {
            points[0]
        } else {
            points[i + 1]
        };

        let (x1, x2, y1, y2) = if point[0] < target[0] {
            (point[0], target[0], point[1], target[1])
        } else {
            (target[0], point[0], target[1], point[1])
        };

        let dx = x2 - x1;
        let dy = y2 - y1;

        for n in 1..n_interp {
            let x = x1 + T::from_usize(n) * dx / T::from_usize(n_interp);
            let y = y1 + T::from_usize(n) * dy / T::from_usize(n_interp);
            connected_points.push([x, y]);
        }
    }

    connected_points
}

/// Connect points via a bezier curve interpolation
///
/// # Arguments
///
/// * `points` - A vector of 2D points
/// * `n_interp` - Number of points to interpolate between each pair of points
/// * `rng` - A random number generator
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::geometry::points::connect_points_bezier;
/// use rand::thread_rng;
/// let mut rng = thread_rng();
/// let points = vec![[0.0, 0.0], [1.0, 0.0], [0.0, 1.0]];
/// let connected_points = connect_points_bezier(points, 10, &mut rng);
/// ```
pub fn connect_points_bezier<T: Numeric + SampleUniform, R: Rng + RngCore>(
    points: Vec<[T; 2]>,
    n_interp: usize,
    rng: &mut R,
) -> Vec<[T; 2]> {
    let mut bezier_points = Vec::new();
    for (i, point) in points.iter().enumerate() {
        let target = if i == points.len() - 1 {
            points[0]
        } else {
            points[i + 1]
        };

        let (x1, x2) = (point[0], target[0]);
        let (y1, y2) = (point[1], target[1]);

        let control = [
            x1 + (x2 - x1) * T::from_f64(rng.gen_range(0.0..1.0)),
            y1 + (y2 - y1) * T::from_f64(rng.gen_range(0.0..1.0)),
        ];

        for n in 0..n_interp {
            let t = T::from_usize(n) / T::from_usize(n_interp);

            let p1_x = point[0] * (T::one() - t).powf(T::two());
            let p1_y = point[1] * (T::one() - t).powf(T::two());
            let p2_x = control[0] * T::two() * t * (T::one() - t);
            let p2_y = control[1] * T::two() * t * (T::one() - t);
            let p3_x = target[0] * t.powf(T::two());
            let p3_y = target[1] * t.powf(T::two());

            bezier_points.push([
                p1_x + p2_x + p3_x,
                p1_y + p2_y + p3_y
            ]);
        }
    }

    bezier_points
}

/// Smooth points using a Gaussian filter
///
/// # Arguments
///
/// * `points` - A vector of 2D points
/// * `sigma` - Standard deviation of the Gaussian filter
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::geometry::points::smooth_points;
/// let points = vec![[0.0, 0.0], [1.0, 0.0], [0.0, 1.0]];
/// let smoothed_points = smooth_points(points, 0.1);
/// ```
pub fn smooth_points<T: Numeric>(
    points: Vec<[T; 2]>,
    sigma: T,
) -> Vec<[T; 2]> {
    fn gaussian_kernel<T: Numeric>(
        sigma: T,
        radius: usize,
    ) -> Vec<T> {
        let sigma = sigma * sigma;
        let radius = radius as isize;

        let phi_x = (-radius..=radius)
            .map(|x| (T::from_f64(-0.5) * T::from_isize(x * x) / sigma).exp())
            .collect::<Vec<T>>();

        let sum = phi_x.iter().fold(T::zero(), |acc, &x| acc + x);

        phi_x.iter().map(|&x| x / sum).collect()
    }

    let truncate = T::from_f64(4.0);
    let lw = (truncate * sigma).ceil().to_usize();
    let kernel: Vec<T> = gaussian_kernel(sigma, lw);

    // This constraint can probably be relaxed later to match the scipy implementation
    if points.len() < kernel.len() {
        println!("The number of points cannot be less than kernel size (sigma * 4). Please lower sigma");
        std::process::exit(1);
    }

    let kernel_size = kernel.len();
    let kernel_half = kernel_size / 2;
    let n_points = points.len();
        
    let mut smoothed = vec![[T::zero(); 2]; n_points];
    for c in 0..2 {
        // Create a buffer for storing points
        let mut buffer = vec![T::zero(); n_points + kernel_size];
        for i in kernel_half..n_points + kernel_half {
            buffer[i] = points[i - kernel_half][c];
        }

        // Add reflection padding to buffer similar to scipy
        for i in 0..kernel_half {
            buffer[i] = points[kernel_half - i - 1][c];
            buffer[n_points + kernel_half + i] = points[n_points - 1 - i][c];
        }

        // Apply kernel to each point in the input
        for i in 0..n_points {
            smoothed[i][c] = vector_multiply(
                &buffer[i..i + kernel_size],
                &kernel
            ).iter().fold(T::zero(), |acc, &x| acc + x);
        }
    } 

    smoothed
}

/// Resample points to a fixed number of equidistant points
///
/// # Arguments
///
/// * `points` - A vector of 2D points
/// * `n_points` - Number of points to resample
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::geometry::points::resample_points;
/// let points = vec![[0.0, 0.0], [1.0, 0.0], [0.0, 1.0]];
/// let resampled_points = resample_points(points, 10);
/// ```
pub fn resample_points<T: Numeric>(points: Vec<[T; 2]>, n_points: usize) -> Vec<[T; 2]> {
    // Close points
    let (points, is_closed) = if points[0] == points[points.len() - 1] {
        (points, true)
    } else {
        let mut points = points.clone();
        points.push(points[0]);
        (points, false)
    };

    let mut distances = Vec::new();
    for i in 0..points.len() - 1 {
        let dx = points[i][0] - points[i+1][0];
        let dy = points[i][1] - points[i+1][1];
        distances.push((dx * dx + dy * dy).sqrt());
    }

    let mut cum_distances = vec![T::zero(); points.len()];
    for i in 1..points.len() {
        cum_distances[i] = cum_distances[i - 1] + distances[i - 1];
    }

    let total_length = cum_distances[points.len() - 1];
    
    let sample_distances = (0..n_points).map(|i| {
        T::from_usize(i) * total_length / T::from_usize(n_points)
    }).collect::<Vec<T>>();

    let mut resampled_points = Vec::new();
    for sample_distance in sample_distances.iter() {
        let mut j = 0;
        while j < points.len() - 1 && *sample_distance >= cum_distances[j + 1] {
            j += 1;
        }

        let t = (*sample_distance - cum_distances[j]) / distances[j];
        let x = points[j][0] + t * (points[j + 1][0] - points[j][0]);
        let y = points[j][1] + t * (points[j + 1][1] - points[j][1]);
        resampled_points.push([x, y]);
    }

    if !is_closed {
        resampled_points.pop();
    }

    resampled_points
}

/// Check if a point is inside a polygon using the ray casting algorithm
///
/// # Arguments
///
/// * `point` - A 2D point
/// * `polygon` - A vector of 2D points
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::geometry::points::point_in_polygon;
/// let point = [0.2, 0.2];
/// let polygon = vec![[0.0, 0.0], [1.0, 0.0], [0.0, 1.0]];
/// let inside = point_in_polygon(&point, &polygon);
/// ```
///
/// # Notes
///
/// Points inside OR on the edge of the polygon are considered inside.
///
/// # References
///
/// 1. Ray casting algorithm: <https://rosettacode.org/wiki/Ray-casting_algorithm#Rust>
pub fn point_in_polygon<T: Numeric>(point: &[T; 2], polygon: &[[T; 2]]) -> bool {
    fn ray_intersect<T: Numeric>(point: &[T; 2], edge: &[[T; 2]; 2]) -> bool {
        let (px, mut py) = (point[0], point[1]);
        let (mut edge_a, mut edge_b) = (edge[0], edge[1]);
        if edge_a[1] > edge_b[1] {
            std::mem::swap(&mut edge_a, &mut edge_b);
        }
        
        if py == edge_a[1] || py == edge_b[1] {
            py += T::epsilon();
        }

        let max_x = if edge_a[0] > edge_b[0] { edge_a[0] } else { edge_b[0] };
        let min_x = if edge_a[0] < edge_b[0] { edge_a[0] } else { edge_b[0] };

        if (py > edge_b[1] || py < edge_a[1]) || px > max_x {
            false
        } else if px < min_x {
            true
        } else {
            let m_red = if (edge_a[0] - edge_b[0]).abs() > T::min_value() {
                (edge_b[1] - edge_a[1]) / (edge_b[0] - edge_a[0])
            } else {
                T::max_value()
            };
            let m_blue = if (edge_a[0] - px).abs() > T::min_value() {
                (py - edge_a[1]) / (px - edge_a[0])
            } else {
                T::max_value()
            };
            m_blue > m_red
        }
    }

    let mut intersects = 0;
    for i in 0..polygon.len() {
        let edge = [polygon[i], polygon[(i + 1) % polygon.len()]];
        if ray_intersect(point, &edge) {
            intersects += 1;
        }
    }

    intersects % 2 == 1
}

/// Align points to a reference shape using orthogonal Procrustes analysis
///
/// # Arguments
///
/// * `points` - A vector of 2D points
/// * `reference` - A vector of 2D points
/// * `scale` - Normalize each shape to unit norm
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::geometry::points::align_points_orthogonal;
/// let points = vec![[0.0, 0.0], [1.0, 0.0], [0.0, 1.0]];
/// let reference = vec![[0.0, 0.0], [1.0, 0.0], [0.0, 1.0]];
/// let aligned_points = align_points_orthogonal(&points, &reference, false);
/// ```
pub fn align_points_orthogonal(
    points: &[[f64; 2]],
    reference: &[[f64; 2]],
    scale: bool,
) -> Vec<[f64; 2]> {
    let n = points.len();
    if n != reference.len() {
        panic!("Number of points in points and reference must be equal");
    }

    let (remove_last, n) = if points[0] == points[n - 1] {
        (1, n - 1)
    } else {
        (0, n)
    };
    
    let (mut px, mut py, mut p_norm) = (0.0, 0.0, 0.0);
    let (mut rx, mut ry, mut r_norm) = (0.0, 0.0, 0.0);
    for i in 0..n {
        px += points[i][0];
        py += points[i][1];
        rx += reference[i][0];
        ry += reference[i][1];

        p_norm += points[i][0] * points[i][0] + points[i][1] * points[i][1];
        r_norm += reference[i][0] * reference[i][0] + reference[i][1] * reference[i][1];
    }

    px /= n as f64;
    py /= n as f64;
    rx /= n as f64;
    ry /= n as f64;

    if scale {
        p_norm = p_norm.sqrt();
        r_norm = r_norm.sqrt();
    } else {
        p_norm = 1.0;
        r_norm = 1.0;
    }

    let p = MatrixXx2::from_columns(&[
        DVector::from_iterator(n, points[0..n].iter().map(|p| (p[0] - px) / p_norm)),
        DVector::from_iterator(n, points[0..n].iter().map(|p| (p[1] - py) / p_norm)),
    ]).transpose();

    let r = MatrixXx2::from_columns(&[
        DVector::from_iterator(n, reference[0..n].iter().map(|p| (p[0] - rx) / r_norm)),
        DVector::from_iterator(n, reference[0..n].iter().map(|p| (p[1] - ry) / r_norm)),
    ]);

    let dot: Matrix2<f64> = (&p * r).transpose();
    let svd = nalgebra::linalg::SVD::new(dot, true, true);
    let (u, _, vt) = (svd.u.unwrap(), svd.singular_values, svd.v_t.unwrap());
    let mut rotation = u * vt;

    if rotation.determinant() < 0.0 {
        let s = nalgebra::Matrix2::new(1.0, 0.0, 0.0, -1.0 * rotation.determinant().signum());
        rotation = (u * s) * vt;
    }

    let p = (rotation * p).data
        .as_vec()
        .chunks(2)
        .map(|c| [c[0], c[1]])
        .collect();

    if remove_last == 0 {
        p
    } else {
        let mut p = p;
        p.push(p[0]);
        p
    }
}
