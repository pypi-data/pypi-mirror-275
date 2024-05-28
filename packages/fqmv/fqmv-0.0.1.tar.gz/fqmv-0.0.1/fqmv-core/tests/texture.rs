use fqmv_core::features::glcm;
use image::{ImageBuffer, Luma};
use fqmv_core::descriptors::texture;

fn square_mask() -> ImageBuffer<Luma<u8>, Vec<u8>> {
    let mut mask = ImageBuffer::<Luma<u8>, Vec<u8>>::new(2, 2);
    for i in 0..2 {
        for j in 0..2 {
            if j > 0 {
                mask.put_pixel(i, j, Luma([1u8]));
            }
        }
    }
    mask
}


#[test]
fn test_texture_energy() {
    let mask = square_mask();
    let comatrix = glcm(&mask, 1.0, 0.0, 2, false, false, false);
    let energy = texture::texture_energy(&comatrix);
    assert_eq!(energy, 0.5);
}

#[test]
fn test_texture_contrast() {
    let mask = square_mask();
    let comatrix = glcm(&mask, 1.0, 0.0, 2, false, false, false);
    let contrast = texture::texture_contrast(&comatrix);
    assert_eq!(contrast, 0.0);
}

#[test]
fn test_texture_correlation() {
    let mask = square_mask();
    let comatrix = glcm(&mask, 1.0, 0.0, 2, false, false, false);
    let correlation = texture::texture_correlation(&comatrix);
    assert_eq!(correlation, 1.0);
}

#[test]
fn test_texture_sum_of_squares() {
    let mask = square_mask();
    let comatrix = glcm(&mask, 1.0, 0.0, 2, false, false, false);
    let sum_of_squares = texture::texture_sum_of_squares(&comatrix);
    assert_eq!(sum_of_squares, 0.25);
}

#[test]
fn test_texture_inverse_difference() {
    let mask = square_mask();
    let comatrix = glcm(&mask, 1.0, 0.0, 2, false, false, false);
    let inverse_difference = texture::texture_inverse_difference(&comatrix);
    assert_eq!(inverse_difference, 1.0);
}

#[test]
fn test_texture_sum_average() {
    let mask = square_mask();
    let comatrix = glcm(&mask, 1.0, 0.0, 2, false, false, false);
    let sum_average = texture::texture_sum_average(&comatrix);
    assert_eq!(sum_average, 1.0);
}

#[test]
fn test_texture_sum_variance() {
    let mask = square_mask();
    let comatrix = glcm(&mask, 1.0, 0.0, 2, false, false, false);
    let sum_variance = texture::texture_sum_variance(&comatrix);
    assert_eq!(sum_variance, 1.0);
}

#[test]
fn test_texture_sum_entropy() {
    let mask = square_mask();
    let comatrix = glcm(&mask, 1.0, 0.0, 2, false, false, false);
    let sum_entropy = texture::texture_sum_entropy(&comatrix);
    assert!((sum_entropy - 1.0).abs() < 1e-6);
}

#[test]
fn test_texture_entropy() {
    let mask = square_mask();
    let comatrix = glcm(&mask, 1.0, 0.0, 2, false, false, false);
    let entropy = texture::texture_entropy(&comatrix);
    assert!((entropy - 1.0).abs() < 1e-6);
}

#[test]
fn test_texture_difference_variance() {
    let mask = square_mask();
    let comatrix = glcm(&mask, 1.0, 0.0, 2, false, false, false);
    let difference_variance = texture::texture_difference_variance(&comatrix);
    assert_eq!(difference_variance, 0.25);
}

#[test]
fn test_texture_difference_entropy() {
    let mask = square_mask();
    let comatrix = glcm(&mask, 1.0, 0.0, 2, false, false, false);
    let difference_entropy = texture::texture_difference_entropy(&comatrix);
    assert!((difference_entropy).abs() < 1e-6);
}

#[test]
fn test_texture_information_measure_of_correlation_1() {
    let mask = square_mask();
    let comatrix = glcm(&mask, 1.0, 0.0, 2, false, false, false);
    let imc1 = texture::texture_infocorr_1(&comatrix);
    assert_eq!(imc1, -1.0);
}

#[test]
fn test_texture_information_measure_of_correlation_2() {
    let mask = square_mask();
    let comatrix = glcm(&mask, 1.0, 0.0, 2, false, false, false);
    let imc2 = texture::texture_infocorr_2(&comatrix);
    assert!((imc2 - 1.0).abs() < 0.1);
}

#[test]
fn test_haralick_features() {
    let mask = square_mask();
    let comatrix = glcm(&mask, 1.0, 0.0, 2, false, false, false);
    let features = texture::haralick_features(&comatrix);
    assert_eq!(features.len(), 13);
    assert_eq!(features[0], 0.5);
    assert_eq!(features[1], 0.0);
    assert_eq!(features[2], 1.0);
    assert_eq!(features[3], 0.25);
    assert_eq!(features[4], 1.0);
    assert_eq!(features[5], 1.0);
    assert_eq!(features[6], 1.0);
    assert!((features[7] - 1.0).abs() < 1e-6);
    assert!((features[8] - 1.0).abs() < 1e-6);
    assert_eq!(features[9], 0.25);
    assert!((features[10]).abs() < 1e-6);
    assert_eq!(features[11], -1.0);
    assert!((features[12] - 1.0).abs() < 0.1);
}
