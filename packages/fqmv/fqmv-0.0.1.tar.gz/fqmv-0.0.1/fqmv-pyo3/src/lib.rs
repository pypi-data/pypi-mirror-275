use pyo3::prelude::*;

mod form;
mod intensity;
mod moments;
mod texture;
mod zernike;
mod utils;

mod geometry;

fn measure(parent: &Bound<'_, PyModule>) -> PyResult<()> {
    let measure = PyModule::new_bound(parent.py(), "measure")?;

    // Form
    measure.add_function(wrap_pyfunction!(form::polygon_descriptors, parent)?)?;
    measure.add_function(wrap_pyfunction!(form::polygon_area, parent)?)?;
    measure.add_function(wrap_pyfunction!(form::polygon_area_bbox, parent)?)?;
    measure.add_function(wrap_pyfunction!(form::polygon_area_convex, parent)?)?;
    measure.add_function(wrap_pyfunction!(form::polygon_elongation, parent)?)?;
    measure.add_function(wrap_pyfunction!(form::polygon_perimeter, parent)?)?;
    measure.add_function(wrap_pyfunction!(form::polygon_thread_length, parent)?)?;
    measure.add_function(wrap_pyfunction!(form::polygon_thread_width, parent)?)?;
    measure.add_function(wrap_pyfunction!(form::polygon_solidity, parent)?)?;
    measure.add_function(wrap_pyfunction!(form::polygon_extent, parent)?)?;
    measure.add_function(wrap_pyfunction!(form::polygon_form_factor, parent)?)?;
    measure.add_function(wrap_pyfunction!(form::polygon_eccentricity, parent)?)?;
    measure.add_function(wrap_pyfunction!(form::polygon_major_axis_length, parent)?)?;
    measure.add_function(wrap_pyfunction!(form::polygon_minor_axis_length, parent)?)?;
    measure.add_function(wrap_pyfunction!(form::polygon_curl_major, parent)?)?;
    measure.add_function(wrap_pyfunction!(form::polygon_curl_bbox, parent)?)?;
    measure.add_function(wrap_pyfunction!(form::polygon_equivalent_diameter, parent)?)?;
    measure.add_function(wrap_pyfunction!(form::polygon_minimum_radius, parent)?)?;
    measure.add_function(wrap_pyfunction!(form::polygon_maximum_radius, parent)?)?;
    measure.add_function(wrap_pyfunction!(form::polygon_mean_radius, parent)?)?;
    measure.add_function(wrap_pyfunction!(form::polygon_feret_diameter_maximum, parent)?)?;
    measure.add_function(wrap_pyfunction!(form::polygon_feret_diameter_minimum, parent)?)?;

    // Intensity
    measure.add_function(wrap_pyfunction!(intensity::intensity_descriptors, parent)?)?;
    measure.add_function(wrap_pyfunction!(intensity::intensity_maximum, parent)?)?;
    measure.add_function(wrap_pyfunction!(intensity::intensity_minimum, parent)?)?;
    measure.add_function(wrap_pyfunction!(intensity::intensity_mean, parent)?)?;
    measure.add_function(wrap_pyfunction!(intensity::intensity_integrated, parent)?)?;
    measure.add_function(wrap_pyfunction!(intensity::intensity_standard_deviation, parent)?)?;
    measure.add_function(wrap_pyfunction!(intensity::intensity_median, parent)?)?;
    measure.add_function(wrap_pyfunction!(intensity::intensity_median_absolute_deviation, parent)?)?;
    measure.add_function(wrap_pyfunction!(intensity::intensity_histogram_skewness, parent)?)?;
    measure.add_function(wrap_pyfunction!(intensity::intensity_histogram_kurtosis, parent)?)?;

    // Moments
    measure.add_function(wrap_pyfunction!(moments::moments_descriptors, parent)?)?;
    measure.add_function(wrap_pyfunction!(moments::moments_raw, parent)?)?;
    measure.add_function(wrap_pyfunction!(moments::moments_central, parent)?)?;
    measure.add_function(wrap_pyfunction!(moments::moments_hu, parent)?)?;

    // Texture
    measure.add_function(wrap_pyfunction!(texture::texture_descriptors, parent)?)?;
    measure.add_function(wrap_pyfunction!(texture::texture_energy, parent)?)?;
    measure.add_function(wrap_pyfunction!(texture::texture_contrast, parent)?)?;
    measure.add_function(wrap_pyfunction!(texture::texture_correlation, parent)?)?;
    measure.add_function(wrap_pyfunction!(texture::texture_sum_of_squares, parent)?)?;
    measure.add_function(wrap_pyfunction!(texture::texture_inverse_difference, parent)?)?;
    measure.add_function(wrap_pyfunction!(texture::texture_sum_average, parent)?)?;
    measure.add_function(wrap_pyfunction!(texture::texture_sum_variance, parent)?)?;
    measure.add_function(wrap_pyfunction!(texture::texture_sum_entropy, parent)?)?;
    measure.add_function(wrap_pyfunction!(texture::texture_entropy, parent)?)?;
    measure.add_function(wrap_pyfunction!(texture::texture_difference_variance, parent)?)?;
    measure.add_function(wrap_pyfunction!(texture::texture_difference_entropy, parent)?)?;
    measure.add_function(wrap_pyfunction!(texture::texture_infocorr_1, parent)?)?;
    measure.add_function(wrap_pyfunction!(texture::texture_infocorr_2, parent)?)?;
    measure.add_function(wrap_pyfunction!(texture::haralick_features, parent)?)?;

    // Zernike
    measure.add_function(wrap_pyfunction!(zernike::zernike_descriptors, parent)?)?;

    parent.add_submodule(&measure)?;
    Ok(())
}

