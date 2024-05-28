use pyo3::prelude::*;
use fqmv_core::descriptors::moments;

use crate::utils::to_gray;

/// Compute the moments descriptors for a grayscale image
///
/// Parameters
/// ----------
/// image : Union[np.ndarray, list]
///     A (H, W) grayscale image
///
/// Returns
/// -------
/// list
///     A list of moments descriptors
#[pyfunction]
pub fn moments_descriptors(image: Vec<Vec<u8>>) -> Vec<f64> {
    moments::moments_descriptors(&to_gray(image))
}

/// Compute the raw moments for a grayscale image
///
/// Parameters
/// ----------
/// image : Union[np.ndarray, list]
///     A (H, W) grayscale image
///
/// Returns
/// -------
/// list
///     A list of raw moments
#[pyfunction]
pub fn moments_raw(image: Vec<Vec<u8>>) -> Vec<f64> {
    moments::moments_raw(&to_gray(image))
}

/// Compute the central moments for a grayscale image
///
/// Parameters
/// ----------
/// image : Union[np.ndarray, list]
///     A (H, W) grayscale image
///
/// Returns
/// -------
/// list
///     A list of central moments
#[pyfunction]
pub fn moments_central(image: Vec<Vec<u8>>) -> Vec<f64> {
    moments::moments_central(&to_gray(image))
}

/// Compute the Hu moments for a grayscale image
///
/// Parameters
/// ----------
/// image : Union[np.ndarray, list]
///     A (H, W) grayscale image
///
/// Returns
/// -------
/// list
///     A list of Hu moments
#[pyfunction]
pub fn moments_hu(image: Vec<Vec<u8>>) -> Vec<f64> {
    moments::moments_hu(&to_gray(image))
}
