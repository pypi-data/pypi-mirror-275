use pyo3::prelude::*;
use pyo3::types::PyAny;

use fqmv_core::descriptors::form;

// TO-DO: a bit difficult to write a generic over a closure with generics
// but it would reduce a lot of this unecessary if-else bloat if I have time 
// to write one

/// Compute morphometric descriptors for a polygon/set of points
///
/// Parameters
/// ----------
/// points : Union[np.ndarray, list]
///     A (N, 2) array of points
///
/// Returns
/// -------
/// list
///     A list of morphometric descriptors
#[pyfunction]
pub fn polygon_descriptors<'py>(points: Bound<'py, PyAny>) -> Vec<f64> {
    if let Ok(vec) = points.extract::<Vec<[u8; 2]>>() {
        form::polygon_descriptors::<u8>(&vec).iter().map(|&x| x as f64).collect()
    } else if let Ok(vec) = points.extract::<Vec<[u16; 2]>>() {
        form::polygon_descriptors::<u16>(&vec).iter().map(|&x| x as f64).collect()
    } else if let Ok(vec) = points.extract::<Vec<[u32; 2]>>() {
        form::polygon_descriptors::<u32>(&vec).iter().map(|&x| x as f64).collect()
    } else if let Ok(vec) = points.extract::<Vec<[i8; 2]>>() {
        form::polygon_descriptors::<i8>(&vec).iter().map(|&x| x as f64).collect()
    } else if let Ok(vec) = points.extract::<Vec<[i16; 2]>>() {
        form::polygon_descriptors::<i16>(&vec).iter().map(|&x| x as f64).collect()
    } else if let Ok(vec) = points.extract::<Vec<[i32; 2]>>() {
        form::polygon_descriptors::<i32>(&vec).iter().map(|&x| x as f64).collect()
    } else if let Ok(vec) = points.extract::<Vec<[i64; 2]>>() {
        form::polygon_descriptors::<i64>(&vec).iter().map(|&x| x as f64).collect()
    } else if let Ok(vec) = points.extract::<Vec<[u64; 2]>>() {
        form::polygon_descriptors::<u64>(&vec).iter().map(|&x| x as f64).collect()
    } else if let Ok(vec) = points.extract::<Vec<[f32; 2]>>() {
        form::polygon_descriptors::<f32>(&vec).iter().map(|&x| x as f64).collect()
    } else if let Ok(vec) = points.extract::<Vec<[f64; 2]>>() {
        form::polygon_descriptors::<f64>(&vec)
    } else {
        panic!("Invalid type/shape of input points. Must be one of u8, u16, u32, i8, i16, i32, f32, f64 with shape (N, 2)")
    }
}

