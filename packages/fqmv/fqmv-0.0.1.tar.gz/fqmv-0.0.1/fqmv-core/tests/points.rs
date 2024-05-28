use fqmv_core::geometry::points::*;

fn elongated_circle(radians: f64) -> Vec<[f64; 2]> {
    let mut circle = Vec::new();
    for i in 0..360 {
        let angle = i as f64;
        let x = angle.to_radians().cos() * 2.0;
        let y = angle.to_radians().sin();
        let x_rot = x * radians.cos() - y * radians.sin();
        let y_rot = x * radians.sin() + y * radians.cos();
        circle.push([x_rot, y_rot]);
    }
    circle
}

#[test]
fn test_order_points() {
    let double_colinear_a = vec![
        [-0.5, 0.0],
        [0.5, 0.0],
        [0.0, 1.0],
        [0.0, -1.0],
    ];

    let ordered = order_points(double_colinear_a);
    assert_eq!(ordered, vec![
        [0.0, -1.0],
        [0.5, 0.0],
        [0.0, 1.0],
        [-0.5, 0.0],
    ]);

    let double_colinear_b = vec![
        [0.5, 0.0],
        [-0.5, 0.0],
        [0.0, 1.0],
        [0.0, -1.0],
    ];

    let ordered = order_points(double_colinear_b);
    assert_eq!(ordered, vec![
        [0.0, -1.0],
        [0.5, 0.0],
        [0.0, 1.0],
        [-0.5, 0.0],
    ]);

    let random_points = vec![
        [0.4, 0.3],
        [0.1, 0.1],
        [-0.1, 5.2],
        [-4.0, -3.0],
    ];

    let ordered = order_points(random_points);
    assert_eq!(ordered, vec![
        [-4.0, -3.0],
        [0.1, 0.1],
        [0.4, 0.3],
        [-0.1, 5.2],
    ]);
}

#[test]
fn test_point_in_polygon() {
    let polygon = vec![
        [0.0, 0.0],
        [1.0, 0.0],
        [1.0, 1.0],
        [0.0, 1.0],
    ];

    let point_inside = [0.5, 0.5];
    let point_outside = [1.5, 0.5];
    let point_on_edge = [0.0, 0.0];

    assert_eq!(point_in_polygon(&point_inside, &polygon), true);
    assert_eq!(point_in_polygon(&point_outside, &polygon), false);
    assert_eq!(point_in_polygon(&point_on_edge, &polygon), true);
}

#[test]
fn test_points_align() {
    for scale in [true, false].iter() {
        let mut circle_0 = elongated_circle(0.0);
        let mut circle_30 = elongated_circle(30.0_f64.to_radians());
        let mut circle_60 = elongated_circle(60.0_f64.to_radians());

        let aligned_0 = align_points_orthogonal(&circle_0, &circle_0, *scale);
        let aligned_30 = align_points_orthogonal(&circle_30, &circle_0, *scale);
        let aligned_60 = align_points_orthogonal(&circle_60, &circle_0, *scale);

        for i in 0..aligned_0.len() {
            assert!((aligned_0[i][0] - aligned_30[i][0]).abs() < 1e-10);
            assert!((aligned_0[i][1] - aligned_30[i][1]).abs() < 1e-10);
            assert!((aligned_0[i][0] - aligned_60[i][0]).abs() < 1e-10);
            assert!((aligned_0[i][1] - aligned_60[i][1]).abs() < 1e-10);
        }

        circle_0.push(circle_0[0]);
        circle_30.push(circle_30[0]);
        circle_60.push(circle_60[0]);

        let aligned_0 = align_points_orthogonal(&circle_0, &circle_0, *scale);
        let aligned_30 = align_points_orthogonal(&circle_30, &circle_0, *scale);
        let aligned_60 = align_points_orthogonal(&circle_60, &circle_0, *scale);

        for i in 0..aligned_0.len() {
            assert!((aligned_0[i][0] - aligned_30[i][0]).abs() < 1e-10);
            assert!((aligned_0[i][1] - aligned_30[i][1]).abs() < 1e-10);
            assert!((aligned_0[i][0] - aligned_60[i][0]).abs() < 1e-10);
            assert!((aligned_0[i][1] - aligned_60[i][1]).abs() < 1e-10);
        }
    }
}
