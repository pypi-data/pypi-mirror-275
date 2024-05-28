use image::Luma;

use crate::types::Image;
use crate::utils::matrix::Matrix;
use crate::features::glcm;

/// Calculate energy from gray level co-occurrence matrix
/// ∑ i=1->N ∑ j=1->N p(i,j)^2
///
/// # Arguments
///
/// * `glcm` - Gray level co-occurrence matrix
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::{features::glcm, descriptors::texture::texture_energy};
/// let img = image::open("path/to/image").unwrap().to_luma8();
/// let comatrix = glcm(&img, 1.0, 0.0, 17, true, false, false);
/// let energy = texture_energy(&comatrix);
/// ```
pub fn texture_energy(glcm: &Matrix) -> f64 {
    let r = glcm.sum();
    let pij = glcm.divide(r);
    pij.data.iter().fold(0.0, |acc, &x| acc + x * x)
}

/// Calculate contrast from gray level co-occurrence matrix
/// ∑ i=1->N ∑ j=1->N (i-j) * p(i,j)
///
/// # Arguments
///
/// * `glcm` - Gray level co-occurrence matrix
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::{features::glcm, descriptors::texture::texture_contrast};
/// let img = image::open("path/to/image").unwrap().to_luma8();
/// let comatrix = glcm(&img, 1.0, 0.0, 17, true, false, false);
/// let contrast = texture_contrast(&comatrix);
/// ```
pub fn texture_contrast(glcm: &Matrix) -> f64 {
    let r = glcm.sum();
    let pij = glcm.divide(r);
    
    let mut contrast = 0.0;
    for i in 0..pij.rows {
        for j in 0..pij.cols {
            let i_minus_j = i as f64 - j as f64;
            contrast += i_minus_j * i_minus_j * pij[(i, j)];
        }
    }
    contrast
}

/// Calculate correlation from gray level co-occurrence matrix
/// ∑ i=1->N ∑ j=1->N (i - ux) * (j - uy) * p(i,j) / (sx * sy)
///
/// # Arguments
///
/// * `glcm` - Gray level co-occurrence matrix
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::{features::glcm, descriptors::texture::texture_correlation};
/// let img = image::open("path/to/image").unwrap().to_luma8();
/// let comatrix = glcm(&img, 1.0, 0.0, 17, true, false, false);
/// let correlation = texture_correlation(&comatrix);
/// ```
pub fn texture_correlation(glcm: &Matrix) -> f64 {
    let r = glcm.sum();
    let pij = glcm.divide(r);
    let px = pij.row_sum();
    let py = pij.col_sum();
    
    let ux = px
        .iter()
        .enumerate()
        .fold(0.0, |acc, (i, &x)| acc + ((i as f64 + 1.0) * x));
    
    let uy = py
        .iter()
        .enumerate()
        .fold(0.0, |acc, (i, &y)| acc + ((i as f64 + 1.0) * y));

    let sx = px
        .iter()
        .enumerate()
        .fold(0.0, |acc, (i, &x)| acc + (i as f64 + 1.0 - ux) * (i as f64 + 1.0 - ux) * x).sqrt();
    
    let sy = py
        .iter()
        .enumerate()
        .fold(0.0, |acc, (i, &y)| acc + (i as f64 + 1.0 - uy) * (i as f64 + 1.0 - uy) * y).sqrt();

    let mut correlation = 0.0;
    for i in 0..glcm.rows {
        for j in 0..glcm.cols {
            correlation += ((i as f64 + 1.0 - ux) * (j as f64 + 1.0 - uy) * pij[(i, j)])
                / (sx * sy);
        }
    }

    correlation
}

/// Calculate the sum of squares from gray level co-occurrence matrix
/// ∑ i=1->N ∑ j=1->N (i - u)^2 * p(i,j)
///
/// # Arguments
///
/// * `glcm` - Gray level co-occurrence matrix
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::{features::glcm, descriptors::texture::texture_sum_of_squares};
/// let img = image::open("path/to/image").unwrap().to_luma8();
/// let comatrix = glcm(&img, 1.0, 0.0, 17, true, false, false);
/// let sum_of_squares = texture_sum_of_squares(&comatrix);
/// ```
pub fn texture_sum_of_squares(glcm: &Matrix) -> f64 {
    let r = glcm.sum();
    let pij = glcm.divide(r);
    let px = pij.row_sum();
    
    let u = px
        .iter()
        .enumerate()
        .fold(0.0, |acc, (i, &x)| acc + ((i as f64 + 1.0) * x));
    
    let mut sum_of_squares = 0.0;
    for i in 0..glcm.rows {
        for j in 0..glcm.cols {
            sum_of_squares += (i as f64 + 1.0 - u) * (i as f64 + 1.0 - u) * pij[(i, j)];
        }
    }

    sum_of_squares
}

