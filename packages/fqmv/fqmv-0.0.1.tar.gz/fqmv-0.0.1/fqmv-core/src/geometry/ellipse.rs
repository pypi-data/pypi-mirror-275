/// Fitting an ellipse to points
use nalgebra::{MatrixXx3, Matrix3, MatrixXx5, DMatrix, DVector, Vector3, Vector6};

use crate::Numeric;
use crate::geometry::points::resample_points;

/// Compute parameters of a best fit ellipse for a set of points using the least squares method
///
/// # Arguments
///
/// * `points` - A vector of points (x,y) to fit an ellipse to
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::geometry::ellipse;
/// let points = vec![[0.0, 0.0], [0.0, 1.0], [1.0, 1.0], [0.0, 0.0]];
/// let ellipse = ellipse::fit_ellipse_lstsq(&points);
/// ```
pub fn fit_ellipse_lstsq<T: Numeric>(points: &[[T; 2]]) -> Vec<T> {
    let points = if points[0] != points[points.len()-1] {
        let mut new_points = points.to_owned();
        new_points.push(points[0]);
        new_points
    } else {
        points.to_owned()
    };

    let points = if points.len() < 32 {
        resample_points(points, 32)
    } else {
        points
    };
    
    let (cx, cy) = points
        .iter()
        .skip(1)
        .fold((T::zero(), T::zero()), |(cx, cy), p| (cx + p[0], cy + p[1]));
    
    let n = T::from_usize(points.len() - 1);
    let points: Vec<[f64; 2]> = points.iter()
        .map(|p| [(p[0] - cx/n).to_f64(), (p[1] - cy/n).to_f64()])
        .collect();

    let design: MatrixXx5<f64> = MatrixXx5::from_columns(&[
        DVector::from_iterator(points.len(), points.iter().map(|p| p[0] * p[0])),
        DVector::from_iterator(points.len(), points.iter().map(|p| p[0] * p[1])),
        DVector::from_iterator(points.len(), points.iter().map(|p| p[1] * p[1])),
        DVector::from_iterator(points.len(), points.iter().map(|p| p[0])),
        DVector::from_iterator(points.len(), points.iter().map(|p| p[1])),
    ]);

    let y = DVector::from_iterator(points.len(), points.iter().map(|_| 1.0_f64));

    let epsilon = 1e-8;
    let results = lstsq::lstsq(&design, &y, epsilon).unwrap();

    let a: f64 = results.solution[0];
    let b: f64 = results.solution[1] / 2.0;
    let c: f64 = results.solution[2];
    let d: f64 = results.solution[3] / 2.0;
    let f: f64 = results.solution[4] / 2.0;
    let g: f64 = -1.0;

    let denominator = b * b - a * c;
    let numerator = 2.0 * (a * f * f + c * d * d + g * b * b - 2.0 * b * d * f - a * c * g);
    let factor = ((a - c) * (a - c) + 4.0 * b * b).sqrt();

    let mut axis_length_major = (numerator / denominator / (factor - a - c)).sqrt();
    let mut axis_length_minor = (numerator / denominator / (-factor - a - c)).sqrt();

    let mut width_gt_height = true;
    if axis_length_major < axis_length_minor {
        width_gt_height = false;
        std::mem::swap(&mut axis_length_major, &mut axis_length_minor);
    }

    let mut r = (axis_length_minor / axis_length_major).powf(2.0);
    r = if r > 1.0 { 1.0 / r } else { r };
    let eccentricity = (1.0 - r).sqrt();

    let mut phi = if b == 0.0 {
        if a < c { 0.0 } else { std::f64::consts::PI / 2.0 }
    } else {
        let mut inner = ((2.0 * b) / (a - c)).atan() / 2.0;
        inner += if a > c { std::f64::consts::PI / 2.0 } else { 0.0 };
        inner
    };

    phi += if !width_gt_height { std::f64::consts::PI / 2.0 } else { 0.0 };
    phi %= std::f64::consts::PI;

    vec![
        T::from_f64(axis_length_major) * T::two(),
        T::from_f64(axis_length_minor) * T::two(),
        T::from_f64(eccentricity),
        T::from_f64(phi)
    ]
}

