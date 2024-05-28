use fqmv_core::features::glcm;
use image::{DynamicImage, GrayImage, Luma};

#[test]
fn test_glcm_zero() {
    let img = DynamicImage::new_luma8(10, 10).to_luma8();
    let glcm_zero = glcm(&img, 1.0, 0.0, 11, false, false, false);
    assert_eq!(glcm_zero[(0, 0)], 90.0);
}

#[test]
fn test_glcm_diagonal() {
    let mut img = GrayImage::new(10, 10);
    for w in 0..10 {
        for h in 0..10 {
            let t = Luma([w as u8]);
            img.put_pixel(w, h, t);
        }
    }

    let img = DynamicImage::ImageLuma8(img).to_luma8();
    let glcm_diagonal = glcm(&img, 1.0, 0.0, 11, false, false, false);
    assert_eq!(glcm_diagonal.clone().dimensions(), (11, 11));

    for i in 0..11 {
        for j in 0..11 {
            if i + 1 == j && j < 10 && i < 9 {
                assert_eq!(glcm_diagonal[(i, j)], 10.0);
            } else {
                assert_eq!(glcm_diagonal[(i, j)], 0.0);
            }
        }
    }
}

#[test]
fn test_glcm_diagonal_rectangle() {
    let mut img = GrayImage::new(10, 15);
    for w in 0..10 {
        for h in 0..15 {
            let t = Luma([w as u8]);
            img.put_pixel(w, h, t);
        }
    }

    let img = DynamicImage::ImageLuma8(img).to_luma8();
    let glcm_diagonal = glcm(&img, 1.0, 0.0, 11, false, false, false);
    assert_eq!(glcm_diagonal.clone().dimensions(), (11, 11));
    
    for i in 0..11 {
        for j in 0..11 {
            if i + 1 == j && j < 10 && i < 9 {
                assert_eq!(glcm_diagonal[(i, j)], 15.0);
            } else {
                assert_eq!(glcm_diagonal[(i, j)], 0.0);
            }
        }
    }
}