/// Calculate the inverse difference moment from gray level co-occurrence matrix
/// ∑ i=1->N ∑ j=1->N 1 / (1 + (i - j)^2) * p(i,j)
///
/// # Arguments
///
/// * `glcm` - Gray level co-occurrence matrix
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::{features::glcm, descriptors::texture::texture_inverse_difference};
/// let img = image::open("path/to/image").unwrap().to_luma8();
/// let comatrix = glcm(&img, 1.0, 0.0, 17, true, false, false);
/// let inverse_difference_moment = texture_inverse_difference(&comatrix);
/// ```
pub fn texture_inverse_difference(glcm: &Matrix) -> f64 {
    let r = glcm.sum();
    let pij = glcm.divide(r);
    
    let mut inverse_difference_moment = 0.0;
    for i in 0..glcm.rows {
        for j in 0..glcm.cols {
            inverse_difference_moment += (1.0 / (1.0 + ((i as f64 - j as f64) * (i as f64 - j as f64))))
                * pij[(i, j)];
        }
    }

    inverse_difference_moment
}

/// Calculate the sum average from gray level co-occurrence matrix
/// ∑ k=2->2N k * ∑ i=1->N ∑ j=1->N p(i,j) * δ(i+j,k)
///
/// # Arguments
///
/// * `glcm` - Gray level co-occurrence matrix
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::{features::glcm, descriptors::texture::texture_sum_average};
/// let img = image::open("path/to/image").unwrap().to_luma8();
/// let comatrix = glcm(&img, 1.0, 0.0, 17, true, false, false);
/// let sum_average = texture_sum_average(&comatrix);
/// ```
pub fn texture_sum_average(glcm: &Matrix) -> f64 {
    let r = glcm.sum();
    let pij = glcm.divide(r);
    
    let mut px_plus_y = vec![0.0; 2 * glcm.rows];
    for i in 0..glcm.rows {
        for j in 0..glcm.cols {
            px_plus_y[i + j] += pij[(i, j)];
        }
    }

    let mut sum_average = 0.0;
    for k in 0..(2 * glcm.rows) {
        sum_average += k as f64 * px_plus_y[k];
    }

    sum_average
}

/// Calculate the sum variance from gray level co-occurrence matrix
/// ∑ k=2->2N (k - u_(x+y))^2 * ∑ i=1->N ∑ j=1->N p(i,j) * δ(i+j,k)
///
/// # Arguments
///
/// * `glcm` - Gray level co-occurrence matrix
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::{features::glcm, descriptors::texture::texture_sum_variance};
/// let img = image::open("path/to/image").unwrap().to_luma8();
/// let comatrix = glcm(&img, 1.0, 0.0, 17, true, false, false);
/// let sum_variance = texture_sum_variance(&comatrix);
/// ```
pub fn texture_sum_variance(glcm: &Matrix) -> f64 {
    let r = glcm.sum();
    let pij = glcm.divide(r);
    
    let mut px_plus_y = vec![0.0; 2 * glcm.rows];
    for i in 0..glcm.rows {
        for j in 0..glcm.cols {
            px_plus_y[i + j] += pij[(i, j)];
        }
    }

    let mut sum_average = 0.0;
    let mut sum_variance = 0.0;
    for k in 0..(2 * glcm.rows) {
        let px_plus_y_k = px_plus_y[k];
        sum_average += k as f64 * px_plus_y_k;
        sum_variance += (k as f64) * (k as f64) * px_plus_y_k;
    }

    sum_variance - sum_average * sum_average
}

