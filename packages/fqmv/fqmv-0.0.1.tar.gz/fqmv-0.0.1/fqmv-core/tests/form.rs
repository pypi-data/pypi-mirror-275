use fqmv_core::descriptors::form::*;
use fqmv_core::draw::random_polygons;

fn square_unclosed() -> Vec<[f64; 2]> {
    vec![
        [0.0, 0.0],
        [1.0, 0.0],
        [1.0, 1.0],
        [0.0, 1.0]
    ]
}

fn square_closed() -> Vec<[f64; 2]> {
    vec![
        [0.0, 0.0],
        [1.0, 0.0],
        [1.0, 1.0],
        [0.0, 1.0],
        [0.0, 0.0]
    ]
}

fn square_repeats() -> Vec<[f64; 2]> {
    vec![
        [0.0, 0.0],
        [0.0, 0.0],
        [1.0, 0.0],
        [1.0, 1.0],
        [0.0, 1.0],
        [0.0, 0.0]
    ]
}

fn square_with_negative () -> Vec<[f64; 2]> {
    vec![
        [-1.0, -1.0],
        [0.0, -1.0],
        [1.0, -1.0],
        [1.0, 1.0],
        [0.0, 1.0],
        [-1.0, 1.0],
        [-1.0, -1.0]
    ]
}

fn square_with_inner_point() -> Vec<[f64; 2]> {
    vec![
        [0.0, 0.0],
        [0.5, 0.1],
        [1.0, 0.0],
        [1.0, 1.0],
        [0.0, 1.0],
        [0.0, 0.0]
    ]
}

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

fn unit_circle_repeats() -> Vec<[f64; 2]> {
    let mut circle = Vec::new();
    for i in 0..360 {
        let angle = i as f64;
        let x = angle.to_radians().cos();
        let y = angle.to_radians().sin();
        circle.push([x, y]);
        circle.push([x, y]);
    }
    circle
}

fn elongated_circle() -> Vec<[f64; 2]> {
    let mut circle = Vec::new();
    for i in 0..360 {
        let angle = i as f64;
        let x = angle.to_radians().cos() * 2.0;
        let y = angle.to_radians().sin();
        circle.push([x, y]);
    }
    circle.push([2.0, 0.0]);
    circle
}

#[test]
fn test_polygon_area() {
    
    let area_square_unclosed = polygon_area(&square_unclosed());
    assert_eq!(area_square_unclosed, 1.0);

    let area_square_closed = polygon_area(&square_closed());
    assert_eq!(area_square_closed, 1.0);

    let area_square_repeats = polygon_area(&square_repeats());
    assert_eq!(area_square_repeats, 1.0);

    let area_square_with_negative = polygon_area(&square_with_negative());
    assert_eq!(area_square_with_negative, 4.0);

    let area_circle_unclosed = polygon_area(&unit_circle_unclosed());
    assert!(area_circle_unclosed - std::f64::consts::PI < 1e-8);

    let area_circle_closed = polygon_area(&unit_circle_closed());
    assert!(area_circle_closed - std::f64::consts::PI < 1e-8);

    let area_circle_repeats = polygon_area(&unit_circle_repeats());
    assert!(area_circle_repeats - std::f64::consts::PI < 1e-8);
}

#[test]
fn test_polygon_area_bbox() {
    let area_square_unclosed = polygon_area_bbox(&square_unclosed());
    assert_eq!(area_square_unclosed, 1.0);

    let area_square_closed = polygon_area_bbox(&square_closed());
    assert_eq!(area_square_closed, 1.0);

    let area_square_repeats = polygon_area_bbox(&square_repeats());
    assert_eq!(area_square_repeats, 1.0);

    let area_square_with_negative = polygon_area_bbox(&square_with_negative());
    assert_eq!(area_square_with_negative, 4.0);

    let area_square_with_inner_point = polygon_area_bbox(&square_with_inner_point());
    assert_eq!(area_square_with_inner_point, 1.0);

    let area_circle_unclosed = polygon_area_bbox(&unit_circle_unclosed());
    assert_eq!(area_circle_unclosed, 4.0);

    let area_circle_closed = polygon_area_bbox(&unit_circle_closed());
    assert_eq!(area_circle_closed, 4.0);

    let area_circle_repeats = polygon_area_bbox(&unit_circle_repeats());
    assert_eq!(area_circle_repeats, 4.0);
}

