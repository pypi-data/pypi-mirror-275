use pyo3::prelude::*;
use fqmv_core::geometry::points;

/// Order points in an (N, 2) polygon in a clockwise or counterclockwise direction
#[pyfunction]
pub fn order_points_u8(points: Vec<[u8; 2]>) -> Vec<[u8; 2]> {
    points::order_points::<u8>(points)
}

/// Order points in an (N, 2) polygon in a clockwise or counterclockwise direction
#[pyfunction]
pub fn order_points_i32(points: Vec<[i32; 2]>) -> Vec<[i32; 2]> {
    points::order_points::<i32>(points)
}

/// Order points in an (N, 2) polygon in a clockwise or counterclockwise direction
#[pyfunction]
pub fn order_points_i64(points: Vec<[i64; 2]>) -> Vec<[i64; 2]> {
    points::order_points::<i64>(points)
}

/// Order points in an (N, 2) polygon in a clockwise or counterclockwise direction
#[pyfunction]
pub fn order_points_f32(points: Vec<[f32; 2]>) -> Vec<[f32; 2]> {
    points::order_points::<f32>(points)
}

/// Order points in an (N, 2) polygon in a clockwise or counterclockwise direction
#[pyfunction]
pub fn order_points_f64(points: Vec<[f64; 2]>) -> Vec<[f64; 2]> {
    points::order_points::<f64>(points)
}

/// Resample equidistant points along outline of an (N, 2) polygon
///
/// Parameters
/// ----------
/// points : Union[np.ndarray, list]
///     An (N, 2) array of points
/// n : int
///     The number of points to resample outline to
///
/// Returns
/// -------
/// list
///     A list of resampled points
#[pyfunction]
#[pyo3(signature = (points, n=64))]
pub fn resample_points_u8(points: Vec<[u8; 2]>, n: usize) -> Vec<[u8; 2]> {
    points::resample_points::<u8>(points, n)
}

/// Resample equidistant points along outline of an (N, 2) polygon
///
/// Parameters
/// ----------
/// points : Union[np.ndarray, list]
///     An (N, 2) array of points
/// n : int
///     The number of points to resample outline to
#[pyfunction]
#[pyo3(signature = (points, n=64))]
pub fn resample_points_i32(points: Vec<[i32; 2]>, n: usize) -> Vec<[i32; 2]> {
    points::resample_points::<i32>(points, n)
}

/// Resample equidistant points along outline of an (N, 2) polygon
///
/// Parameters
/// ----------
/// points : Union[np.ndarray, list]
///     An (N, 2) array of points
/// n : int
///     The number of points to resample outline to
///
/// Returns
/// -------
/// list
///     A list of resampled points
#[pyfunction]
#[pyo3(signature = (points, n=64))]
pub fn resample_points_i64(points: Vec<[i64; 2]>, n: usize) -> Vec<[i64; 2]> {
    points::resample_points::<i64>(points, n)
}

/// Resample equidistant points along outline of an (N, 2) polygon
///
/// Parameters
/// ----------
/// points : Union[np.ndarray, list]
///     An (N, 2) array of points
/// n : int
///     The number of points to resample outline to
///
/// Returns
/// -------
/// list
///     A list of resampled points
#[pyfunction]
#[pyo3(signature = (points, n=64))]
pub fn resample_points_f32(points: Vec<[f32; 2]>, n: usize) -> Vec<[f32; 2]> {
    points::resample_points::<f32>(points, n)
}

/// Resample equidistant points along outline of an (N, 2) polygon
///
/// Parameters
/// ----------
/// points : Union[np.ndarray, list]
///     An (N, 2) array of points
/// n : int
/// 
/// Returns
/// -------
/// list
///     A list of resampled points
#[pyfunction]
#[pyo3(signature = (points, n=64))]
pub fn resample_points_f64(points: Vec<[f64; 2]>, n: usize) -> Vec<[f64; 2]> {
    points::resample_points::<f64>(points, n)
}

/// Align a polygon to a reference polygon using Orthogonal procrustes
///
/// Parameters
/// ----------
/// points : Union[np.ndarray, list]
///     An (N, 2) array of f64 points
/// reference : Union[np.ndarray, list]
///     An (N, 2) array of f64 points
/// scale : bool
///     Whether to scale the points (remove scale variation)
///
/// Returns
/// -------
/// list
///     A list of aligned points
#[pyfunction]
#[pyo3(signature = (points, reference, scale=false))]
pub fn align_points_orthogonal(points: Vec<[f64; 2]>, reference: Vec<[f64; 2]>, scale: bool) -> Vec<[f64; 2]> {
    points::align_points_orthogonal(&points, &reference, scale)
}

/// Check if a point is inside a polygon
///
/// Parameters
/// ----------
/// point : Union[np.ndarray, list]
///     A [x, y] point to check
/// polygon : Union[np.ndarray, list]
///     An (N, 2) array of points defining the polygon
///
/// Returns
/// -------
/// bool
///     Whether the point is inside the polygon
#[pyfunction]
pub fn point_in_polygon_u8(point: [u8; 2], polygon: Vec<[u8; 2]>) -> bool {
    points::point_in_polygon::<u8>(&point, &polygon)
}

/// Check if a point is inside a polygon
///
/// Parameters
/// ----------
/// point : Union[np.ndarray, list]
///     A [x, y] point to check
/// polygon : Union[np.ndarray, list]
///     An (N, 2) array of points defining the polygon
///
/// Returns
/// -------
/// bool
///     Whether the point is inside the polygon

#[pyfunction]
pub fn point_in_polygon_i32(point: [i32; 2], polygon: Vec<[i32; 2]>) -> bool {
    points::point_in_polygon::<i32>(&point, &polygon)
}

/// Check if a point is inside a polygon
///
/// Parameters
/// ----------
/// point : Union[np.ndarray, list]
///     A [x, y] point to check
/// polygon : Union[np.ndarray, list]
///     An (N, 2) array of points defining the polygon
///
/// Returns
/// -------
/// bool
///     Whether the point is inside the polygon

#[pyfunction]
pub fn point_in_polygon_i64(point: [i64; 2], polygon: Vec<[i64; 2]>) -> bool {
    points::point_in_polygon::<i64>(&point, &polygon)
}

/// Check if a point is inside a polygon
///
/// Parameters
/// ----------
/// point : Union[np.ndarray, list]
///     A [x, y] point to check
/// polygon : Union[np.ndarray, list]
///     An (N, 2) array of points defining the polygon
///
/// Returns
/// -------
/// bool
///     Whether the point is inside the polygon

#[pyfunction]
pub fn point_in_polygon_f32(point: [f32; 2], polygon: Vec<[f32; 2]>) -> bool {
    points::point_in_polygon::<f32>(&point, &polygon)
}

/// Check if a point is inside a polygon
///
/// Parameters
/// ----------
/// point : Union[np.ndarray, list]
///     A [x, y] point to check
/// polygon : Union[np.ndarray, list]
///     An (N, 2) array of points defining the polygon
///
/// Returns
/// -------
/// bool
///     Whether the point is inside the polygon

#[pyfunction]
pub fn point_in_polygon_f64(point: [f64; 2], polygon: Vec<[f64; 2]>) -> bool {
    points::point_in_polygon::<f64>(&point, &polygon)
}
