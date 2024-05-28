use image::Luma;
use num::complex::Complex;

use crate::types::Image;
use crate::process::transform::center_mask;

fn radial_polynomial(n: usize, m: usize, r: &Vec<f64>) -> Vec<f64> {
    const FACT: [f64; 10] = [
        1.0, 1.0, 2.0, 6.0, 
        24.0, 120.0, 720.0, 
        5040.0, 40320.0, 
        362880.0
    ];
    
    let nf = n as f64;
    let nsm = (n - m) / 2;
    let nam = (n + m) / 2;

    let mut r_nm: Vec<f64> = Vec::with_capacity(r.len());
    for i in 0..r.len() {
        let mut r_nm_i = 0.0;
        for si in 0..=nsm {
            let sf = si as f64;
            let v = ((-1.0f64).powf(sf) * FACT[n - si])
                / (FACT[si] * FACT[nam - si] * FACT[nsm - si]);
            r_nm_i += v * r[i].powf(nf - 2.0 * sf);
        }

        r_nm.push(r_nm_i);
    }

    r_nm
}

fn zernike_polynomial(n: usize, m: usize, r: &Vec<f64>, theta: &Vec<f64>) -> Vec<Complex<f64>> {
    let complex_i = Complex::new(0.0, 1.0);
    let complex_m = Complex::new(m as f64, 0.0);
    let mut z_nm: Vec<Complex<f64>> = Vec::with_capacity(r.len());
    let r_nm = radial_polynomial(n, m, r);
    for i in 0..r.len() {
        let z_nm_i = Complex::new(r_nm[i], 0.0) 
            * (complex_i * complex_m * Complex::new(theta[i], 0.0)).exp();
        z_nm.push(z_nm_i);
    }

    z_nm
}

/// Compute the zernike moments for an image mask
///
/// # Arguments
///
/// * `mask` - A binary mask image
/// * `n` - Positive integer or zero
/// * `m` - Positive integer or zero
///
/// # Notes
///
/// The zernike moments are computed on scaled pixel values (image / image_sum)
/// but no image centering is performed. To get translation invariant moments,
/// center the image prior to computing the moments.
///
/// # References
///
/// 1. "Invariant Image Recognition by Zernike Moments". Khotanzad & Hong. 1988.
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::utils::toy;
/// use fqmv_core::descriptors::zernike::zernike_moments;
/// let mask = toy::gray_image();
/// let a_nm = zernike_moments(&mask, 3, 1);
/// ```
pub fn zernike_moments(mask: &Image<Luma<u8>>, n: usize, m: usize) -> Complex<f64> {
    let (width, height) = mask.dimensions();

    let half_width = width as f64 / 2.0;
    let half_height = height as f64 / 2.0;

    let mut r = vec![];
    let mut theta = vec![];
    let mut pixels = vec![];
    let mut total_mass = 0.0;

    for (x, y, pixel) in mask.enumerate_pixels() {
        let pixel = pixel.0[0] as f64;
        total_mass += pixel;

        let x = (x as f64 - half_width) / half_width;
        let y = (y as f64 - half_height) / half_height;
        let r_i = (x * x + y * y).sqrt();
        if r_i <= 1.0 {
            let theta_i = y.atan2(x);
            r.push(r_i);
            theta.push(theta_i);
            pixels.push(pixel);
        }
    }

    let z_nm = zernike_polynomial(n, m, &r, &theta);

    let mut a_nm = Complex::new(0.0, 0.0);
    for (i, z_nm_i) in z_nm.iter().enumerate() {
        a_nm += z_nm_i.conj() * Complex::new(pixels[i] as f64 / total_mass, 0.0);
    }

    a_nm = (Complex::new(n as f64 + 1.0, 0.0) * a_nm)
        / Complex::new(std::f64::consts::PI, 0.0);

    a_nm
}
    
/// Compute the zernike descriptors for a binary image mask
///
/// # Arguments
///
/// * `mask` - A binary mask image
/// * `center` - If true, center mask prior to computing the descriptors
///
/// # Notes
///
/// We only compute up to the 9th order zernike moments (n = 9, m = 0..9)
/// which is similar to what cellprofiler seems to do as per the measure
/// documentation.
///
/// # References
///
/// 1. "Invariant Image Recognition by Zernike Moments". Khotanzad & Hong. 1988.
/// 2. https://github.com/CellProfiler: We choose the max degree based
///    to be similar to the CellProfiler implementation.
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::utils::toy;
/// use fqmv_core::descriptors::zernike::zernike_descriptors;
/// let mask = toy::gray_image();
/// let descriptors = zernike_descriptors(&mask, None);
/// ```
pub fn zernike_descriptors(mask: &Image<Luma<u8>>, center: Option<bool>) -> Vec<f64> {
    let center = center.unwrap_or(false);
    let mask = if center {
        center_mask(&mask)
    } else {
        mask.to_owned()
    };

    let mut descriptors = vec![];
    for n in 0..=9 {
        for m in 0..=n {
            if (n - m) % 2 == 0 {
                let a_nm = zernike_moments(&mask, n, m);
                descriptors.push((a_nm.re.powi(2) + a_nm.im.powi(2)).sqrt());
            }
        }
    }

    descriptors
}