/// Calculate the sum entropy from gray level co-occurrence matrix
/// -∑ k=2->2N p_x+y(k) * log(∑ i=1->N ∑ j=1->N p(i,j) * δ(i+j,k))
///
/// # Arguments
///
/// * `glcm` - Gray level co-occurrence matrix
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::{features::glcm, descriptors::texture::texture_sum_entropy};
/// let img = image::open("path/to/image").unwrap().to_luma8();
/// let comatrix = glcm(&img, 1.0, 0.0, 17, true, false, false);
/// let sum_entropy = texture_sum_entropy(&comatrix);
/// ```
pub fn texture_sum_entropy(glcm: &Matrix) -> f64 {
    let r = glcm.sum();
    let pij = glcm.divide(r);
    
    let mut px_plus_y = vec![0.0; 2 * glcm.rows];
    for i in 0..glcm.rows {
        for j in 0..glcm.cols {
            px_plus_y[i + j] += pij[(i, j)];
        }
    }

    let mut sum_entropy = 0.0;
    for k in 0..(2 * glcm.rows) {
        let px_plus_y_k = px_plus_y[k];

        let buffer = if px_plus_y_k <= f64::EPSILON {
            1.0
        } else {
            0.0
        };

        sum_entropy += px_plus_y[k] * (px_plus_y[k] + buffer).log2();
    }

    -sum_entropy
}

/// Calculate the entropy from gray level co-occurrence matrix
/// -∑ i=1->N ∑ j=1->N p(i,j) * log(p(i,j))
///
/// # Arguments
/// 
/// * `glcm` - Gray level co-occurrence matrix
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::{features::glcm, descriptors::texture::texture_entropy};
/// let img = image::open("path/to/image").unwrap().to_luma8();
/// let comatrix = glcm(&img, 1.0, 0.0, 17, true, false, false);
/// let entropy = texture_entropy(&comatrix);
/// ```
pub fn texture_entropy(glcm: &Matrix) -> f64 {
    let r = glcm.sum();
    let pij = glcm.divide(r);
    -pij.data.iter().fold(0.0, |acc, &x| acc + x * (x + f64::EPSILON).log2())
}

/// Calculate the difference variance from gray level co-occurrence matrix
/// ∑ k=0->N-1 (k - u_(x-y))^2 * ∑ i=1->N ∑ j=1->N p(i,j) * δ(i-j,k)
/// 
/// # Arguments
///
/// * `glcm` - Gray level co-occurrence matrix
///
/// # Note
///
/// To keep in line with previous work (e.g. mahotas), we compute the difference
/// variance as variance of p_|x-y| rather than |x-y| as in the original definition.
///
/// # Examples
/// 
/// ```no_run
/// use fqmv_core::{features::glcm, descriptors::texture::texture_difference_variance};
/// let img = image::open("path/to/image").unwrap().to_luma8();
/// let comatrix = glcm(&img, 1.0, 0.0, 17, true, false, false);
/// let difference_variance = texture_difference_variance(&comatrix);
/// ```
pub fn texture_difference_variance(glcm: &Matrix) -> f64 {
    let r = glcm.sum();
    let pij = glcm.divide(r);
    
    let mut px_minus_y = vec![0.0; glcm.rows];
    for i in 0..glcm.rows {
        for j in 0..glcm.cols {
            let index = (i as i32 - j as i32).abs() as usize;
            px_minus_y[index] += pij[(i, j)];
        }
    }

    let mean_x_minus_y = px_minus_y.iter().sum::<f64>() / px_minus_y.len() as f64;
    let variance = px_minus_y
        .iter()
        .enumerate()
        .fold(0.0, |acc, (_, &x)| acc + (x as f64 - mean_x_minus_y) * (x as f64 - mean_x_minus_y));
    variance / px_minus_y.len() as f64
}

/// Calculate the difference entropy from gray level co-occurrence matrix
/// -∑ k=0->N-1 p_x-y(k) * log(p_x-y(k))
/// # Arguments
///
/// * `glcm` - Gray level co-occurrence matrix
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::{features::glcm, descriptors::texture::texture_difference_entropy};
/// let img = image::open("path/to/image").unwrap().to_luma8();
/// let comatrix = glcm(&img, 1.0, 0.0, 17, true, false, false);
/// let difference_entropy = texture_difference_entropy(&comatrix);
/// ```
pub fn texture_difference_entropy(glcm: &Matrix) -> f64 {
    let r = glcm.sum();
    let pij = glcm.divide(r);
    
    let mut px_minus_y = vec![0.0; glcm.rows];
    for i in 0..glcm.rows {
        for j in 0..glcm.cols {
            let index = (i as i32 - j as i32).unsigned_abs() as usize;
            px_minus_y[index] += pij[(i, j)];
        }
    }

    -px_minus_y.iter().fold(0.0, |acc, &x| acc + x * (x + f64::EPSILON).log2())
}