#[test]
fn test_polygon_area_convex() {
    let area_square_unclosed = polygon_area_convex(&square_unclosed());
    assert_eq!(area_square_unclosed, 1.0);

    let area_square_closed = polygon_area_convex(&square_closed());
    assert_eq!(area_square_closed, 1.0);

    let area_square_repeats = polygon_area_convex(&square_repeats());
    assert_eq!(area_square_repeats, 1.0);

    let area_square_with_negative = polygon_area_convex(&square_with_negative());
    assert_eq!(area_square_with_negative, 4.0);

    let area_square_with_inner_point = polygon_area_convex(&square_with_inner_point());
    assert_eq!(area_square_with_inner_point, 1.0);

    let area_circle_unclosed = polygon_area_convex(&unit_circle_unclosed());
    assert!(area_circle_unclosed - std::f64::consts::PI < 1e-8);

    let area_circle_closed = polygon_area_convex(&unit_circle_closed());
    assert!(area_circle_closed - std::f64::consts::PI < 1e-8);

    let area_circle_repeats = polygon_area_convex(&unit_circle_repeats());
    assert!(area_circle_repeats - std::f64::consts::PI < 1e-8);
}

#[test]
fn test_polygon_perimeter() {
    let perimeter_square_unclosed = polygon_perimeter(&square_unclosed());
    assert_eq!(perimeter_square_unclosed, 4.0);

    let perimeter_square_closed = polygon_perimeter(&square_closed());
    assert_eq!(perimeter_square_closed, 4.0);

    let perimeter_square_repeats = polygon_perimeter(&square_repeats());
    assert_eq!(perimeter_square_repeats, 4.0);

    let perimeter_square_with_negative = polygon_perimeter(&square_with_negative());
    assert_eq!(perimeter_square_with_negative, 8.0);

    let perimeter_square_with_inner_point = polygon_perimeter(&square_with_inner_point());
    assert_eq!(perimeter_square_with_inner_point, 4.0 + 2.0*(0.5_f64.powf(2.0) + 0.1_f64.powf(2.0)).sqrt() - 1.0);

    let perimeter_circle_unclosed = polygon_perimeter(&unit_circle_unclosed());
    assert!(perimeter_circle_unclosed - 2.0*std::f64::consts::PI < 1e-8);

    let perimeter_circle_closed = polygon_perimeter(&unit_circle_closed());
    assert!(perimeter_circle_closed - 2.0*std::f64::consts::PI < 1e-8);

    let perimeter_circle_repeats = polygon_perimeter(&unit_circle_repeats());
    assert!(perimeter_circle_repeats - 2.0*std::f64::consts::PI < 1e-8);
}

#[test]
fn test_polygon_elongation() {
    let elongation_square_unclosed = polygon_elongation(&square_unclosed());
    assert_eq!(elongation_square_unclosed, 1.0);

    let elongation_square_closed = polygon_elongation(&square_closed());
    assert_eq!(elongation_square_closed, 1.0);

    let elongation_square_repeats = polygon_elongation(&square_repeats());
    assert_eq!(elongation_square_repeats, 1.0);

    let elongation_square_with_negative = polygon_elongation(&square_with_negative());
    assert_eq!(elongation_square_with_negative, 1.0);

    let elongation_square_with_inner_point = polygon_elongation(&square_with_inner_point());
    assert_eq!(elongation_square_with_inner_point, 1.0);

    let elongation_circle_unclosed = polygon_elongation(&unit_circle_unclosed());
    assert_eq!(elongation_circle_unclosed, 1.0);

    let elongation_circle_closed = polygon_elongation(&unit_circle_closed());
    assert_eq!(elongation_circle_closed, 1.0);

    let elongation_circle_repeats = polygon_elongation(&unit_circle_repeats());
    assert_eq!(elongation_circle_repeats, 1.0);
}

