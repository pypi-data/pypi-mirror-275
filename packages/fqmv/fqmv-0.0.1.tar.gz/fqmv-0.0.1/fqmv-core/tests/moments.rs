use image::{DynamicImage, GrayImage};
use fqmv_core::descriptors::moments;

fn mask_1() -> GrayImage {
    DynamicImage::new_luma8(2, 2).to_luma8()
}

fn mask_2() -> GrayImage {
    let mut mask = DynamicImage::new_luma8(4, 4).to_luma8();
    mask.put_pixel(0, 0, image::Luma([1]));
    mask.put_pixel(1, 1, image::Luma([1]));
    mask.put_pixel(2, 2, image::Luma([1]));
    mask.put_pixel(3, 3, image::Luma([1]));
    mask
}

fn mask_3() -> GrayImage {
    let mut mask = DynamicImage::new_luma8(10, 10).to_luma8();
    for i in 0..10 {
        for j in 0..10 {
            mask.put_pixel(i, j, image::Luma([(i + j) as u8]));
        }
    }
    mask
}

#[test]
fn test_moments_raw() {
    let moments_1 = moments::moments_raw(&mask_1());
    assert_eq!(moments_1, vec![0.0; 10]);

    let moments_2 = moments::moments_raw(&mask_2());
    assert_eq!(moments_2, vec![
        4.0, 6.0,
        6.0, 14.0,
        14.0, 14.0, 
        36.0, 36.0,
        36.0, 36.0
    ]);

    let moments_3 = moments::moments_raw(&mask_3());
    assert_eq!(moments_3, vec![
        900.0, 4875.0,
        4875.0, 25650.0,
        33075.0, 33075.0,
        172350.0, 172350.0,
        244455.0, 244455.0
    ]);
}

#[test]
fn test_moments_central() {
    let moments_1 = moments::moments_central(&mask_1());
    assert_eq!(moments_1, vec![0.0; 10]);

    let moments_2 = moments::moments_central(&mask_2());
    assert_eq!(moments_2, vec![
        4.0, 0.0,
        0.0, 5.0,
        5.0, 5.0,
        0.0, 0.0,
        0.0, 0.0
    ]);

    let moments_3 = moments::moments_central(&mask_3());
    assert!(moments_3.iter().zip(vec![
        900.0, 0.0,
        0.0, -756.25,
        6668.75, 6668.75,
        1386.4583333333212, 1386.4583333333212,
        -6946.041666666686, -6946.041666666686
    ]).all(|(a, b)| (a - b).abs() < 1e-9));
}

#[test]
fn test_moments_hu() {
    let moments = moments::moments_hu(&mask_1());
    assert_eq!(moments, vec![0.0; 7]);

    let moments = moments::moments_hu(&mask_2());
    assert_eq!(moments, vec![0.625, 0.390625, 0.0, 0.0, 0.0, 0.0, 0.0]);

    let moments = moments::moments_hu(&mask_3());
    assert!(moments.iter().zip(vec![
        0.0164660494,
        3.48674935e-06,
        4.17721822e-07,
        1.04689214e-07,
        -2.18925569e-14,
        -1.95484488e-10,
        0.0
    ]).all(|(a, b)| (a - b).abs() < 1e-9));
}

#[test]
fn test_binary_descriptors() {
    let raw_moments = moments::moments_raw(&mask_1());
    let central_moments = moments::moments_central(&mask_1());
    let hu_moments = moments::moments_hu(&mask_1());
    let moments = moments::moments_descriptors(&mask_1());

    let concat_moments = raw_moments.iter()
        .chain(central_moments.iter().skip(3))
        .chain(hu_moments.iter())
        .cloned()
        .collect::<Vec<f64>>();

    assert_eq!(moments, concat_moments);

    let raw_moments = moments::moments_raw(&mask_2());
    let central_moments = moments::moments_central(&mask_2());
    let hu_moments = moments::moments_hu(&mask_2());
    let moments = moments::moments_descriptors(&mask_2());

    let concat_moments = raw_moments.iter()
        .chain(central_moments.iter().skip(3))
        .chain(hu_moments.iter())
        .cloned()
        .collect::<Vec<f64>>();

    assert_eq!(moments, concat_moments);

    let raw_moments = moments::moments_raw(&mask_3());
    let central_moments = moments::moments_central(&mask_3());
    let hu_moments = moments::moments_hu(&mask_3());
    let moments = moments::moments_descriptors(&mask_3());

    let concat_moments = raw_moments.iter()
        .chain(central_moments.iter().skip(3))
        .chain(hu_moments.iter())
        .cloned()
        .collect::<Vec<f64>>();

    assert_eq!(moments, concat_moments);
}
