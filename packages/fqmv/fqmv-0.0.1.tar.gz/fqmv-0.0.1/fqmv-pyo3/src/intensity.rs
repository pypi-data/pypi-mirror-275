use pyo3::prelude::*;
use fqmv_core::descriptors::intensity;

use crate::utils::to_gray;

/// Compute intensity descriptors for a grayscale image
///
/// Parameters
/// ----------
/// image : Union[np.ndarray, list]
///     A (H, W) grayscale image
/// bins : int
///     Number of bins to use for the intensity histogram
/// with_zeros : bool
///     Whether to use zeros when computing the descriptors
/// with_max : float
///     Maximum intensity value to use for normalizing when computing the histogram descriptors
///
/// Returns
/// -------
/// list
///     A list of intensity descriptors
#[pyfunction]
#[pyo3(signature = (image, bins=256, with_zeros=false, with_max=255.0))]
pub fn intensity_descriptors(image: Vec<Vec<u8>>, bins: usize, with_zeros: bool, with_max: f64) -> Vec<f64> {
    let with_max = if !with_max.is_nan() { Some(with_max) } else { None };
    intensity::intensity_descriptors(&to_gray(image), bins, with_zeros, with_max)
}

/// Compute the maximum intensity value in a grayscale image
///
/// Parameters
/// ----------
/// image : Union[np.ndarray, list]
///     A (H, W) grayscale image
///
/// Returns
/// -------
/// float
///     The maximum intensity value
#[pyfunction]
pub fn intensity_maximum(image: Vec<Vec<u8>>) -> f64 {
    intensity::intensity_maximum(&to_gray(image))
}

/// Compute the minimum intensity value in a grayscale image
///
/// Parameters
/// ----------
/// image : Union[np.ndarray, list]
///     A (H, W) grayscale image
/// with_zeros : bool
///     Whether to include zeros when computing the minimum intensity value
///
/// Returns
/// -------
/// float
///     The minimum intensity value
#[pyfunction]
#[pyo3(signature = (image, with_zeros=false))]
pub fn intensity_minimum(image: Vec<Vec<u8>>, with_zeros: bool) -> f64 {
    intensity::intensity_minimum(&to_gray(image), with_zeros)
}

/// Compute the mean intensity value in a grayscale image
///
/// Parameters
/// ----------
/// image : Union[np.ndarray, list]
///     A (H, W) grayscale image
/// with_zeros : bool
///     Whether to include zeros when computing the mean intensity value
///
/// Returns
/// -------
/// float
///   The mean intensity value
#[pyfunction]
#[pyo3(signature = (image, with_zeros=false))]
pub fn intensity_mean<'py>(image: Vec<Vec<u8>>, with_zeros: bool) -> f64 {
    intensity::intensity_mean(&to_gray(image), with_zeros)
}

/// Compute the integrated intensity value in a grayscale image
///
/// Parameters
/// ----------
/// image : Union[np.ndarray, list]
///     A (H, W) grayscale image
///
/// Returns
/// -------
/// float
///     The integrated intensity value
#[pyfunction]
pub fn intensity_integrated(image: Vec<Vec<u8>>) -> f64 {
    intensity::intensity_integrated(&to_gray(image))
}

/// Compute the standard deviation of intensity values in a grayscale image
///
/// Parameters
/// ----------
/// image : Union[np.ndarray, list]
///     A (H, W) grayscale image
/// with_zeros : bool
///     Whether to include zeros when computing the standard deviation
///
/// Returns
/// -------
/// float
///     The standard deviation of intensity values
#[pyfunction]
#[pyo3(signature = (image, with_zeros=false))]
pub fn intensity_standard_deviation(image: Vec<Vec<u8>>, with_zeros: bool) -> f64 {
    intensity::intensity_standard_deviation(&to_gray(image), with_zeros)
}

/// Compute the median intensity value in a grayscale image
///
/// Parameters
/// ----------
/// image : Union[np.ndarray, list]
///     A (H, W) grayscale image
///
/// Returns
/// -------
/// float
///     The median intensity value
#[pyfunction]
#[pyo3(signature = (image, with_zeros=false))]
pub fn intensity_median(image: Vec<Vec<u8>>, with_zeros: bool) -> f64 {
    intensity::intensity_median(&to_gray(image), with_zeros)
}

/// Compute the median absolute deviation of intensity values in a grayscale image
///
/// Parameters
/// ----------
/// image : Union[np.ndarray, list]
///     A (H, W) grayscale image
/// with_zeros : bool
///     Whether to include zeros when computing the median absolute deviation
///
/// Returns
/// -------
/// float
///     The median absolute deviation of intensity values
#[pyfunction]
#[pyo3(signature = (image, with_zeros=false))]
pub fn intensity_median_absolute_deviation(image: Vec<Vec<u8>>, with_zeros: bool) -> f64 {
    intensity::intensity_median_absolute_deviation(&to_gray(image), with_zeros)
}

/// Compute the skewness of intensity values in a grayscale image
///
/// Parameters
/// ----------
/// image : Union[np.ndarray, list]
///     A (H, W) grayscale image
/// bins : int
///     Number of bins to use for the intensity histogram
/// with_zeros : bool
///     Whether to include zeros when computing the skewness
/// with_max : float
///     Maximum intensity value to use for normalizing when computing the skewness
///
/// Returns
/// -------
/// float
///     The skewness of intensity values
#[pyfunction]
#[pyo3(signature = (image, bins=256, with_zeros=false, with_max=255.0))]
pub fn intensity_histogram_skewness(image: Vec<Vec<u8>>, bins: usize, with_zeros: bool, with_max: f64) -> f64 {
    let with_max = if !with_max.is_nan() { Some(with_max) } else { None };
    intensity::intensity_histogram_skewness(&to_gray(image), bins, with_zeros, with_max)
}

/// Compute the kurtosis of intensity values in a grayscale image
///
/// Parameters
/// ----------
/// image : Union[np.ndarray, list]
///     A (H, W) grayscale image
/// bins : int
///     Number of bins to use for the intensity histogram
/// with_zeros : bool
///     Whether to include zeros when computing the kurtosis
/// with_max : float
///     Maximum intensity value to use for normalizing when computing the kurtosis
///
/// Returns
/// -------
/// float
///     The kurtosis of intensity values
#[pyfunction]
#[pyo3(signature = (image, bins=256, with_zeros=false, with_max=255.0))]
pub fn intensity_histogram_kurtosis(image: Vec<Vec<u8>>, bins: usize, with_zeros: bool, with_max: f64) -> f64 {
    let with_max = if !with_max.is_nan() { Some(with_max) } else { None };
    intensity::intensity_histogram_kurtosis(&to_gray(image), bins, with_zeros, with_max)
}