#[test]
fn test_polygon_major_axis_length() {
    // When fit to a square, the best fitting ellipse will have a diameter greater than
    // width/height of the square. We just check that the axis length is within a reasonable
    // range of the square's width/height.
    let major_axis_length_square_unclosed = polygon_major_axis_length::<f64>(&square_unclosed());
    assert!((major_axis_length_square_unclosed - 1.0_f64).abs() < 0.25);

    let major_axis_length_square_closed = polygon_major_axis_length(&square_closed());
    assert!((major_axis_length_square_closed - 1.0_f64).abs() < 0.25);

    let major_axis_length_square_repeats = polygon_major_axis_length(&square_repeats());
    assert!((major_axis_length_square_repeats - 1.0_f64).abs() < 0.25);

    let major_axis_length_square_with_negative = polygon_major_axis_length::<f64>(&square_with_negative());
    assert!((major_axis_length_square_with_negative - 2.0_f64).abs() < 0.5);

    let major_axis_length_square_with_inner_point = polygon_major_axis_length(&square_with_inner_point());
    assert!((major_axis_length_square_with_inner_point - 1.0_f64).abs() < 0.25);

    let major_axis_length_circle_unclosed = polygon_major_axis_length(&unit_circle_unclosed());
    assert!((major_axis_length_circle_unclosed - 2.0).abs() < 1e-4);

    let major_axis_length_circle_closed = polygon_major_axis_length(&unit_circle_closed());
    assert!((major_axis_length_circle_closed - 2.0).abs() < 1e-4);

    let major_axis_length_circle_repeats = polygon_major_axis_length(&unit_circle_repeats());
    assert!((major_axis_length_circle_repeats - 2.0).abs() < 1e-4);

    let major_axis_length_elongated_circle = polygon_major_axis_length(&elongated_circle());
    assert!((major_axis_length_elongated_circle - 4.0).abs() < 1e-4);
}

#[test]
fn test_polygon_minor_axis_length() {
    // When fit to a square, the best fitting ellipse will have a diameter greater than
    // width/height of the square. We just check that the axis length is within a reasonable
    // range of the square's width/height.
    let minor_axis_length_square_unclosed = polygon_minor_axis_length::<f64>(&square_unclosed());
    assert!((minor_axis_length_square_unclosed - 1.0_f64).abs() < 0.25);

    let minor_axis_length_square_closed = polygon_minor_axis_length(&square_closed());
    assert!((minor_axis_length_square_closed - 1.0_f64).abs() < 0.25);

    let minor_axis_length_square_repeats = polygon_minor_axis_length(&square_repeats());
    assert!((minor_axis_length_square_repeats - 1.0_f64).abs() < 0.25);

    let minor_axis_length_square_with_negative = polygon_minor_axis_length::<f64>(&square_with_negative());
    assert!((minor_axis_length_square_with_negative - 2.0_f64).abs() < 0.5);

    let minor_axis_length_square_with_inner_point = polygon_minor_axis_length(&square_with_inner_point());
    assert!((minor_axis_length_square_with_inner_point - 1.0_f64).abs() < 0.25);

    let minor_axis_length_circle_unclosed = polygon_minor_axis_length(&unit_circle_unclosed());
    assert!((minor_axis_length_circle_unclosed - 2.0).abs() < 1e-4);

    let minor_axis_length_circle_closed = polygon_minor_axis_length(&unit_circle_closed());
    assert!((minor_axis_length_circle_closed - 2.0).abs() < 1e-4);

    let minor_axis_length_circle_repeats = polygon_minor_axis_length(&unit_circle_repeats());
    assert!((minor_axis_length_circle_repeats - 2.0).abs() < 1e-4);

    let minor_axis_length_elongated_circle = polygon_minor_axis_length(&elongated_circle());
    assert!((minor_axis_length_elongated_circle - 2.0).abs() < 1e-4);
}


