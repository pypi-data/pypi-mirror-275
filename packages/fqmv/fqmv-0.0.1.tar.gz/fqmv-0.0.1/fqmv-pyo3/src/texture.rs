use pyo3::prelude::*;
use fqmv_core::features::glcm;
use fqmv_core::descriptors::texture;

use crate::utils::to_gray;

/// Compute texture descriptors (e.g. Haralick) for a grayscale image
///
/// Parameters
/// ----------
/// image : Union[np.ndarray, list]
///     A (H, W) grayscale image
///
/// Returns
/// -------
/// list
///     A list of texture descriptors
#[pyfunction]
pub fn texture_descriptors(image: Vec<Vec<u8>>) -> Vec<f64> {
    texture::texture_descriptors(&to_gray(image))
}

/// Compute the texture energy for a grayscale image
///
/// Parameters
/// ----------
/// image : Union[np.ndarray, list]
///     A (H, W) grayscale image
/// distance : float
///     Distance used to assign neighbours in comatrix
/// angle : float
///     Angle used to assign neighbours in comatrix
/// levels : int
///     Number of levels to build the comatrix
/// symmetric : bool
///     If True, make the comatrix symmetric
/// normalize : bool
///     If True, normalize the comatrix to sum to 1
/// rescale : bool
///     Rescample input image to the range (0, levels - 1.0)
///
/// Returns
/// -------
/// float
///     The texture energy
#[pyfunction]
#[pyo3(signature = (image, distance=1.0, angle=0.0, levels=256, symmetric=true, normalize=false, rescale=true))]
pub fn texture_energy(image: Vec<Vec<u8>>, distance: f32, angle: f32, levels: usize, symmetric: bool, normalize: bool, rescale: bool) -> f64 {
    let comatrix = glcm(&to_gray(image), distance, angle, levels, symmetric, normalize, rescale);
    texture::texture_energy(&comatrix)
}

/// Compute the texture contrast for a grayscale image
///
/// Parameters
/// ----------
/// image : Union[np.ndarray, list]
///     A (H, W) grayscale image
/// distance : float
///     Distance used to assign neighbours in comatrix
/// angle : float
///     Angle used to assign neighbours in comatrix
/// levels : int
///     Number of levels to build the comatrix
/// symmetric : bool
///     If True, make the comatrix symmetric
/// normalize : bool
///     If True, normalize the comatrix to sum to 1
/// rescale : bool
///     Rescample input image to the range (0, levels - 1.0)
///
/// Returns
/// -------
/// float
///     The texture contrast
#[pyfunction]
#[pyo3(signature = (image, distance=1.0, angle=0.0, levels=256, symmetric=true, normalize=false, rescale=true))]
pub fn texture_contrast(image: Vec<Vec<u8>>, distance: f32, angle: f32, levels: usize, symmetric: bool, normalize: bool, rescale: bool) -> f64 {
    let comatrix = glcm(&to_gray(image), distance, angle, levels, symmetric, normalize, rescale);
    texture::texture_contrast(&comatrix)
}

/// Compute the texture correlation for a grayscale image
///
/// Parameters
/// ----------
/// image : Union[np.ndarray, list]
///     A (H, W) grayscale image
/// distance : float
///     Distance used to assign neighbours in comatrix
/// angle : float
///     Angle used to assign neighbours in comatrix
/// levels : int
///     Number of levels to build the comatrix
/// symmetric : bool
///     If True, make the comatrix symmetric
/// normalize : bool
///     If True, normalize the comatrix to sum to 1
/// rescale : bool
///     Rescample input image to the range (0, levels - 1.0)
///
/// Returns
/// -------
/// float
///     The texture correlation
#[pyfunction]
#[pyo3(signature = (image, distance=1.0, angle=0.0, levels=256, symmetric=true, normalize=false, rescale=true))]
pub fn texture_correlation(image: Vec<Vec<u8>>, distance: f32, angle: f32, levels: usize, symmetric: bool, normalize: bool, rescale: bool) -> f64 {
    let comatrix = glcm(&to_gray(image), distance, angle, levels, symmetric, normalize, rescale);
    texture::texture_correlation(&comatrix)
}

