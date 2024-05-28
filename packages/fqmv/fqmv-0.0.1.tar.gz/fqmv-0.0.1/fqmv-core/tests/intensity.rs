use image::{DynamicImage, GrayImage};
use fqmv_core::descriptors::intensity;

fn test_image() -> GrayImage {
    let mut img = DynamicImage::new_rgb8(10, 10).to_rgb8();
    for y in 0..10 {
        for x in 0..10 {
            img.put_pixel(x, y, image::Rgb([x as u8, x as u8, x as u8]));
        }
    }
    DynamicImage::ImageRgb8(img).to_luma8()
}

fn test_image_2() -> GrayImage {
    let mut img = DynamicImage::new_rgb8(2, 3).to_rgb8();
    img.put_pixel(0, 0, image::Rgb([1 as u8, 1 as u8, 1 as u8]));
    img.put_pixel(0, 1, image::Rgb([2 as u8, 2 as u8, 2 as u8]));
    img.put_pixel(0, 2, image::Rgb([3 as u8, 3 as u8, 3 as u8]));
    img.put_pixel(1, 0, image::Rgb([2 as u8, 2 as u8, 2 as u8]));
    img.put_pixel(1, 1, image::Rgb([3 as u8, 3 as u8, 3 as u8]));
    img.put_pixel(1, 2, image::Rgb([4 as u8, 4 as u8, 4 as u8]));
    DynamicImage::ImageRgb8(img).to_luma8()
}

#[test]
fn test_intensity_max() {
    let img = test_image();
    let max = intensity::intensity_maximum(&img);
    assert_eq!(max, 9.0);
}

#[test]
fn test_intensity_min() {
    let img = test_image();
    let min_with_zeros = intensity::intensity_minimum(&img, true);
    assert_eq!(min_with_zeros, 0.0);

    let min_without_zeros = intensity::intensity_minimum(&img, false);
    assert_eq!(min_without_zeros, 1.0);
}

#[test]
fn test_intensity_mean() {
    let img = test_image();
    let mean_with_zeros = intensity::intensity_mean(&img, true);
    assert_eq!(mean_with_zeros, 4.5);

    let mean_without_zeros = intensity::intensity_mean(&img, false);
    assert_eq!(mean_without_zeros, 5.0);
}

#[test]
fn test_intensity_integrated() {
    let img = test_image();
    let integrated = intensity::intensity_integrated(&img);
    assert_eq!(integrated, 45.0*10.0);
}

#[test]
fn test_intensity_std() {
    let img = test_image();
    let std_with_zeros = intensity::intensity_standard_deviation(&img, true);
    let mut true_std_with_zeros = 0.0;
    for x in 0..10 {
        true_std_with_zeros += (x as f64 - 4.5).powi(2);
    }
    assert_eq!(std_with_zeros, (true_std_with_zeros/10.0).sqrt());

    let std_without_zeros = intensity::intensity_standard_deviation(&img, false);
    let mut true_std_without_zeros = 0.0;
    for x in 1..10 {
        true_std_without_zeros += (x as f64 - 5.0).powi(2);
    }
    assert_eq!(std_without_zeros, (true_std_without_zeros/9.0).sqrt());
}

#[test]
fn test_intensity_median() {
    let img = test_image();
    let median_with_zeros = intensity::intensity_median(&img, true);
    assert_eq!(median_with_zeros, 4.5);

    let median_without_zeros = intensity::intensity_median(&img, false);
    assert_eq!(median_without_zeros, 5.0);
}

#[test]
fn test_intensity_mad() {
    let img = test_image();
    let mad_with_zeros = intensity::intensity_median_absolute_deviation(&img, true);
    assert_eq!(mad_with_zeros, 2.5);

    let mad_without_zeros = intensity::intensity_median_absolute_deviation(&img, false);
    assert_eq!(mad_without_zeros, 2.0);
}