#[test]
fn test_polygon_thread_length() {
    let thread_length_square_unclosed = polygon_thread_length(&square_unclosed());
    assert_eq!(thread_length_square_unclosed, 1.0);

    let thread_length_square_closed = polygon_thread_length(&square_closed());
    assert_eq!(thread_length_square_closed, 1.0);

    let thread_length_square_repeats = polygon_thread_length(&square_repeats());
    assert_eq!(thread_length_square_repeats, 1.0);

    let thread_length_square_with_negative = polygon_thread_length(&square_with_negative());
    assert_eq!(thread_length_square_with_negative, 2.0);

    let thread_length_square_with_inner_point = polygon_thread_length(&square_with_inner_point());
    assert_eq!(thread_length_square_with_inner_point, 1.249749798224722);

    let thread_length_circle_unclosed = polygon_thread_length(&unit_circle_unclosed());
    assert!((thread_length_circle_unclosed - 2.0*std::f64::consts::PI/4.0).abs() < 1e-4);

    let thread_length_circle_closed = polygon_thread_length(&unit_circle_closed());
    assert!((thread_length_circle_closed - 2.0*std::f64::consts::PI/4.0).abs() < 1e-4);

    let thread_length_circle_repeats = polygon_thread_length(&unit_circle_repeats());
    assert!((thread_length_circle_repeats - 2.0*std::f64::consts::PI/4.0).abs() < 1e-4);

    let thread_length_elongated_circle = polygon_thread_length(&elongated_circle());
    let p = polygon_perimeter(&elongated_circle());
    assert_eq!(thread_length_elongated_circle, (p/4.0));
}

#[test]
fn test_polygon_thread_width() {
    let thread_width_square_unclosed = polygon_thread_width(&square_unclosed());
    assert_eq!(thread_width_square_unclosed, 1.0);

    let thread_width_square_closed = polygon_thread_width(&square_closed());
    assert_eq!(thread_width_square_closed, 1.0);

    let thread_width_square_repeats = polygon_thread_width(&square_repeats());
    assert_eq!(thread_width_square_repeats, 1.0);

    let thread_width_square_with_negative = polygon_thread_width(&square_with_negative());
    assert_eq!(thread_width_square_with_negative, 2.0);

    let thread_width_square_with_inner_point = polygon_thread_width(&square_with_inner_point());
    assert_eq!(thread_width_square_with_inner_point, 0.7601521531345564);

    let thread_width_circle_unclosed = polygon_thread_width(&unit_circle_unclosed());
    assert!((thread_width_circle_unclosed - (1.0 / (2.0 / 4.0))).abs() < 1e-4);

    let thread_width_circle_closed = polygon_thread_width(&unit_circle_closed());
    assert!(thread_width_circle_closed - (1.0 / (2.0 / 4.0)) < 1e-4);

    let thread_width_circle_repeats = polygon_thread_width(&unit_circle_repeats());
    assert!(thread_width_circle_repeats - (1.0 / (2.0 / 4.0)) < 1e-4);

    let thread_width_elongated_circle = polygon_thread_width(&elongated_circle());
    let p = polygon_perimeter(&elongated_circle());
    let a = polygon_area(&elongated_circle());
    assert_eq!(thread_width_elongated_circle, a/(p/4.0));
}
    
#[test]
fn test_polygon_solidity() {
    let solidity_square_unclosed = polygon_solidity(&square_unclosed());
    assert_eq!(solidity_square_unclosed, 1.0);

    let solidity_square_closed = polygon_solidity(&square_closed());
    assert_eq!(solidity_square_closed, 1.0);

    let solidity_square_repeats = polygon_solidity(&square_repeats());
    assert_eq!(solidity_square_repeats, 1.0);

    let solidity_square_with_negative = polygon_solidity(&square_with_negative());
    assert_eq!(solidity_square_with_negative, 1.0);

    let solidity_square_with_inner_point = polygon_solidity(&square_with_inner_point());
    assert_eq!(solidity_square_with_inner_point < 1.0, true);

    let solidity_circle_unclosed = polygon_solidity(&unit_circle_unclosed());
    assert!((solidity_circle_unclosed - 1.0).abs() < 1e-4);

    let solidity_circle_closed = polygon_solidity(&unit_circle_closed());
    assert!((solidity_circle_closed - 1.0).abs() < 1e-4);

    let solidity_circle_repeats = polygon_solidity(&unit_circle_repeats());
    assert!((solidity_circle_repeats - 1.0).abs() < 1e-4);

    let solidity_elongated_circle = polygon_solidity(&elongated_circle());
    assert!((solidity_elongated_circle - 1.0).abs() < 1e-4);
}