fn geometry(parent: &Bound<'_, PyModule>) -> PyResult<()> {
    let geometry = PyModule::new_bound(parent.py(), "geometry")?;

    geometry.add_function(wrap_pyfunction!(geometry::order_points_u8, parent)?)?;
    geometry.add_function(wrap_pyfunction!(geometry::order_points_i32, parent)?)?;
    geometry.add_function(wrap_pyfunction!(geometry::order_points_i64, parent)?)?;
    geometry.add_function(wrap_pyfunction!(geometry::order_points_f32, parent)?)?;
    geometry.add_function(wrap_pyfunction!(geometry::order_points_f64, parent)?)?;
    geometry.add_function(wrap_pyfunction!(geometry::resample_points_u8, parent)?)?;
    geometry.add_function(wrap_pyfunction!(geometry::resample_points_i32, parent)?)?;
    geometry.add_function(wrap_pyfunction!(geometry::resample_points_i64, parent)?)?;
    geometry.add_function(wrap_pyfunction!(geometry::resample_points_f32, parent)?)?;
    geometry.add_function(wrap_pyfunction!(geometry::resample_points_f64, parent)?)?;
    geometry.add_function(wrap_pyfunction!(geometry::align_points_orthogonal, parent)?)?;
    geometry.add_function(wrap_pyfunction!(geometry::point_in_polygon_u8, parent)?)?;
    geometry.add_function(wrap_pyfunction!(geometry::point_in_polygon_i32, parent)?)?;
    geometry.add_function(wrap_pyfunction!(geometry::point_in_polygon_i64, parent)?)?;
    geometry.add_function(wrap_pyfunction!(geometry::point_in_polygon_f32, parent)?)?;
    geometry.add_function(wrap_pyfunction!(geometry::point_in_polygon_f64, parent)?)?;

    parent.add_submodule(&geometry)?;
    Ok(())
}

#[pymodule]
fn fqmv(m: &Bound<'_, PyModule>) -> PyResult<()> {
    measure(m)?;
    geometry(m)?;
    Ok(())
}
