use image::Luma;

use crate::types::Image;

/// Compute the raw moments of a binary image
///
/// # Arguments
///
/// * `img` - A binary image
/// 
/// # Examples
///
/// ```no_run
/// use fqmv_core::utils::toy;
/// use fqmv_core::descriptors::moments::moments_raw;
/// let img = toy::gray_image();
/// let moments = moments_raw(&img);
/// ```
///
/// # References
///
/// * https://en.wikipedia.org/wiki/Image_moment
pub fn moments_raw(mask: &Image<Luma<u8>>) -> Vec<f64> {
    let mut m00 = 0.0;
    let mut m10 = 0.0;
    let mut m01 = 0.0;
    let mut m11 = 0.0;
    let mut m20 = 0.0;
    let mut m02 = 0.0;
    let mut m12 = 0.0;
    let mut m21 = 0.0;
    let mut m30 = 0.0;
    let mut m03 = 0.0;

    for y in 0..mask.height() {
        for x in 0..mask.width() {
            let pixel = mask.get_pixel(x, y);
            if pixel[0] > 0 {
                let xa = x as f64;
                let xb = xa * xa;
                let xc = xb * xa;
                let ya = y as f64;
                let yb = ya * ya;
                let yc = yb * ya;

                m00 += pixel[0] as f64;
                m10 += xa * pixel[0] as f64;
                m01 += ya * pixel[0] as f64;
                m11 += xa * ya * pixel[0] as f64;
                m20 += xb * pixel[0] as f64;
                m02 += yb * pixel[0] as f64;
                m21 += xb * ya * pixel[0] as f64;
                m12 += xa * yb * pixel[0] as f64;
                m30 += xc * pixel[0] as f64;
                m03 += yc * pixel[0] as f64;
            }
        }
    }

    vec![ 
        m00, m10,
        m01, m11,
        m20, m02,
        m21, m12,
        m30, m03
    ]
}

/// Compute the central moments of a binary image
///
/// # Arguments
///
/// * `img` - A binary image
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::utils::toy;
/// use fqmv_core::descriptors::moments::moments_central;
/// let img = toy::gray_image();
/// let central_moments = moments_central(&img);
/// ```
///
/// # References
///
/// * https://en.wikipedia.org/wiki/Image_moment
pub fn moments_central(mask: &Image<Luma<u8>>) -> Vec<f64> {
    let raw_moments = moments_raw(mask);
    let m00 = raw_moments[0];
    let m10 = raw_moments[1];
    let m01 = raw_moments[2];
    let m11 = raw_moments[3];
    let m20 = raw_moments[4];
    let m02 = raw_moments[5];
    let m21 = raw_moments[6];
    let m12 = raw_moments[7];
    let m30 = raw_moments[8];
    let m03 = raw_moments[9];

    if m00 == 0.0 {
        return vec![0.0; 10];
    }

    let x = m10 / m00;
    let y = m01 / m00;

    let u00 = m00;
    let u10 = 0.0;
    let u01 = 0.0;
    let u11 = m11 - x*m01;
    let u20 = m20 - x*m10;
    let u02 = m02 - y*m01;
    let u21 = m21 - 2.0*x*m11 - y*m20 + 2.0*x*x*m01;
    let u12 = m12 - 2.0*y*m11 - x*m02 + 2.0*y*y*m10;
    let u30 = m30 - 3.0*x*m20 + 2.0*x*x*m10;
    let u03 = m03 - 3.0*y*m02 + 2.0*y*y*m01;

    vec![
        u00, u10,
        u01, u11,
        u20, u02,
        u21, u12,
        u30, u03
    ]
}