#[test]
fn test_polygon_extent() {
    let extent_square_unclosed = polygon_extent(&square_unclosed());
    assert_eq!(extent_square_unclosed, 1.0);

    let extent_square_closed = polygon_extent(&square_closed());
    assert_eq!(extent_square_closed, 1.0);

    let extent_square_repeats = polygon_extent(&square_repeats());
    assert_eq!(extent_square_repeats, 1.0);

    let extent_square_with_negative = polygon_extent(&square_with_negative());
    assert_eq!(extent_square_with_negative, 1.0);

    let extent_square_with_inner_point = polygon_extent(&square_with_inner_point());
    assert_eq!(extent_square_with_inner_point, 0.95);

    let extent_circle_unclosed = polygon_extent(&unit_circle_unclosed());
    assert!((extent_circle_unclosed - std::f64::consts::PI / 4.0).abs() < 1e-4);

    let extent_circle_closed = polygon_extent(&unit_circle_closed());
    assert!((extent_circle_closed - std::f64::consts::PI / 4.0).abs() < 1e-4);

    let extent_circle_repeats = polygon_extent(&unit_circle_repeats());
    assert!((extent_circle_repeats - std::f64::consts::PI / 4.0).abs() < 1e-4);

    let extent_elongated_circle = polygon_extent(&elongated_circle());
    let a = polygon_area(&elongated_circle());
    assert_eq!(extent_elongated_circle, a/8.0);
}
    
#[test]
fn test_polygon_form_factor() {
    let form_factor_square_unclosed = polygon_form_factor(&square_unclosed());
    assert_eq!(form_factor_square_unclosed, 4.0 * std::f64::consts::PI / 16.0);
    
    let form_factor_square_closed = polygon_form_factor(&square_closed());
    assert_eq!(form_factor_square_closed, 4.0 * std::f64::consts::PI / 16.0);

    let form_factor_square_repeats = polygon_form_factor(&square_repeats());
    assert_eq!(form_factor_square_repeats, 4.0 * std::f64::consts::PI / 16.0);

    let form_factor_square_with_negative = polygon_form_factor(&square_with_negative());
    assert_eq!(form_factor_square_with_negative, 4.0 * std::f64::consts::PI / 16.0);

    let form_factor_circle_unclosed = polygon_form_factor(&unit_circle_unclosed());
    let p = std::f64::consts::PI * 2.0;
    let a = std::f64::consts::PI;
    assert!((form_factor_circle_unclosed - 4.0 * std::f64::consts::PI * a / (p*p)).abs() < 1e-4);

    let form_factor_circle_closed = polygon_form_factor(&unit_circle_closed());
    assert!((form_factor_circle_closed - 4.0 * std::f64::consts::PI * a / (p*p)).abs() < 1e-4);

    let form_factor_circle_repeats = polygon_form_factor(&unit_circle_repeats());
    assert!((form_factor_circle_repeats - 4.0 * std::f64::consts::PI * a / (p*p)).abs() < 1e-4);

    let form_factor_elongated_circle = polygon_form_factor(&elongated_circle());
    let p = polygon_perimeter(&elongated_circle());
    let a = polygon_area(&elongated_circle());
    assert_eq!(form_factor_elongated_circle, 4.0 * std::f64::consts::PI * a / (p*p));
}

#[test]
fn test_polygon_centroid() {
    let centroid_square_unclosed = polygon_centroid(&square_unclosed());
    assert_eq!(centroid_square_unclosed, (0.5, 0.5));

    let centroid_square_closed = polygon_centroid(&square_closed());
    assert_eq!(centroid_square_closed, (0.5, 0.5));

    let centroid_square_repeats = polygon_centroid(&square_repeats());
    assert!(centroid_square_repeats.0 != 0.5 && centroid_square_repeats.1 != 0.5);

    let centroid_square_with_negative = polygon_centroid(&square_with_negative());
    assert_eq!(centroid_square_with_negative, (0.0, 0.0));

    let centroid_circle_unclosed = polygon_centroid(&unit_circle_unclosed());
    assert!((centroid_circle_unclosed.0 - 0.0).abs() < 1e-7 && (centroid_circle_unclosed.1 - 0.0).abs() < 1e-7);

    let centroid_circle_closed = polygon_centroid(&unit_circle_closed());
    assert!((centroid_circle_closed.0 - 0.0).abs() < 1e-7 && (centroid_circle_closed.1 - 0.0).abs() < 1e-7);

    let centroid_circle_repeats = polygon_centroid(&unit_circle_repeats());
    assert!((centroid_circle_repeats.0 - 0.0).abs() < 1e-7 && (centroid_circle_repeats.1 - 0.0).abs() < 1e-7);

    let centroid_elongated_circle = polygon_centroid(&elongated_circle());
    assert!((centroid_elongated_circle.0 - 0.0).abs() < 1e-7 && (centroid_elongated_circle.1 - 0.0).abs() < 1e-7);
}