/// Compute the texture sum of squares for a grayscale image
///
/// Parameters
/// ----------
/// image : Union[np.ndarray, list]
///     A (H, W) grayscale image
/// distance : float
///     Distance used to assign neighbours in comatrix
/// angle : float
///     Angle used to assign neighbours in comatrix
/// levels : int
///     Number of levels to build the comatrix
/// symmetric : bool
///     If True, make the comatrix symmetric
/// normalize : bool
///     If True, normalize the comatrix to sum to 1
/// rescale : bool
///     Rescample input image to the range (0, levels - 1.0)
///
/// Returns
/// -------
/// float
///     The texture sum of squares
#[pyfunction]
#[pyo3(signature = (image, distance=1.0, angle=0.0, levels=256, symmetric=true, normalize=false, rescale=true))]
pub fn texture_sum_of_squares(image: Vec<Vec<u8>>, distance: f32, angle: f32, levels: usize, symmetric: bool, normalize: bool, rescale: bool) -> f64 {
    let comatrix = glcm(&to_gray(image), distance, angle, levels, symmetric, normalize, rescale);
    texture::texture_sum_of_squares(&comatrix)
}

/// Compute the texture inverse difference for a grayscale image
///
/// Parameters
/// ----------
/// image : Union[np.ndarray, list]
///     A (H, W) grayscale image
/// distance : float
///     Distance used to assign neighbours in comatrix
/// angle : float
///     Angle used to assign neighbours in comatrix
/// levels : int
///     Number of levels to build the comatrix
/// symmetric : bool
///     If True, make the comatrix symmetric
/// normalize : bool
///     If True, normalize the comatrix to sum to 1
/// rescale : bool
///     Rescample input image to the range (0, levels - 1.0)
///
/// Returns
/// -------
/// float
///     The texture inverse difference
#[pyfunction]
#[pyo3(signature = (image, distance=1.0, angle=0.0, levels=256, symmetric=true, normalize=false, rescale=true))]
pub fn texture_inverse_difference(image: Vec<Vec<u8>>, distance: f32, angle: f32, levels: usize, symmetric: bool, normalize: bool, rescale: bool) -> f64 {
    let comatrix = glcm(&to_gray(image), distance, angle, levels, symmetric, normalize, rescale);
    texture::texture_inverse_difference(&comatrix)
}

/// Compute the texture sum average for a grayscale image
///
/// Parameters
/// ----------
/// image : Union[np.ndarray, list]
///     A (H, W) grayscale image
/// distance : float
///     Distance used to assign neighbours in comatrix
/// angle : float
///     Angle used to assign neighbours in comatrix
/// levels : int
///     Number of levels to build the comatrix
/// symmetric : bool
///     If True, make the comatrix symmetric
/// normalize : bool
///     If True, normalize the comatrix to sum to 1
/// rescale : bool
///     Rescample input image to the range (0, levels - 1.0)
///
/// Returns
/// -------
/// float
///     The texture sum average
#[pyfunction]
#[pyo3(signature = (image, distance=1.0, angle=0.0, levels=256, symmetric=true, normalize=false, rescale=true))]
pub fn texture_sum_average(image: Vec<Vec<u8>>, distance: f32, angle: f32, levels: usize, symmetric: bool, normalize: bool, rescale: bool) -> f64 {
    let comatrix = glcm(&to_gray(image), distance, angle, levels, symmetric, normalize, rescale);
    texture::texture_sum_average(&comatrix)
}

/// Compute the texture sum variance for a grayscale image
///
/// Parameters
/// ----------
/// image : Union[np.ndarray, list]
///     A (H, W) grayscale image
/// distance : float
///     Distance used to assign neighbours in comatrix
/// angle : float
///     Angle used to assign neighbours in comatrix
/// levels : int
///     Number of levels to build the comatrix
/// symmetric : bool
///     If True, make the comatrix symmetric
/// normalize : bool
///     If True, normalize the comatrix to sum to 1
/// rescale : bool
///     Rescample input image to the range (0, levels - 1.0)
///
/// Returns
/// -------
/// float
///     The texture sum variance
#[pyfunction]
#[pyo3(signature = (image, distance=1.0, angle=0.0, levels=256, symmetric=true, normalize=false, rescale=true))]
pub fn texture_sum_variance(image: Vec<Vec<u8>>, distance: f32, angle: f32, levels: usize, symmetric: bool, normalize: bool, rescale: bool) -> f64 {
    let comatrix = glcm(&to_gray(image), distance, angle, levels, symmetric, normalize, rescale);
    texture::texture_sum_variance(&comatrix)
}

