use fqmv_core::geometry::hull::convex_hull_graham;

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

#[test]
fn test_convex_hull_graham() {
    let square = square_closed();
    let hull = convex_hull_graham(&square);
    assert_eq!(hull.len(), 5);
    assert_eq!(hull, vec![
        [1.0, 0.0],
        [1.0, 1.0],
        [0.0, 1.0],
        [0.0, 0.0],
        [1.0, 0.0]
    ]);


    let square = square_unclosed();
    let hull = convex_hull_graham(&square);
    assert_eq!(hull.len(), 5);
    assert_eq!(hull, vec![
        [1.0, 0.0],
        [1.0, 1.0],
        [0.0, 1.0],
        [0.0, 0.0],
        [1.0, 0.0]
    ]);

    let square = square_repeats();
    let hull = convex_hull_graham(&square);
    assert_eq!(hull.len(), 5);
    assert_eq!(hull, vec![
        [1.0, 0.0],
        [1.0, 1.0],
        [0.0, 1.0],
        [0.0, 0.0],
        [1.0, 0.0]
    ]);

    let square = square_with_negative();
    let hull = convex_hull_graham(&square);
    assert_eq!(hull.len(), 6);
    assert_eq!(hull, vec![
        [1.0, -1.0],
        [1.0, 1.0],
        [0.0, 1.0],
        [-1.0, 1.0],
        [-1.0, -1.0],
        [1.0, -1.0]
    ]);

    let square = square_with_inner_point();
    let hull = convex_hull_graham(&square);
    assert_eq!(hull.len(), 5);
    assert_eq!(hull, vec![
        [1.0, 0.0],
        [1.0, 1.0],
        [0.0, 1.0],
        [0.0, 0.0],
        [1.0, 0.0]
    ]);
}