#[test]
fn test_polygon_equivalent_diameter() {
    let equivalent_diameter_square_unclosed = polygon_equivalent_diameter(&square_unclosed());
    assert_eq!(equivalent_diameter_square_unclosed, (1.0_f64 / std::f64::consts::PI).sqrt() * 2.0);

    let equivalent_diameter_square_closed = polygon_equivalent_diameter(&square_closed());
    assert_eq!(equivalent_diameter_square_closed, (1.0_f64 / std::f64::consts::PI).sqrt() * 2.0);

    let equivalent_diameter_square_repeats = polygon_equivalent_diameter(&square_repeats());
    assert_eq!(equivalent_diameter_square_repeats, (1.0_f64 / std::f64::consts::PI).sqrt() * 2.0);

    let equivalent_diameter_square_with_negative = polygon_equivalent_diameter(&square_with_negative());
    assert_eq!(equivalent_diameter_square_with_negative, (4.0_f64 / std::f64::consts::PI).sqrt() * 2.0);

    let equivalent_diameter_circle_unclosed = polygon_equivalent_diameter(&unit_circle_unclosed());
    assert!((equivalent_diameter_circle_unclosed - (1.0_f64).sqrt() * 2.0).abs() < 1e-4);

    let equivalent_diameter_circle_closed = polygon_equivalent_diameter(&unit_circle_closed());
    assert!((equivalent_diameter_circle_closed - (1.0_f64).sqrt() * 2.0).abs() < 1e-4);

    let equivalent_diameter_circle_repeats = polygon_equivalent_diameter(&unit_circle_repeats());
    assert!((equivalent_diameter_circle_repeats - (1.0_f64).sqrt() * 2.0).abs() < 1e-4);

    let equivalent_diameter_elongated_circle = polygon_equivalent_diameter(&elongated_circle());
    let a = polygon_area(&elongated_circle());
    assert_eq!(equivalent_diameter_elongated_circle, (a / std::f64::consts::PI).sqrt() * 2.0);
}

#[test]
fn test_polygon_minimum_radius() {
    let minimum_radius_square_unclosed = polygon_minimum_radius(&square_unclosed());
    assert_eq!(minimum_radius_square_unclosed, 0.5_f64.sqrt());

    let minimum_radius_square_closed = polygon_minimum_radius(&square_closed());
    assert_eq!(minimum_radius_square_closed, 0.5_f64.sqrt());

    let minimum_radius_square_with_negative = polygon_minimum_radius(&square_with_negative());
    assert_eq!(minimum_radius_square_with_negative, 1.0_f64.sqrt());

    let minimum_radius_circle_unclosed = polygon_minimum_radius(&unit_circle_unclosed());
    assert!((minimum_radius_circle_unclosed - 1.0_f64.sqrt()) < 1e-4);

    let minimum_radius_circle_closed = polygon_minimum_radius(&unit_circle_closed());
    assert!((minimum_radius_circle_closed - 1.0_f64.sqrt()) < 1e-4);

    let minimum_radius_circle_repeats = polygon_minimum_radius(&unit_circle_repeats());
    assert!((minimum_radius_circle_repeats - 1.0_f64.sqrt()) < 1e-4);

    let minimum_radius_elongated_circle = polygon_minimum_radius(&elongated_circle());
    assert_eq!(minimum_radius_elongated_circle, 1.0_f64.sqrt());
}