/// Compute the Hu moments of a binary image
///
/// # Arguments
///
/// * `img` - A binary image
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::utils::toy;
/// use fqmv_core::descriptors::moments::moments_hu;
/// let img = toy::gray_image();
/// let hu_moments = moments_hu(&img);
/// ```
///
/// # References
///
/// * https://en.wikipedia.org/wiki/Image_moment
pub fn moments_hu(mask: &Image<Luma<u8>>) -> Vec<f64> {
    let central_moments = moments_central(mask);
    let u00 = central_moments[0];
    let u20 = central_moments[4];
    let u02 = central_moments[5];
    let u11 = central_moments[3];
    let u30 = central_moments[8];
    let u03 = central_moments[9];
    let u21 = central_moments[6];
    let u12 = central_moments[7];

    if u00 == 0.0 {
        return vec![0.0; 7];
    }

    let s2 = u00 * u00;
    let s3 = u00.powf(2.5);

    let n20 = u20 / s2;
    let n02 = u02 / s2;
    let n11 = u11 / s2;
    let n30 = u30 / s3;
    let n03 = u03 / s3;
    let n21 = u21 / s3;
    let n12 = u12 / s3;

    let p = n20 - n02;
    let q = n30 - 3.0*n12;
    let r = n30 + n12;
    let z = n21 + n03;
    let y = 3.0*n21 - n03;

    let i1 = n20 + n02;
    let i2 = p*p + 4.0*n11*n11;
    let i3 = q*q + y*y;
    let i4 = r*r + z*z;
    let i5 = q*r*(r*r - 3.0*z*z) + y*z*(3.0*r*r - z*z);
    let i6 = p*(r*r - z*z) + 4.0*n11*r*z;
    let i7 = y*r*(r*r - 3.0*z*z) - q*z*(3.0*r*r - z*z);

    vec![i1, i2, i3, i4, i5, i6, i7]
}

/// Non-redundant computation of all binary descriptors
///
/// # Arguments
///
/// * `img` - A binary image
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::utils::toy;
/// use fqmv_core::descriptors::moments::moments_descriptors;
/// let img = toy::gray_image();
/// let moments_descriptors = moments_descriptors(&img);
/// ```
pub fn moments_descriptors(mask: &Image<Luma<u8>>) -> Vec<f64> {
    let mut m00 = 0.0;
    let mut m10 = 0.0;
    let mut m01 = 0.0;
    let mut m11 = 0.0;
    let mut m20 = 0.0;
    let mut m02 = 0.0;
    let mut m12 = 0.0;
    let mut m21 = 0.0;
    let mut m30 = 0.0;
    let mut m03 = 0.0;
    
    for y in 0..mask.height() {
        for x in 0..mask.width() {
            let pixel = mask.get_pixel(x, y);
            if pixel[0] > 0 {
                let xa = x as f64;
                let xb = xa * xa;
                let xc = xb * xa;
                let ya = y as f64;
                let yb = ya * ya;
                let yc = yb * ya;

                m00 += pixel[0] as f64;
                m10 += xa * pixel[0] as f64;
                m01 += ya * pixel[0] as f64;
                m11 += xa * ya * pixel[0] as f64;
                m20 += xb * pixel[0] as f64;
                m02 += yb * pixel[0] as f64;
                m21 += xb * ya * pixel[0] as f64;
                m12 += xa * yb * pixel[0] as f64;
                m30 += xc * pixel[0] as f64;
                m03 += yc * pixel[0] as f64;
            }
        }
    }

    if m00 == 0.0 {
        return vec![0.0; 24];
    }

    let x = m10 / m00;
    let y = m01 / m00;
    
    let u00 = m00;
    let u11 = m11 - x*m01;
    let u20 = m20 - x*m10;
    let u02 = m02 - y*m01;
    let u21 = m21 - 2.0*x*m11 - y*m20 + 2.0*x*x*m01;
    let u12 = m12 - 2.0*y*m11 - x*m02 + 2.0*y*y*m10;
    let u30 = m30 - 3.0*x*m20 + 2.0*x*x*m10;
    let u03 = m03 - 3.0*y*m02 + 2.0*y*y*m01;
    
    let s2 = u00 * u00;
    let s3 = u00.powf(2.5);

    let n20 = u20 / s2;
    let n02 = u02 / s2;
    let n11 = u11 / s2;
    let n30 = u30 / s3;
    let n03 = u03 / s3;
    let n21 = u21 / s3;
    let n12 = u12 / s3;
    
    let p = n20 - n02;
    let q = n30 - 3.0*n12;
    let r = n30 + n12;
    let z = n21 + n03;
    let y = 3.0*n21 - n03;

    let i1 = n20 + n02;
    let i2 = p*p + 4.0*n11*n11;
    let i3 = q*q + y*y;
    let i4 = r*r + z*z;
    let i5 = q*r*(r*r - 3.0*z*z) + y*z*(3.0*r*r - z*z);
    let i6 = p*(r*r - z*z) + 4.0*n11*r*z;
    let i7 = y*r*(r*r - 3.0*z*z) - q*z*(3.0*r*r - z*z);
    
    vec![
        m00, m10, m01, m11, m20, m02, m21, m12, m30, m03,
        u11, u20, u02, u21, u12, u30, u03,
        i1, i2, i3, i4, i5, i6, i7
    ]
}