/// Compute parameters of a best fit ellipse for a set of points using the direct method
///
/// # Arguments
///
/// * `points` - A vector of points (x,y) to fit an ellipse to
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::geometry::ellipse;
/// let points = vec![[0.0, 0.0], [0.0, 1.0], [1.0, 1.0], [0.0, 0.0]];
/// let ellipse = ellipse::fit_ellipse_direct(&points);
/// ```
///
/// # Notes
///
/// Although theoretically this should provide better fits than the basic least
/// squares approach, it has issues with numerical stability with current rust
/// linear algebra libraries relative to numpy. These errors usually arise when
/// computing eigenvectors so it might be useful to think about better ways to
/// approximate these. We won't use this function for now.
///
/// # References
///
/// 1. "Numerically stable direct least squares fitting of ellipses". R. Halir & J. Flusser. 1998.
/// 2. Fitting ellipses in python: <https://scipython.com/blog/direct-linear-least-squares-fitting-of-an-ellipse/>
/// 3. Another less stable implementation of the direct method: <https://github.com/AkosSeres/ellipse_detect>
pub fn fit_ellipse_direct<T: Numeric>(points: &[[T; 2]]) -> Vec<T> {
    let max_iter: usize = 1000;

    // These initial preprocessing steps help with numerical stability but should probably be
    // thought through a bit more
    // - Ensure that the points are closed
    // - Resample the points to a minimum number of points
    // - Center the points around the centroid
    // - Scale by the maximum bound and then rescale by norm
    let mut points = if points[0] != points[points.len()-1] {
        let mut new_points = points.to_owned();
        new_points.push(points[0]);
        new_points
    } else {
        points.to_owned()
    };

    if points.len() < 16 {
        points = resample_points(points, 16);
    }

    let design_1: MatrixXx3<f64> = MatrixXx3::from_columns(&[
        DVector::from_iterator(points.len(), points.iter().map(|p| T::to_f64(p[0] * p[0]))),
        DVector::from_iterator(points.len(), points.iter().map(|p| T::to_f64(p[0] * p[1]))),
        DVector::from_iterator(points.len(), points.iter().map(|p| T::to_f64(p[1] * p[1]))),
    ]);

    let design_2: MatrixXx3<f64> = MatrixXx3::from_columns(&[
        DVector::from_iterator(points.len(), points.iter().map(|p| T::to_f64(p[0]))),
        DVector::from_iterator(points.len(), points.iter().map(|p| T::to_f64(p[1]))),
        DVector::from_iterator(points.len(), points.iter().map(|_| 1.0_f64)),
    ]);

    let scatter_1 = &design_1.transpose() * &design_1;
    let scatter_2 = &design_2.transpose() * &design_1;
    let scatter_3 = &design_2.transpose() * &design_2;

    let transform = scatter_2.transpose() * (-1.0 * scatter_3.try_inverse().unwrap()); 
    let matrix_1 = scatter_1 + transform * scatter_2;

    let constraint_matrix = Matrix3::<f64>::new(0.0, 0.0, 2.0, 0.0, -1.0, 0.0, 2.0, 0.0, 0.0);
    let matrix_2 = matrix_1 * constraint_matrix.try_inverse().unwrap();

    let mut find_eigenvalues = matrix_2.hessenberg().h();
    let n = find_eigenvalues.nrows();
    for _ in 0..max_iter {
        let shift = *find_eigenvalues.index((n-1, n-1)) * DMatrix::<f64>::identity(n, n);
        let qr = (find_eigenvalues - &shift).qr();
        find_eigenvalues = qr.r() * qr.q() + &shift;
    }

    let eigenvalue = find_eigenvalues.diagonal().iter().copied().fold(f64::NEG_INFINITY, f64::max);

    let mut eigenvector = Vector3::from_element(1.0).normalize();
    let a_minus_lambda = matrix_2.transpose() - eigenvalue * Matrix3::identity();
    let inverse_iteration = a_minus_lambda.try_inverse();
    let inverse_iteration = match inverse_iteration {
        Some(matrix) => matrix,
        None => a_minus_lambda.pseudo_inverse(f64::MIN_POSITIVE).unwrap()
    };

    for _ in 0..max_iter {
        eigenvector = inverse_iteration * eigenvector;
        eigenvector.normalize_mut();
    }

    let coefficients_1 = eigenvector;
    let coefficients_2 = transform.transpose() * coefficients_1;    
    let mut coefficients = Vector6::zeros();
    coefficients.fixed_rows_mut::<3>(0).copy_from(&coefficients_1);
    coefficients.fixed_rows_mut::<3>(3).copy_from(&coefficients_2);

    let [a, mut b, c, mut d, mut f, g] = coefficients.data.0[0];
    b /= 2.0;
    d /= 2.0;
    f /= 2.0;

    let denominator = b.powf(2.0) - a*c;    
    if denominator > 0.0 {
        let placeholder: Vec<T> = vec![T::from_f64(-1.0); 4];
        return placeholder
    }

    let numerator = 2.0 * (a*f.powf(2.0) + c*d.powf(2.0) + g*b.powf(2.0) - 2.0*b*d*f - a*c*g);
    let factor = ((a - c).powf(2.0) + 4.0*b.powf(2.0)).sqrt();
    let mut axis_length_major = (numerator / denominator / (factor - a - c)).sqrt();
    let mut axis_length_minor = (numerator / denominator / (-factor - a - c)).sqrt();

    let mut width_gt_height = true;
    if axis_length_major < axis_length_minor {
        width_gt_height = false;
        std::mem::swap(&mut axis_length_major, &mut axis_length_minor);
    }

    let mut r = (axis_length_minor/axis_length_major).powf(2.0);
    r = if r > 1.0 { 1.0 / r } else { r };
    let eccentricity = (1.0 - r).sqrt();

    let mut phi = if b == 0.0 {
        if a < c { 0.0 } else { std::f64::consts::PI / 2.0 }
    } else {
        let mut inner = ((2.0*b) / (a - c)).atan() / 2.0;
        inner += if a > c { std::f64::consts::PI / 2.0 } else { 0.0 };
        inner
    };

    phi += if !width_gt_height { std::f64::consts::PI / 2.0 } else { 0.0 };
    phi %= std::f64::consts::PI;

    let output = vec![
        T::from_f64(axis_length_major) * T::two(),
        T::from_f64(axis_length_minor) * T::two(),
        T::from_f64(eccentricity),
        T::from_f64(phi)
    ];
    
    output
}