#[test]
fn test_polygon_maximum_radius() {
    let maximum_radius_square_unclosed = polygon_maximum_radius(&square_unclosed());
    assert_eq!(maximum_radius_square_unclosed, 0.5_f64.sqrt());

    let maximum_radius_square_closed = polygon_maximum_radius(&square_closed());
    assert_eq!(maximum_radius_square_closed, 0.5_f64.sqrt());

    let maximum_radius_square_with_negative = polygon_maximum_radius(&square_with_negative());
    assert_eq!(maximum_radius_square_with_negative, (1.0_f64.powf(2.0) + 1.0_f64.powf(2.0)).sqrt());

    let maximum_radius_circle_unclosed = polygon_maximum_radius(&unit_circle_unclosed());
    assert!((maximum_radius_circle_unclosed - 1.0_f64.sqrt()) < 1e-4);

    let maximum_radius_circle_closed = polygon_maximum_radius(&unit_circle_closed());
    assert!((maximum_radius_circle_closed - 1.0_f64.sqrt()) < 1e-4);

    let maximum_radius_circle_repeats = polygon_maximum_radius(&unit_circle_repeats());
    assert!((maximum_radius_circle_repeats - 1.0_f64.sqrt()) < 1e-4);

    let maximum_radius_elongated_circle = polygon_maximum_radius(&elongated_circle());
    assert_eq!(maximum_radius_elongated_circle, 2.0_f64);
}

#[test]
fn test_polygon_mean_radius() {
    let mean_radius_square_unclosed = polygon_mean_radius(&square_unclosed());
    assert_eq!(mean_radius_square_unclosed, 0.5_f64.sqrt());

    let mean_radius_square_closed = polygon_mean_radius(&square_closed());
    assert_eq!(mean_radius_square_closed, 0.5_f64.sqrt());

    let mean_radius_circle_closed = polygon_mean_radius(&unit_circle_closed());
    assert!((mean_radius_circle_closed - 1.0_f64.sqrt()) < 1e-4);

    let mean_radius_circle_repeats = polygon_mean_radius(&unit_circle_repeats());
    assert!((mean_radius_circle_repeats - 1.0_f64.sqrt()) < 1e-4);
}

#[test]
fn test_polygon_feret_diameter_maximum() {
    let feret_diameter_square_unclosed = polygon_feret_diameter_maximum(&square_unclosed());
    assert_eq!(feret_diameter_square_unclosed, 1.0);
    
    let feret_diameter_square_closed = polygon_feret_diameter_maximum(&square_closed());
    assert_eq!(feret_diameter_square_closed, 1.0);
    
    let feret_diameter_square_repeats = polygon_feret_diameter_maximum(&square_repeats());
    assert_eq!(feret_diameter_square_repeats, 1.0);

    let feret_diameter_square_with_negative = polygon_feret_diameter_maximum(&square_with_negative());
    assert_eq!(feret_diameter_square_with_negative, 2.0);
    
    let feret_diameter_square_with_inner_point = polygon_feret_diameter_maximum(&square_with_inner_point());
    assert_eq!(feret_diameter_square_with_inner_point, 1.0);
    
    let feret_diameter_circle_unclosed = polygon_feret_diameter_maximum(&unit_circle_unclosed());
    assert!((feret_diameter_circle_unclosed - 2.0).abs() < 1e-3);
    
    let feret_diameter_circle_closed = polygon_feret_diameter_maximum(&unit_circle_closed());
    assert!((feret_diameter_circle_closed - 2.0).abs() < 1e-3);

    let feret_diameter_circle_repeats = polygon_feret_diameter_maximum(&unit_circle_repeats());
    assert!((feret_diameter_circle_repeats - 2.0).abs() < 1e-3);
    
    let feret_diameter_elongated_circle = polygon_feret_diameter_maximum(&elongated_circle());
    assert!((feret_diameter_elongated_circle - 4.0).abs() < 1e-3);
}

#[test]
fn test_polygon_feret_diameter_minimum() {
    let feret_diameter_square_unclosed = polygon_feret_diameter_minimum(&square_unclosed());
    assert_eq!(feret_diameter_square_unclosed, 1.0);

    let feret_diameter_square_closed = polygon_feret_diameter_minimum(&square_closed());
    assert_eq!(feret_diameter_square_closed, 1.0);

    let feret_diameter_square_repeats = polygon_feret_diameter_minimum(&square_repeats());
    assert_eq!(feret_diameter_square_repeats, 1.0);

    let feret_diameter_square_with_negative = polygon_feret_diameter_minimum(&square_with_negative());
    assert_eq!(feret_diameter_square_with_negative, 2.0);

    let feret_diameter_circle_unclosed = polygon_feret_diameter_minimum(&unit_circle_unclosed());
    assert!((feret_diameter_circle_unclosed - 2.0).abs() < 1e-3);

    let feret_diameter_circle_closed = polygon_feret_diameter_minimum(&unit_circle_closed());
    assert!((feret_diameter_circle_closed - 2.0).abs() < 1e-3);

    let feret_diameter_circle_repeats = polygon_feret_diameter_minimum(&unit_circle_repeats());
    assert!((feret_diameter_circle_repeats - 2.0).abs() < 1e-3);

    let feret_diameter_elongated_circle = polygon_feret_diameter_minimum(&elongated_circle());
    assert!((feret_diameter_elongated_circle - 2.0).abs() < 1e-3);
}