#[test]
fn test_intensity_histogram() {
    let img = test_image();
    let hist_with_zeros = intensity::intensity_histogram(&img, 10, true, None);
    assert_eq!(hist_with_zeros.len(), 10);
    for i in 0..10 {
        assert_eq!(hist_with_zeros[i], 10.0);
    }

    let hist_with_zeros_2 = intensity::intensity_histogram(&img, 5, true, None);
    assert_eq!(hist_with_zeros_2.len(), 5);
    for i in 0..5 {
        assert_eq!(hist_with_zeros_2[i], 20.0);
    }

    let img2 = test_image_2();
    let hist_with_zeros_3 = intensity::intensity_histogram(&img2, 4, true, None);
    assert_eq!(hist_with_zeros_3.len(), 4);
    for i in 0..4 {
        assert_eq!(hist_with_zeros_3[i], i as f64);
    }

    let hist_without_zeros = intensity::intensity_histogram(&img, 9, false, None);
    assert_eq!(hist_without_zeros.len(), 9);
    for i in 0..9 {
        assert_eq!(hist_without_zeros[i], 10.0);

    }

    let hist_with_max = intensity::intensity_histogram(&img, 4, true, Some(3.0));
    assert_eq!(hist_with_max.len(), 4);
    for i in 0..4 {
        assert_eq!(hist_with_max[i], 10.0);
    }
}

#[test]
fn test_intensity_histogram_skewness() {
    let img = test_image();
    let skewness_with_zeros = intensity::intensity_histogram_skewness(&img, 10, true, None);
    assert_eq!(skewness_with_zeros, 0.0);

    let skewness_without_zeros = intensity::intensity_histogram_skewness(&img, 9, false, None);
    assert_eq!(skewness_without_zeros, 0.0);

    let img2 = test_image_2();
    let skewness_with_zeros_2 = intensity::intensity_histogram_skewness(&img2, 4, true, None);
    assert!((skewness_with_zeros_2 - 0.0).abs() < 1e-7);

    let skewness_with_max = intensity::intensity_histogram_skewness(&img, 4, true, Some(3.0));
    assert_eq!(skewness_with_max, 0.0);
}

#[test]
fn test_intensity_histogram_kurtosis() {
    let img = test_image();
    let kurtosis_with_zeros = intensity::intensity_histogram_kurtosis(&img, 10, true, None);
    assert_eq!(kurtosis_with_zeros, 0.0);

    let kurtosis_without_zeros = intensity::intensity_histogram_kurtosis(&img, 9, false, None);
    assert_eq!(kurtosis_without_zeros, 0.0);

    let img2 = test_image_2();
    let kurtosis_with_zeros_2 = intensity::intensity_histogram_kurtosis(&img2, 4, true, None);
    assert!((kurtosis_with_zeros_2 -  1.64).abs() < 1e-7);

    let kurtosis_with_max = intensity::intensity_histogram_kurtosis(&img, 4, true, Some(3.0));
    assert_eq!(kurtosis_with_max, 0.0);
}

#[test]
fn test_intensity_descriptors() {
    let img = test_image();

    for params in [
        (10, true, None),
        (9, false, None)
    ].iter() {
        let intensity_max = intensity::intensity_maximum(&img);
        let intensity_min = intensity::intensity_minimum(&img, params.1);
        let intensity_integrated = intensity::intensity_integrated(&img);
        let intensity_mean = intensity::intensity_mean(&img, params.1);
        let intensity_std = intensity::intensity_standard_deviation(&img, params.1);
        let intensity_median = intensity::intensity_median(&img, params.1);
        let intensity_mad = intensity::intensity_median_absolute_deviation(&img, params.1);
        let intensity_skewness = intensity::intensity_histogram_skewness(&img, params.0, params.1, params.2);
        let intensity_kurtosis = intensity::intensity_histogram_kurtosis(&img, params.0, params.1, params.2);

        let descriptors = intensity::intensity_descriptors(&img, params.0, params.1, params.2);

        assert_eq!(descriptors[0], intensity_max);
        assert_eq!(descriptors[1], intensity_min);
        assert_eq!(descriptors[2], intensity_integrated);
        assert_eq!(descriptors[3], intensity_mean);
        assert_eq!(descriptors[4], intensity_std);
        assert_eq!(descriptors[5], intensity_median);
        assert_eq!(descriptors[6], intensity_mad);
        assert_eq!(descriptors[7], intensity_kurtosis);
        assert_eq!(descriptors[8], intensity_skewness);
    }

    let img2 = test_image_2();
    let descriptors = intensity::intensity_descriptors(&img2, 4, true, None);
    let skewness = intensity::intensity_histogram_skewness(&img2, 4, true, None);
    let kurtosis = intensity::intensity_histogram_kurtosis(&img2, 4, true, None);
    assert_eq!(descriptors[7], skewness);
    assert_eq!(descriptors[8], kurtosis);
}
