use pyo3::prelude::*;
use fqmv_core::descriptors::zernike;

use crate::utils::to_gray;

/// Compute the first 30 Zernike moments of a grayscale image
///
/// Parameters
/// ----------
/// image : Union[np.ndarray, list]
///     A (H, W) grayscale image
#[pyfunction]
#[pyo3(signature = (image, center=false))]
pub fn zernike_descriptors(image: Vec<Vec<u8>>, center: Option<bool>) -> Vec<f64> {
    zernike::zernike_descriptors(&to_gray(image), center)
}