/// Calculate the information measure of correlation 1 from gray level co-occurrence matrix
/// (HXY1 - HXY2) / max(HX, HY)
/// # Arguments
///
/// * `glcm` - Gray level co-occurrence matrix
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::{features::glcm, descriptors::texture::texture_infocorr_1};
/// let img = image::open("path/to/image").unwrap().to_luma8();
/// let comatrix = glcm(&img, 1.0, 0.0, 17, true, false, false);
/// let information_measure_of_correlation_1 = texture_infocorr_1(&comatrix);
/// ```
pub fn texture_infocorr_1(glcm: &Matrix) -> f64 {
    let r = glcm.sum();
    let pij = glcm.divide(r);
    let px = pij.row_sum();
    let py = pij.col_sum();
    
    let hx = -px.iter().fold(0.0, |acc, &x| acc + x * (x + f64::EPSILON).log2());
    let hy = -py.iter().fold(0.0, |acc, &y| acc + y * (y + f64::EPSILON).log2());

    let mut hxy1 = 0.0;
    let mut hxy2 = 0.0;
    for i in 0..glcm.rows {
        for j in 0..glcm.cols {
            hxy1 += pij[(i, j)] * (pij[(i, j)] + f64::EPSILON).log2();
            hxy2 += px[i] * py[j] * (px[i] * py[j] + f64::EPSILON).log2();
        }
    }

    (hxy2 - hxy1) / hx.max(hy)
}

/// Calculate the information measure of correlation 2 from gray level co-occurrence matrix
/// (1 - exp(-2 * (HXY1 - HXY2)))^0.5
///
/// # Arguments
///
/// * `glcm` - Gray level co-occurrence matrix
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::{features::glcm, descriptors::texture::texture_infocorr_2};
/// let img = image::open("path/to/image").unwrap().to_luma8();
/// let comatrix = glcm(&img, 1.0, 0.0, 17, true, false, false);
/// let information_measure_of_correlation_2 = texture_infocorr_2(&comatrix);
/// ```
pub fn texture_infocorr_2(glcm: &Matrix) -> f64 {
    let r = glcm.sum();
    let pij = glcm.divide(r);
    let px = pij.row_sum();
    let py = pij.col_sum();
    
    let mut hxy1 = 0.0;
    let mut hxy2 = 0.0;
    for i in 0..glcm.rows {
        for j in 0..glcm.cols {
            hxy1 += pij[(i, j)] * (pij[(i, j)] + f64::EPSILON).log2();
            hxy2 += px[i] * py[j] * (px[i] * py[j] + f64::EPSILON).log2();
        }
    }

    (1.0 - (-2.0 * (hxy1 - hxy2)).exp()).sqrt()
}