#[test]
fn test_polygon_descriptors() {
    for polygon in [
        square_unclosed(),
        square_closed(),
        square_repeats(),
        square_with_negative(),
        square_with_inner_point(),
        unit_circle_unclosed(),
        unit_circle_closed(),
        unit_circle_repeats(),
        elongated_circle()
    ].iter() {
        let descriptors = polygon_descriptors(&polygon);
        assert_eq!(descriptors.len(), 23);

        let area = polygon_area(&polygon);
        let perimeter = polygon_perimeter(&polygon);
        let (centroid_x, centroid_y) = polygon_centroid(&polygon);
        let area_bbox = polygon_area_bbox(&polygon);
        let area_convex = polygon_area_convex(&polygon);
        let elongation = polygon_elongation(&polygon);
        let thread_length = polygon_thread_length(&polygon);
        let thread_width = polygon_thread_width(&polygon);
        let solidity = polygon_solidity(&polygon);
        let extent = polygon_extent(&polygon);
        let form_factor = polygon_form_factor(&polygon);
        let eccentricity = polygon_eccentricity(&polygon);
        let major_axis_length = polygon_major_axis_length(&polygon);
        let minor_axis_length = polygon_minor_axis_length(&polygon);
        let curl_major = polygon_curl_major(&polygon);
        let curl_bbox = polygon_curl_bbox(&polygon);
        let equivalent_diameter = polygon_equivalent_diameter(&polygon);
        let minimum_radius = polygon_minimum_radius(&polygon);
        let maximum_radius = polygon_maximum_radius(&polygon);
        let mean_radius = polygon_mean_radius(&polygon);
        let feret_diameter_maximum = polygon_feret_diameter_maximum(&polygon);
        let feret_diameter_minimum = polygon_feret_diameter_minimum(&polygon);

        assert_eq!(descriptors[0], centroid_x);
        assert_eq!(descriptors[1], centroid_y);
        assert_eq!(descriptors[2], area);
        assert_eq!(descriptors[3], area_bbox);
        assert_eq!(descriptors[4], area_convex);
        assert_eq!(descriptors[5], elongation);
        assert_eq!(descriptors[6], perimeter);
        assert_eq!(descriptors[7], thread_length);
        assert_eq!(descriptors[8], thread_width);
        assert_eq!(descriptors[9], solidity);
        assert_eq!(descriptors[10], extent);
        assert_eq!(descriptors[11], form_factor);
        assert_eq!(descriptors[12], eccentricity);
        assert_eq!(descriptors[13], major_axis_length);
        assert_eq!(descriptors[14], minor_axis_length);
        assert_eq!(descriptors[15], curl_major);
        assert_eq!(descriptors[16], curl_bbox);
        assert_eq!(descriptors[17], equivalent_diameter);
        assert_eq!(descriptors[18], minimum_radius);
        assert_eq!(descriptors[19], maximum_radius);
        assert_eq!(descriptors[20], mean_radius);
        assert!((descriptors[21] - feret_diameter_maximum).abs() < 1e-1);
        assert!((descriptors[22] - feret_diameter_minimum).abs() < 1e-1);
    }
}

#[test]
fn test_polygons_linear() {
    let polygons = random_polygons(10000, 5, 0.2, 1.0, 1.0, 3, "linear", 0.05, 1.0, true, 0);
    for polygon in polygons.iter() {
        let _ = polygon_descriptors(&polygon);
    }
    let pass = true;
    assert!(pass);
}

#[test]
fn test_polygons_bezier() {
    let polygons = random_polygons(10000, 5, 0.2, 1.0, 1.0, 3, "bezier", 0.05, 1.0, true, 0);
    for polygon in polygons.iter() {
        let _ = polygon_descriptors(&polygon);
    }
    let pass = true;
    assert!(pass);
}