/// Compute the area of a polygon
///
/// Parameters
/// ----------
/// points : Union[np.ndarray, list]
///     A (N, 2) array of points
///
/// Returns
/// -------
/// float
///     The area of the polygon
#[pyfunction]
pub fn polygon_area<'py>(points: Bound<'py, PyAny>) -> f64 {
    if let Ok(vec) = points.extract::<Vec<[u8; 2]>>() {
        form::polygon_area::<u8>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[u16; 2]>>() {
        form::polygon_area::<u16>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[u32; 2]>>() {
        form::polygon_area::<u32>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i8; 2]>>() {
        form::polygon_area::<i8>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i16; 2]>>() {
        form::polygon_area::<i16>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i32; 2]>>() {
        form::polygon_area::<i32>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i64; 2]>>() {
        form::polygon_area::<i64>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[u64; 2]>>() {
        form::polygon_area::<u64>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[f32; 2]>>() {
        form::polygon_area::<f32>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[f64; 2]>>() {
        form::polygon_area::<f64>(&vec) as f64
    } else {
        panic!("Invalid type/shape of input points. Must be one of u8, u16, u32, i8, i16, i32, f32, f64 with shape (N, 2)")
    }
}

/// Compute the area of the bounding box of a polygon
///
/// Parameters
/// ----------
/// points : Union[np.ndarray, list]
///     A (N, 2) array of points
///
/// Returns
/// -------
/// float
///     The area of the bounding box of the polygon
#[pyfunction]
pub fn polygon_area_bbox<'py>(points: Bound<'py, PyAny>) -> f64 {
    if let Ok(vec) = points.extract::<Vec<[u8; 2]>>() {
        form::polygon_area_bbox::<u8>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[u16; 2]>>() {
        form::polygon_area_bbox::<u16>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[u32; 2]>>() {
        form::polygon_area_bbox::<u32>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i8; 2]>>() {
        form::polygon_area_bbox::<i8>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i16; 2]>>() {
        form::polygon_area_bbox::<i16>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i32; 2]>>() {
        form::polygon_area_bbox::<i32>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i64; 2]>>() {
        form::polygon_area_bbox::<i64>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[u64; 2]>>() {
        form::polygon_area_bbox::<u64>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[f32; 2]>>() {
        form::polygon_area_bbox::<f32>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[f64; 2]>>() {
        form::polygon_area_bbox::<f64>(&vec) as f64
    } else {
        panic!("Invalid type/shape of input points. Must be one of u8, u16, u32, i8, i16, i32, f32, f64 with shape (N, 2)")
    }
}

/// Compute the area of the convex hull of a polygon
///
/// Parameters
/// ----------
/// points : Union[np.ndarray, list]
///     A (N, 2) array of points
///
/// Returns
/// -------
/// float
///     The area of the convex hull of the polygon
#[pyfunction]
pub fn polygon_area_convex<'py>(points: Bound<'py, PyAny>) -> f64 {
    if let Ok(vec) = points.extract::<Vec<[u8; 2]>>() {
        form::polygon_area_convex::<u8>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[u16; 2]>>() {
        form::polygon_area_convex::<u16>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[u32; 2]>>() {
        form::polygon_area_convex::<u32>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i8; 2]>>() {
        form::polygon_area_convex::<i8>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i16; 2]>>() {
        form::polygon_area_convex::<i16>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i32; 2]>>() {
        form::polygon_area_convex::<i32>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i64; 2]>>() {
        form::polygon_area_convex::<i64>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[u64; 2]>>() {
        form::polygon_area_convex::<u64>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[f32; 2]>>() {
        form::polygon_area_convex::<f32>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[f64; 2]>>() {
        form::polygon_area_convex::<f64>(&vec) as f64
    } else {
        panic!("Invalid type/shape of input points. Must be one of u8, u16, u32, i8, i16, i32, f32, f64 with shape (N, 2)")
    }
}

/// Compute the perimeter of a polygon
///
/// Parameters
/// ----------
/// points : Union[np.ndarray, list]
///     A (N, 2) array of points
///
/// Returns
/// -------
/// float
///     The perimeter of the polygon
#[pyfunction]
pub fn polygon_perimeter<'py>(points: Bound<'py, PyAny>) -> f64 {
    if let Ok(vec) = points.extract::<Vec<[u8; 2]>>() {
        form::polygon_perimeter::<u8>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[u16; 2]>>() {
        form::polygon_perimeter::<u16>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[u32; 2]>>() {
        form::polygon_perimeter::<u32>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i8; 2]>>() {
        form::polygon_perimeter::<i8>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i16; 2]>>() {
        form::polygon_perimeter::<i16>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i32; 2]>>() {
        form::polygon_perimeter::<i32>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i64; 2]>>() {
        form::polygon_perimeter::<i64>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[u64; 2]>>() {
        form::polygon_perimeter::<u64>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[f32; 2]>>() {
        form::polygon_perimeter::<f32>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[f64; 2]>>() {
        form::polygon_perimeter::<f64>(&vec) as f64
    } else {
        panic!("Invalid type/shape of input points. Must be one of u8, u16, u32, i8, i16, i32, f32, f64 with shape (N, 2)")
    }
}

/// Compute the elongation of a polygon
///
/// Parameters
/// ----------
/// points : Union[np.ndarray, list]
///     A (N, 2) array of points
///
/// Returns
/// -------
/// float
///     The elongation of the polygon
#[pyfunction]
pub fn polygon_elongation<'py>(points: Bound<'py, PyAny>) -> f64 {
    if let Ok(vec) = points.extract::<Vec<[u8; 2]>>() {
        form::polygon_elongation::<u8>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[u16; 2]>>() {
        form::polygon_elongation::<u16>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[u32; 2]>>() {
        form::polygon_elongation::<u32>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i8; 2]>>() {
        form::polygon_elongation::<i8>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i16; 2]>>() {
        form::polygon_elongation::<i16>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i32; 2]>>() {
        form::polygon_elongation::<i32>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i64; 2]>>() {
        form::polygon_elongation::<i64>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[u64; 2]>>() {
        form::polygon_elongation::<u64>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[f32; 2]>>() {
        form::polygon_elongation::<f32>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[f64; 2]>>() {
        form::polygon_elongation::<f64>(&vec) as f64
    } else {
        panic!("Invalid type/shape of input points. Must be one of u8, u16, u32, i8, i16, i32, f32, f64 with shape (N, 2)")
    }
}

/// Compute the thread length of a polygon
///
/// Parameters
/// ----------
/// points : Union[np.ndarray, list]
///     A (N, 2) array of points
///
/// Returns
/// -------
/// float
///     The thread length of the polygon
#[pyfunction]
pub fn polygon_thread_length<'py>(points: Bound<'py, PyAny>) -> f64 {
    if let Ok(vec) = points.extract::<Vec<[u8; 2]>>() {
        form::polygon_thread_length::<u8>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[u16; 2]>>() {
        form::polygon_thread_length::<u16>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[u32; 2]>>() {
        form::polygon_thread_length::<u32>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i8; 2]>>() {
        form::polygon_thread_length::<i8>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i16; 2]>>() {
        form::polygon_thread_length::<i16>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i32; 2]>>() {
        form::polygon_thread_length::<i32>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i64; 2]>>() {
        form::polygon_thread_length::<i64>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[u64; 2]>>() {
        form::polygon_thread_length::<u64>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[f32; 2]>>() {
        form::polygon_thread_length::<f32>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[f64; 2]>>() {
        form::polygon_thread_length::<f64>(&vec) as f64
    } else {
        panic!("Invalid type/shape of input points. Must be one of u8, u16, u32, i8, i16, i32, f32, f64 with shape (N, 2)")
    }
}

/// Compute the thread width of a polygon
///
/// Parameters
/// ----------
/// points : Union[np.ndarray, list]
///     A (N, 2) array of points
///
/// Returns
/// -------
/// float
///     The thread width of the polygon
#[pyfunction]
pub fn polygon_thread_width<'py>(points: Bound<'py, PyAny>) -> f64 {
    if let Ok(vec) = points.extract::<Vec<[u8; 2]>>() {
        form::polygon_thread_width::<u8>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[u16; 2]>>() {
        form::polygon_thread_width::<u16>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[u32; 2]>>() {
        form::polygon_thread_width::<u32>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i8; 2]>>() {
        form::polygon_thread_width::<i8>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i16; 2]>>() {
        form::polygon_thread_width::<i16>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i32; 2]>>() {
        form::polygon_thread_width::<i32>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i64; 2]>>() {
        form::polygon_thread_width::<i64>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[u64; 2]>>() {
        form::polygon_thread_width::<u64>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[f32; 2]>>() {
        form::polygon_thread_width::<f32>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[f64; 2]>>() {
        form::polygon_thread_width::<f64>(&vec) as f64
    } else {
        panic!("Invalid type/shape of input points. Must be one of u8, u16, u32, i8, i16, i32, f32, f64 with shape (N, 2)")
    }
}

/// Compute the solidity of a polygon
///
/// Parameters
/// ----------
/// points : Union[np.ndarray, list]
///     A (N, 2) array of points
///
/// Returns
/// -------
/// float
///     The solidity of the polygon
#[pyfunction]
pub fn polygon_solidity<'py>(points: Bound<'py, PyAny>) -> f64 {
    if let Ok(vec) = points.extract::<Vec<[u8; 2]>>() {
        form::polygon_solidity::<u8>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[u16; 2]>>() {
        form::polygon_solidity::<u16>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[u32; 2]>>() {
        form::polygon_solidity::<u32>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i8; 2]>>() {
        form::polygon_solidity::<i8>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i16; 2]>>() {
        form::polygon_solidity::<i16>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i32; 2]>>() {
        form::polygon_solidity::<i32>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i64; 2]>>() {
        form::polygon_solidity::<i64>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[u64; 2]>>() {
        form::polygon_solidity::<u64>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[f32; 2]>>() {
        form::polygon_solidity::<f32>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[f64; 2]>>() {
        form::polygon_solidity::<f64>(&vec) as f64
    } else {
        panic!("Invalid type/shape of input points. Must be one of u8, u16, u32, i8, i16, i32, f32, f64 with shape (N, 2)")
    }
}

/// Compute the compactness of a polygon
///
/// Parameters
/// ----------
/// points : Union[np.ndarray, list]
///     A (N, 2) array of points
///
/// Returns
/// -------
/// float
///     The compactness of the polygon
#[pyfunction]
pub fn polygon_extent<'py>(points: Bound<'py, PyAny>) -> f64 {
    if let Ok(vec) = points.extract::<Vec<[u8; 2]>>() {
        form::polygon_extent::<u8>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[u16; 2]>>() {
        form::polygon_extent::<u16>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[u32; 2]>>() {
        form::polygon_extent::<u32>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i8; 2]>>() {
        form::polygon_extent::<i8>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i16; 2]>>() {
        form::polygon_extent::<i16>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i32; 2]>>() {
        form::polygon_extent::<i32>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i64; 2]>>() {
        form::polygon_extent::<i64>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[u64; 2]>>() {
        form::polygon_extent::<u64>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[f32; 2]>>() {
        form::polygon_extent::<f32>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[f64; 2]>>() {
        form::polygon_extent::<f64>(&vec) as f64
    } else {
        panic!("Invalid type/shape of input points. Must be one of u8, u16, u32, i8, i16, i32, f32, f64 with shape (N, 2)")
    }
}

/// Compute the form factor of a polygon
///
/// Parameters
/// ----------
/// points : Union[np.ndarray, list]
///     A (N, 2) array of points
///
/// Returns
/// -------
/// float
///     The form factor of the polygon
#[pyfunction]
pub fn polygon_form_factor<'py>(points: Bound<'py, PyAny>) -> f64 {
    if let Ok(vec) = points.extract::<Vec<[u8; 2]>>() {
        form::polygon_form_factor::<u8>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[u16; 2]>>() {
        form::polygon_form_factor::<u16>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[u32; 2]>>() {
        form::polygon_form_factor::<u32>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i8; 2]>>() {
        form::polygon_form_factor::<i8>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i16; 2]>>() {
        form::polygon_form_factor::<i16>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i32; 2]>>() {
        form::polygon_form_factor::<i32>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i64; 2]>>() {
        form::polygon_form_factor::<i64>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[u64; 2]>>() {
        form::polygon_form_factor::<u64>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[f32; 2]>>() {
        form::polygon_form_factor::<f32>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[f64; 2]>>() {
        form::polygon_form_factor::<f64>(&vec) as f64
    } else {
        panic!("Invalid type/shape of input points. Must be one of u8, u16, u32, i8, i16, i32, f32, f64 with shape (N, 2)")
    }
}

/// Compute the eccentricity of a polygon
///
/// Parameters
/// ----------
/// points : Union[np.ndarray, list]
///     A (N, 2) array of points
///
/// Returns
/// -------
/// float
///     The eccentricity of the polygon
#[pyfunction]
pub fn polygon_eccentricity<'py>(points: Bound<'py, PyAny>) -> f64 {
    if let Ok(vec) = points.extract::<Vec<[u8; 2]>>() {
        form::polygon_eccentricity::<u8>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[u16; 2]>>() {
        form::polygon_eccentricity::<u16>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[u32; 2]>>() {
        form::polygon_eccentricity::<u32>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i8; 2]>>() {
        form::polygon_eccentricity::<i8>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i16; 2]>>() {
        form::polygon_eccentricity::<i16>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i32; 2]>>() {
        form::polygon_eccentricity::<i32>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i64; 2]>>() {
        form::polygon_eccentricity::<i64>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[u64; 2]>>() {
        form::polygon_eccentricity::<u64>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[f32; 2]>>() {
        form::polygon_eccentricity::<f32>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[f64; 2]>>() {
        form::polygon_eccentricity::<f64>(&vec) as f64
    } else {
        panic!("Invalid type/shape of input points. Must be one of u8, u16, u32, i8, i16, i32, f32, f64 with shape (N, 2)")
    }
}

/// Compute the major axis length of a polygon
///
/// Parameters
/// ----------
/// points : Union[np.ndarray, list]
///     A (N, 2) array of points
///
/// Returns
/// -------
/// float
///     The major axis length of the polygon
#[pyfunction]
pub fn polygon_major_axis_length<'py>(points: Bound<'py, PyAny>) -> f64 {
    if let Ok(vec) = points.extract::<Vec<[u8; 2]>>() {
        form::polygon_major_axis_length::<u8>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[u16; 2]>>() {
        form::polygon_major_axis_length::<u16>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[u32; 2]>>() {
        form::polygon_major_axis_length::<u32>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i8; 2]>>() {
        form::polygon_major_axis_length::<i8>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i16; 2]>>() {
        form::polygon_major_axis_length::<i16>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i32; 2]>>() {
        form::polygon_major_axis_length::<i32>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i64; 2]>>() {
        form::polygon_major_axis_length::<i64>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[u64; 2]>>() {
        form::polygon_major_axis_length::<u64>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[f32; 2]>>() {
        form::polygon_major_axis_length::<f32>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[f64; 2]>>() {
        form::polygon_major_axis_length::<f64>(&vec) as f64
    } else {
        panic!("Invalid type/shape of input points. Must be one of u8, u16, u32, i8, i16, i32, f32, f64 with shape (N, 2)")
    }
}

/// Compute the minor axis length of a polygon
///
/// Parameters
/// ----------
/// points : Union[np.ndarray, list]
///     A (N, 2) array of points
///
/// Returns
/// -------
/// float
///     The minor axis length of the polygon
#[pyfunction]
pub fn polygon_minor_axis_length<'py>(points: Bound<'py, PyAny>) -> f64 {
    if let Ok(vec) = points.extract::<Vec<[u8; 2]>>() {
        form::polygon_minor_axis_length::<u8>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[u16; 2]>>() {
        form::polygon_minor_axis_length::<u16>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[u32; 2]>>() {
        form::polygon_minor_axis_length::<u32>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i8; 2]>>() {
        form::polygon_minor_axis_length::<i8>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i16; 2]>>() {
        form::polygon_minor_axis_length::<i16>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i32; 2]>>() {
        form::polygon_minor_axis_length::<i32>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i64; 2]>>() {
        form::polygon_minor_axis_length::<i64>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[u64; 2]>>() {
        form::polygon_minor_axis_length::<u64>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[f32; 2]>>() {
        form::polygon_minor_axis_length::<f32>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[f64; 2]>>() {
        form::polygon_minor_axis_length::<f64>(&vec) as f64
    } else {
        panic!("Invalid type/shape of input points. Must be one of u8, u16, u32, i8, i16, i32, f32, f64 with shape (N, 2)")
    }
}

/// Compute the curl major of a polygon
///
/// Parameters
/// ----------
/// points : Union[np.ndarray, list]
///     A (N, 2) array of points
///
/// Returns
/// -------
/// float
///     The curl major of the polygon
#[pyfunction]
pub fn polygon_curl_major<'py>(points: Bound<'py, PyAny>) -> f64 {
    if let Ok(vec) = points.extract::<Vec<[u8; 2]>>() {
        form::polygon_curl_major::<u8>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[u16; 2]>>() {
        form::polygon_curl_major::<u16>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[u32; 2]>>() {
        form::polygon_curl_major::<u32>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i8; 2]>>() {
        form::polygon_curl_major::<i8>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i16; 2]>>() {
        form::polygon_curl_major::<i16>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i32; 2]>>() {
        form::polygon_curl_major::<i32>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i64; 2]>>() {
        form::polygon_curl_major::<i64>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[u64; 2]>>() {
        form::polygon_curl_major::<u64>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[f32; 2]>>() {
        form::polygon_curl_major::<f32>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[f64; 2]>>() {
        form::polygon_curl_major::<f64>(&vec) as f64
    } else {
        panic!("Invalid type/shape of input points. Must be one of u8, u16, u32, i8, i16, i32, f32, f64 with shape (N, 2)")
    }
}

/// Compute the curl bbox of a polygon
///
/// Parameters
/// ----------
/// points : Union[np.ndarray, list]
///     A (N, 2) array of points
///
/// Returns
/// -------
/// float
///     The curl bbox of the polygon
#[pyfunction]
pub fn polygon_curl_bbox<'py>(points: Bound<'py, PyAny>) -> f64 {
    if let Ok(vec) = points.extract::<Vec<[u8; 2]>>() {
        form::polygon_curl_bbox::<u8>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[u16; 2]>>() {
        form::polygon_curl_bbox::<u16>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[u32; 2]>>() {
        form::polygon_curl_bbox::<u32>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i8; 2]>>() {
        form::polygon_curl_bbox::<i8>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i16; 2]>>() {
        form::polygon_curl_bbox::<i16>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i32; 2]>>() {
        form::polygon_curl_bbox::<i32>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i64; 2]>>() {
        form::polygon_curl_bbox::<i64>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[u64; 2]>>() {
        form::polygon_curl_bbox::<u64>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[f32; 2]>>() {
        form::polygon_curl_bbox::<f32>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[f64; 2]>>() {
        form::polygon_curl_bbox::<f64>(&vec) as f64
    } else {
        panic!("Invalid type/shape of input points. Must be one of u8, u16, u32, i8, i16, i32, f32, f64 with shape (N, 2)")
    }
}

/// Compute the equivalent diameter of a polygon
///
/// Parameters
/// ----------
/// points : Union[np.ndarray, list]
///     A (N, 2) array of points
///
/// Returns
/// -------
/// float
///     The equivalent diameter of the polygon
#[pyfunction]
pub fn polygon_equivalent_diameter<'py>(points: Bound<'py, PyAny>) -> f64 {
    if let Ok(vec) = points.extract::<Vec<[u8; 2]>>() {
        form::polygon_equivalent_diameter::<u8>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[u16; 2]>>() {
        form::polygon_equivalent_diameter::<u16>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[u32; 2]>>() {
        form::polygon_equivalent_diameter::<u32>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i8; 2]>>() {
        form::polygon_equivalent_diameter::<i8>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i16; 2]>>() {
        form::polygon_equivalent_diameter::<i16>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i32; 2]>>() {
        form::polygon_equivalent_diameter::<i32>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i64; 2]>>() {
        form::polygon_equivalent_diameter::<i64>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[u64; 2]>>() {
        form::polygon_equivalent_diameter::<u64>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[f32; 2]>>() {
        form::polygon_equivalent_diameter::<f32>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[f64; 2]>>() {
        form::polygon_equivalent_diameter::<f64>(&vec) as f64
    } else {
        panic!("Invalid type/shape of input points. Must be one of u8, u16, u32, i8, i16, i32, f32, f64 with shape (N, 2)")
    }
}

/// Compute the minimum radius of a polygon
///
/// Parameters
/// ----------
/// points : Union[np.ndarray, list]
///     A (N, 2) array of points
///
/// Returns
/// -------
/// float
///     The minimum radius of the polygon
#[pyfunction]
pub fn polygon_minimum_radius<'py>(points: Bound<'py, PyAny>) -> f64 {
    if let Ok(vec) = points.extract::<Vec<[u8; 2]>>() {
        form::polygon_minimum_radius::<u8>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[u16; 2]>>() {
        form::polygon_minimum_radius::<u16>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[u32; 2]>>() {
        form::polygon_minimum_radius::<u32>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i8; 2]>>() {
        form::polygon_minimum_radius::<i8>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i16; 2]>>() {
        form::polygon_minimum_radius::<i16>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i32; 2]>>() {
        form::polygon_minimum_radius::<i32>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i64; 2]>>() {
        form::polygon_minimum_radius::<i64>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[u64; 2]>>() {
        form::polygon_minimum_radius::<u64>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[f32; 2]>>() {
        form::polygon_minimum_radius::<f32>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[f64; 2]>>() {
        form::polygon_minimum_radius::<f64>(&vec) as f64
    } else {
        panic!("Invalid type/shape of input points. Must be one of u8, u16, u32, i8, i16, i32, f32, f64 with shape (N, 2)")
    }
}

/// Compute the maximum radius of a polygon
///
/// Parameters
/// ----------
/// points : Union[np.ndarray, list]
///     A (N, 2) array of points
///
/// Returns
/// -------
/// float
///     The maximum radius of the polygon
#[pyfunction]
pub fn polygon_maximum_radius<'py>(points: Bound<'py, PyAny>) -> f64 {
    if let Ok(vec) = points.extract::<Vec<[u8; 2]>>() {
        form::polygon_maximum_radius::<u8>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[u16; 2]>>() {
        form::polygon_maximum_radius::<u16>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[u32; 2]>>() {
        form::polygon_maximum_radius::<u32>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i8; 2]>>() {
        form::polygon_maximum_radius::<i8>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i16; 2]>>() {
        form::polygon_maximum_radius::<i16>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i32; 2]>>() {
        form::polygon_maximum_radius::<i32>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i64; 2]>>() {
        form::polygon_maximum_radius::<i64>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[u64; 2]>>() {
        form::polygon_maximum_radius::<u64>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[f32; 2]>>() {
        form::polygon_maximum_radius::<f32>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[f64; 2]>>() {
        form::polygon_maximum_radius::<f64>(&vec) as f64
    } else {
        panic!("Invalid type/shape of input points. Must be one of u8, u16, u32, i8, i16, i32, f32, f64 with shape (N, 2)")
    }
}

/// Compute the mean radius of a polygon
///
/// Parameters
/// ----------
/// points : Union[np.ndarray, list]
///     A (N, 2) array of points
///
/// Returns
/// -------
/// float
///     The mean radius of the polygon
#[pyfunction]
pub fn polygon_mean_radius<'py>(points: Bound<'py, PyAny>) -> f64 {
    if let Ok(vec) = points.extract::<Vec<[u8; 2]>>() {
        form::polygon_mean_radius::<u8>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[u16; 2]>>() {
        form::polygon_mean_radius::<u16>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[u32; 2]>>() {
        form::polygon_mean_radius::<u32>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i8; 2]>>() {
        form::polygon_mean_radius::<i8>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i16; 2]>>() {
        form::polygon_mean_radius::<i16>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i32; 2]>>() {
        form::polygon_mean_radius::<i32>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i64; 2]>>() {
        form::polygon_mean_radius::<i64>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[u64; 2]>>() {
        form::polygon_mean_radius::<u64>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[f32; 2]>>() {
        form::polygon_mean_radius::<f32>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[f64; 2]>>() {
        form::polygon_mean_radius::<f64>(&vec) as f64
    } else {
        panic!("Invalid type/shape of input points. Must be one of u8, u16, u32, i8, i16, i32, f32, f64 with shape (N, 2)")
    }
}

/// Compute the maximum feret diameter of a polygon
///
/// Parameters
/// ----------
/// points : Union[np.ndarray, list]
///    A (N, 2) array of points
///
/// Returns
/// -------
/// float
///     The maximum feret diameter of the polygon
#[pyfunction]
pub fn polygon_feret_diameter_maximum<'py>(points: Bound<'py, PyAny>) -> f64 {
    if let Ok(vec) = points.extract::<Vec<[u8; 2]>>() {
        form::polygon_feret_diameter_maximum::<u8>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[u16; 2]>>() {
        form::polygon_feret_diameter_maximum::<u16>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[u32; 2]>>() {
        form::polygon_feret_diameter_maximum::<u32>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i8; 2]>>() {
        form::polygon_feret_diameter_maximum::<i8>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i16; 2]>>() {
        form::polygon_feret_diameter_maximum::<i16>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i32; 2]>>() {
        form::polygon_feret_diameter_maximum::<i32>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i64; 2]>>() {
        form::polygon_feret_diameter_maximum::<i64>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[u64; 2]>>() {
        form::polygon_feret_diameter_maximum::<u64>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[f32; 2]>>() {
        form::polygon_feret_diameter_maximum::<f32>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[f64; 2]>>() {
        form::polygon_feret_diameter_maximum::<f64>(&vec) as f64
    } else {
        panic!("Invalid type/shape of input points. Must be one of u8, u16, u32, i8, i16, i32, f32, f64 with shape (N, 2)")
    }
}

/// Compute the minimum feret diameter of a polygon
///
/// Parameters
/// ----------
/// points : Union[np.ndarray, list]
///     A (N, 2) array of points
///
/// Returns
/// -------
/// float
///     The minimum feret diameter of the polygon
#[pyfunction]
pub fn polygon_feret_diameter_minimum<'py>(points: Bound<'py, PyAny>) -> f64 {
    if let Ok(vec) = points.extract::<Vec<[u8; 2]>>() {
        form::polygon_feret_diameter_minimum::<u8>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[u16; 2]>>() {
        form::polygon_feret_diameter_minimum::<u16>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[u32; 2]>>() {
        form::polygon_feret_diameter_minimum::<u32>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i8; 2]>>() {
        form::polygon_feret_diameter_minimum::<i8>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i16; 2]>>() {
        form::polygon_feret_diameter_minimum::<i16>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i32; 2]>>() {
        form::polygon_feret_diameter_minimum::<i32>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[i64; 2]>>() {
        form::polygon_feret_diameter_minimum::<i64>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[u64; 2]>>() {
        form::polygon_feret_diameter_minimum::<u64>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[f32; 2]>>() {
        form::polygon_feret_diameter_minimum::<f32>(&vec) as f64
    } else if let Ok(vec) = points.extract::<Vec<[f64; 2]>>() {
        form::polygon_feret_diameter_minimum::<f64>(&vec) as f64
    } else {
        panic!("Invalid type/shape of input points. Must be one of u8, u16, u32, i8, i16, i32, f32, f64 with shape (N, 2)")
    }
}