/// Non-redundant computation of all haralick features
///
/// # Arguments
///
/// * `glcm` - Gray level co-occurrence matrix
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::{features::glcm, descriptors::texture::haralick_features};
/// let img = image::open("path/to/image").unwrap().to_luma8();
/// let comatrix = glcm(&img, 1.0, 0.0, 17, true, false, false);
/// let descriptors = haralick_features(&comatrix);
/// ```
pub fn haralick_features(glcm: &Matrix) -> Vec<f64> {
    let r = glcm.sum();
    let pij = glcm.divide(r);

    let px = pij.row_sum();
    let py = pij.col_sum();

    let mut u = 0.0;
    let (mut ux, mut uy) = (0.0, 0.0);
    let (mut hx, mut hy) = (0.0, 0.0);

    for i in 0..px.len() {
        u = u + (i as f64 + 1.0) * px[i];
        ux = ux + (i as f64 + 1.0) * px[i];
        uy = uy + (i as f64 + 1.0) * py[i];
        hx = hx - px[i] * (px[i] + f64::EPSILON).log2();
        hy = hy - py[i] * (py[i] + f64::EPSILON).log2();
    }

    let sx = px
        .iter()
        .enumerate()
        .fold(0.0, |acc, (i, &x)| acc + (i as f64 + 1.0 - ux) * (i as f64 + 1.0 - ux) * x)
        .sqrt();

    let sy = py
        .iter()
        .enumerate()
        .fold(0.0, |acc, (i, &y)| acc + (i as f64 + 1.0 - uy) * (i as f64 + 1.0 - uy) * y)
        .sqrt();

    let mut hxy1 = 0.0;
    let mut hxy2 = 0.0;

    let mut px_plus_y = vec![0.0; 2 * glcm.rows];
    let mut px_minus_y = vec![0.0; glcm.rows];

    let mut energy = 0.0;
    let mut contrast = 0.0;
    let mut correlation = 0.0;
    let mut sum_of_squares = 0.0;
    let mut inverse_difference_moment = 0.0;
    let mut sum_average = 0.0;
    let mut sum_variance = 0.0;
    let mut sum_entropy = 0.0;
    let mut entropy = 0.0;
    let mut difference_variance = 0.0;
    let mut difference_entropy = 0.0;

    for i in 0..glcm.rows {
        for j in 0..glcm.cols {
            energy += pij[(i, j)] * pij[(i, j)];
            contrast += (i as f64 - j as f64) * (i as f64 - j as f64) * pij[(i, j)];

            correlation += ((i as f64 + 1.0 - ux) * (j as f64 + 1.0 - uy) * pij[(i, j)])
                / (sx * sy);

            sum_of_squares += (i as f64 + 1.0 - ux) * (i as f64 + 1.0 - ux) * pij[(i, j)];

            inverse_difference_moment += (1.0 / (1.0 + ((i as f64 - j as f64) * (i as f64 - j as f64))))
                * pij[(i, j)];

            entropy += pij[(i, j)] * (pij[(i, j)] + f64::EPSILON).log2();

            hxy1 += pij[(i, j)] * (pij[(i, j)] + f64::EPSILON).log2();
            hxy2 += px[i] * py[j] * (px[i] * py[j] + f64::EPSILON).log2();

            let index = (i as i32 - j as i32).unsigned_abs() as usize;
            px_minus_y[index] += pij[(i, j)];
            px_plus_y[i + j] += pij[(i, j)];
        }
    }

    for i in 0..(2 * glcm.rows) {
        let px_plus_y_k = px_plus_y[i];

        let k = i as f64;
        sum_average += k * px_plus_y_k;
        sum_variance += k * k * px_plus_y_k;

        let buffer = if px_plus_y_k <= f64::EPSILON { 1.0 } else { 0.0 };
        sum_entropy += px_plus_y_k * (px_plus_y_k + buffer).log2();
    }

    sum_variance -= sum_average * sum_average;

    let u_x_minus_y = px_minus_y.iter().sum::<f64>() / px_minus_y.len() as f64;

    for k in 0..glcm.rows {
        let px_minus_y_k = px_minus_y[k];
        difference_variance += (px_minus_y_k - u_x_minus_y) * (px_minus_y_k - u_x_minus_y);
        difference_entropy += px_minus_y_k * (px_minus_y_k + f64::EPSILON).log2();
    }

    difference_variance /= px_minus_y.len() as f64;

    let information_measure_of_correlation_1 = (hxy2 - hxy1) / hx.max(hy);
    let information_measure_of_correlation_2 = (1.0 - (-2.0 * (hxy1 - hxy2)).exp()).sqrt();

    vec![
        energy,
        contrast,
        correlation,
        sum_of_squares,
        inverse_difference_moment,
        sum_average,
        sum_variance,
        -sum_entropy,
        -entropy,
        difference_variance,
        -difference_entropy,
        information_measure_of_correlation_1,
        information_measure_of_correlation_2,
    ]
}

/// Compute texture descriptors from images
///
/// # Arguments
///
/// * `img` - DynamicImage
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::descriptors::texture::texture_descriptors;
/// let img = image::open("path/to/image").unwrap().to_luma8();
/// let descriptors = texture_descriptors(&img);
/// ```
pub fn texture_descriptors(img: &Image<Luma<u8>>) -> Vec<f64> {
    let mut haralick = vec![0.0; 13];
    for i in [0, 45, 90, 135].iter() {
         let comatrix = glcm(
            img, 1.0, *i as f32, 256, true, false, true
        );
        let features_i = haralick_features(&comatrix);
        for j in 0..features_i.len() {
            haralick[j] += features_i[j];
        }
    }

    haralick = haralick.iter().map(|x| x / 4.0).collect();

    haralick
}