/// Compute the texture sum entropy for a grayscale image
///
/// Parameters
/// ----------
/// image : Union[np.ndarray, list]
///     A (H, W) grayscale image
/// distance : float
///     Distance used to assign neighbours in comatrix
/// angle : float
///     Angle used to assign neighbours in comatrix
/// levels : int
///     Number of levels to build the comatrix
/// symmetric : bool
///     If True, make the comatrix symmetric
/// normalize : bool
///     If True, normalize the comatrix to sum to 1
/// rescale : bool
///     Rescample input image to the range (0, levels - 1.0)
///
/// Returns
/// -------
/// float
///     The texture sum entropy
#[pyfunction]
#[pyo3(signature = (image, distance=1.0, angle=0.0, levels=256, symmetric=true, normalize=false, rescale=true))]
pub fn texture_sum_entropy(image: Vec<Vec<u8>>, distance: f32, angle: f32, levels: usize, symmetric: bool, normalize: bool, rescale: bool) -> f64 {
    let comatrix = glcm(&to_gray(image), distance, angle, levels, symmetric, normalize, rescale);
    texture::texture_sum_entropy(&comatrix)
}

/// Compute the texture entropy for a grayscale image
///
/// Parameters
/// ----------
/// image : Union[np.ndarray, list]
///     A (H, W) grayscale image
/// distance : float
///     Distance used to assign neighbours in comatrix
/// angle : float
///     Angle used to assign neighbours in comatrix
/// levels : int
///     Number of levels to build the comatrix
/// symmetric : bool
///     If True, make the comatrix symmetric
/// normalize : bool
///     If True, normalize the comatrix to sum to 1
/// rescale : bool
///     Rescample input image to the range (0, levels - 1.0)
///
/// Returns
/// -------
/// float
///     The texture entropy
#[pyfunction]
#[pyo3(signature = (image, distance=1.0, angle=0.0, levels=256, symmetric=true, normalize=false, rescale=true))]
pub fn texture_entropy(image: Vec<Vec<u8>>, distance: f32, angle: f32, levels: usize, symmetric: bool, normalize: bool, rescale: bool) -> f64 {
    let comatrix = glcm(&to_gray(image), distance, angle, levels, symmetric, normalize, rescale);
    texture::texture_entropy(&comatrix)
}

/// Compute the texture difference variance for a grayscale image
///
/// Parameters
/// ----------
/// image : Union[np.ndarray, list]
///     A (H, W) grayscale image
/// distance : float
///     Distance used to assign neighbours in comatrix
/// angle : float
///     Angle used to assign neighbours in comatrix
/// levels : int
///     Number of levels to build the comatrix
/// symmetric : bool
///     If True, make the comatrix symmetric
/// normalize : bool
///     If True, normalize the comatrix to sum to 1
/// rescale : bool
///     Rescample input image to the range (0, levels - 1.0)
///
/// Returns
/// -------
/// float
///     The texture difference variance
#[pyfunction]
#[pyo3(signature = (image, distance=1.0, angle=0.0, levels=256, symmetric=true, normalize=false, rescale=true))]
pub fn texture_difference_variance(image: Vec<Vec<u8>>, distance: f32, angle: f32, levels: usize, symmetric: bool, normalize: bool, rescale: bool) -> f64 {
    let comatrix = glcm(&to_gray(image), distance, angle, levels, symmetric, normalize, rescale);
    texture::texture_difference_variance(&comatrix)
}

