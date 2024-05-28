use fqmv_core::geometry::ellipse::fit_ellipse_lstsq;
use fqmv_core::geometry::ellipse::fit_ellipse_direct;

fn unit_circle_unclosed() -> Vec<[f64; 2]> {
    let mut circle = Vec::new();
    for i in 0..360 {
        let angle = i as f64;
        let x = angle.to_radians().cos();
        let y = angle.to_radians().sin();
        circle.push([x, y]);
    }
    circle
}

fn unit_circle_closed() -> Vec<[f64; 2]> {
    let mut circle = Vec::new();
    for i in 0..360 {
        let angle = i as f64;
        let x = angle.to_radians().cos();
        let y = angle.to_radians().sin();
        circle.push([x, y]);
    }
    circle.push([1.0, 0.0]);
    circle
}

#[test]
fn test_fit_ellipse_lstsq() {
    let circle = unit_circle_closed();
    let ellipse_measures = fit_ellipse_lstsq(&circle);

    let major_axis = ellipse_measures[0];
    let minor_axis = ellipse_measures[1];
    let eccentricity = ellipse_measures[2];
    assert!((major_axis - 2.0).abs() < 1e-7);
    assert!((minor_axis - 2.0).abs() < 1e-7);
    assert!((eccentricity - 0.0).abs() < 1e-6);

    let circle = unit_circle_unclosed();
    let ellipse_measures = fit_ellipse_lstsq(&circle);

    let major_axis = ellipse_measures[0];
    let minor_axis = ellipse_measures[1];
    let eccentricity = ellipse_measures[2];
    assert!((major_axis - 2.0).abs() < 1e-7);
    assert!((minor_axis - 2.0).abs() < 1e-7);
    assert!((eccentricity - 0.0).abs() < 1e-6);
}

#[test]
fn test_fit_ellipse_direct() {
    let circle = unit_circle_closed();
    let ellipse_measures = fit_ellipse_direct(&circle);

    let major_axis = ellipse_measures[0];
    let minor_axis = ellipse_measures[1];
    let eccentricity = ellipse_measures[2];
    assert!((major_axis - 2.0).abs() < 1e-7);
    assert!((minor_axis - 2.0).abs() < 1e-7);
    assert!((eccentricity - 0.0).abs() < 1e-7);

    let circle = unit_circle_unclosed();
    let ellipse_measures = fit_ellipse_direct(&circle);

    let major_axis = ellipse_measures[0];
    let minor_axis = ellipse_measures[1];
    let eccentricity = ellipse_measures[2];
    assert!((major_axis - 2.0).abs() < 1e-7);
    assert!((minor_axis - 2.0).abs() < 1e-7);
    assert!((eccentricity - 0.0).abs() < 1e-7);
}