/// Compute the texture difference entropy for a grayscale image
///
/// Parameters
/// ----------
/// image : Union[np.ndarray, list]
///     A (H, W) grayscale image
/// distance : float
///     Distance used to assign neighbours in comatrix
/// angle : float
///     Angle used to assign neighbours in comatrix
/// levels : int
///     Number of levels to build the comatrix
/// symmetric : bool
///     If True, make the comatrix symmetric
/// normalize : bool
///     If True, normalize the comatrix to sum to 1
/// rescale : bool
///     Rescample input image to the range (0, levels - 1.0)
///
/// Returns
/// -------
/// float
///     The texture difference entropy
#[pyfunction]
#[pyo3(signature = (image, distance=1.0, angle=0.0, levels=256, symmetric=true, normalize=false, rescale=true))]
pub fn texture_difference_entropy(image: Vec<Vec<u8>>, distance: f32, angle: f32, levels: usize, symmetric: bool, normalize: bool, rescale: bool) -> f64 {
    let comatrix = glcm(&to_gray(image), distance, angle, levels, symmetric, normalize, rescale);
    texture::texture_difference_entropy(&comatrix)
}

/// Compute the texture information measure of correlation 1 for a grayscale image
///
/// Parameters
/// ----------
/// image : Union[np.ndarray, list]
///     A (H, W) grayscale image
/// distance : float
///     Distance used to assign neighbours in comatrix
/// angle : float
///     Angle used to assign neighbours in comatrix
/// levels : int
///     Number of levels to build the comatrix
/// symmetric : bool
///     If True, make the comatrix symmetric
/// normalize : bool
///     If True, normalize the comatrix to sum to 1
/// rescale : bool
///     Rescample input image to the range (0, levels - 1.0)
///
/// Returns
/// -------
/// float
///     The texture information measure of correlation 1
#[pyfunction]
#[pyo3(signature = (image, distance=1.0, angle=0.0, levels=256, symmetric=true, normalize=false, rescale=true))]
pub fn texture_infocorr_1(image: Vec<Vec<u8>>, distance: f32, angle: f32, levels: usize, symmetric: bool, normalize: bool, rescale: bool) -> f64 {
    let comatrix = glcm(&to_gray(image), distance, angle, levels, symmetric, normalize, rescale);
    texture::texture_infocorr_1(&comatrix)
}

/// Compute the texture information measure of correlation 2 for a grayscale image
///
/// Parameters
/// ----------
/// image : Union[np.ndarray, list]
///     A (H, W) grayscale image
/// distance : float
///     Distance used to assign neighbours in comatrix
/// angle : float
///     Angle used to assign neighbours in comatrix
/// levels : int
///     Number of levels to build the comatrix
/// symmetric : bool
///     If True, make the comatrix symmetric
/// normalize : bool
///     If True, normalize the comatrix to sum to 1
/// rescale : bool
///     Rescample input image to the range (0, levels - 1.0)
///
/// Returns
/// -------
/// float
///     The texture information measure of correlation 2
#[pyfunction]
#[pyo3(signature = (image, distance=1.0, angle=0.0, levels=256, symmetric=true, normalize=false, rescale=true))]
pub fn texture_infocorr_2(image: Vec<Vec<u8>>, distance: f32, angle: f32, levels: usize, symmetric: bool, normalize: bool, rescale: bool) -> f64 {
    let comatrix = glcm(&to_gray(image), distance, angle, levels, symmetric, normalize, rescale);
    texture::texture_infocorr_2(&comatrix)
}

/// Compute the Haralick features for a grayscale image
///
/// Parameters
/// ----------
/// image : Union[np.ndarray, list]
///     A (H, W) grayscale image
/// distance : float
///     Distance used to assign neighbours in comatrix
/// angle : float
///     Angle used to assign neighbours in comatrix
/// levels : int
///     Number of levels to build the comatrix
/// symmetric : bool
///     If True, make the comatrix symmetric
/// normalize : bool
///     If True, normalize the comatrix to sum to 1
/// rescale : bool
///     Rescample input image to the range (0, levels - 1.0)
///
/// Returns
/// -------
/// list
///     A list of the first 13 Haralick features
#[pyfunction]
#[pyo3(signature = (image, distance=1.0, angle=0.0, levels=256, symmetric=true, normalize=false, rescale=true))]
pub fn haralick_features(image: Vec<Vec<u8>>, distance: f32, angle: f32, levels: usize, symmetric: bool, normalize: bool, rescale: bool) -> Vec<f64> {
    let comatrix = glcm(&to_gray(image), distance, angle, levels, symmetric, normalize, rescale);
    texture::haralick_features(&comatrix)
}
