use image::Luma;

use crate::types::Image;

/// Calculate the maximum pixel intensity in grayscale-converted image
///
/// # Arguments
///
/// * `img` - A GrayImage object
///
/// # Examples
///
/// ```no_run
/// use image::DynamicImage;
/// use fqmv_core::descriptors::intensity::intensity_maximum;
/// let img = DynamicImage::new_luma8(32, 32);
/// let max_intensity = intensity_maximum(&img.to_luma8());
/// ```
pub fn intensity_maximum(img: &Image<Luma<u8>>) -> f64 {
    let mut max_intensity = 0;
    for pixel in img.pixels() {
        if pixel[0] > max_intensity {
            max_intensity = pixel[0];
        }
    }
    max_intensity as f64
}

/// Calculate the minimum pixel intensity in grayscale-converted image
///
/// # Arguments
///
/// * `img` - A GrayImage object
/// * `with_zeros` - If true, include zero intensity pixels in calculation
///
/// # Examples
///
/// ```no_run
/// use image::DynamicImage;
/// use fqmv_core::descriptors::intensity::intensity_minimum;
/// let img = DynamicImage::new_luma8(32, 32);
/// let min_intensity = intensity_minimum(&img.to_luma8(), false);
/// ```
pub fn intensity_minimum(img: &Image<Luma<u8>>, with_zeros: bool) -> f64 {
    let lower_bound = if with_zeros { 0 } else { 1 };
    let mut min_intensity = 255;
    for pixel in img.pixels() {
        if pixel[0] < min_intensity && pixel[0] >= lower_bound {
            min_intensity = pixel[0];
        }
    }
    min_intensity as f64
}

/// Calculate the mean pixel intensity in grayscale-converted image
///
/// # Arguments
///
/// * `img` - A GrayImage object
/// * `with_zeros` - If true, include zero intensity pixels in calculation
///
/// # Examples
///
/// ```no_run
/// use image::DynamicImage;
/// use fqmv_core::descriptors::intensity::intensity_mean;
/// let img = DynamicImage::new_luma8(32, 32);
/// let mean_intensity = intensity_mean(&img.to_luma8(), false);
/// ```
pub fn intensity_mean(img: &Image<Luma<u8>>, with_zeros: bool) -> f64 {
    let lower_bound = if with_zeros { 0 } else { 1 };
    let mut sum = 0;
    let mut count = 0;
    for (_, _, pixel) in img.enumerate_pixels() {
        if pixel[0] >= lower_bound {
            sum += pixel[0] as u64;
            count += 1;
        }
    }
    sum as f64 / count as f64
}

/// Calculate the integrated pixel intensity in grayscale-converted image
///
/// # Arguments
///
/// * `img` - A GrayImage object
///
/// # Examples
///
/// ```no_run
/// use image::DynamicImage;
/// use fqmv_core::descriptors::intensity::intensity_integrated;
/// let img = DynamicImage::new_luma8(32, 32);
/// let integrated_intensity = intensity_integrated(&img.to_luma8());
/// ```
pub fn intensity_integrated(img: &Image<Luma<u8>>) -> f64 {
    let mut sum = 0;
    for pixel in img.pixels() {
        sum += pixel[0] as u64;
    }
    sum as f64
}

/// Calculate the standard deviation of pixel intensity in grayscale-converted image
///
/// # Arguments
///
/// * `img` - A GrayImage object
/// * `with_zeros` - If true, include zero intensity pixels in calculation
///
/// # Examples
///
/// ```no_run
/// use image::DynamicImage;
/// use fqmv_core::descriptors::intensity::intensity_standard_deviation;
/// let img = DynamicImage::new_luma8(32, 32);
/// let std_intensity = intensity_standard_deviation(&img.to_luma8(), false);
/// ```
pub fn intensity_standard_deviation(img: &Image<Luma<u8>>, with_zeros: bool) -> f64 {
    let mean = intensity_mean(img, with_zeros);
    let lower_bound = if with_zeros { 0 } else { 1 };
    let mut sum = 0.0;
    let mut count = 0;
    for pixel in img.pixels() {
        if pixel[0] >= lower_bound {
            sum += (pixel[0] as f64 - mean).powf(2.0);
            count += 1;
        }
    }
    (sum / count as f64).sqrt()
}

/// Calculate the median pixel intensity in grayscale-converted image
///
/// # Arguments
///
/// * `img` - A GrayImage object
/// * `with_zeros` - If true, include zero intensity pixels in calculation
///
/// # Examples
///
/// ```no_run
/// use image::DynamicImage;
/// use fqmv_core::descriptors::intensity::intensity_median;
/// let img = DynamicImage::new_luma8(32, 32);
/// let median_intensity = intensity_median(&img.to_luma8(), false);
/// ```
pub fn intensity_median(img: &Image<Luma<u8>>, with_zeros: bool) -> f64 {
    let lower_bound = if with_zeros { 0 } else { 1 };
    let mut intensities = Vec::new();
    for pixel in img.pixels() {
        if pixel[0] >= lower_bound {
            intensities.push(pixel[0]);
        }
    }
    intensities.sort();
    let mid = intensities.len() / 2;
    if intensities.len() % 2 == 0 {
        (intensities[mid] + intensities[mid - 1]) as f64 / 2.0
    } else {
        intensities[mid] as f64
    }
}

/// Calculate the median absolute deviation of pixel intensity in grayscale-converted image
///
/// # Arguments
///
/// * `img` - A GrayImage object
///
/// # Examples
///
/// ```no_run
/// use image::DynamicImage;
/// use fqmv_core::descriptors::intensity::intensity_median_absolute_deviation;
/// let img = DynamicImage::new_luma8(32, 32);
/// let mad_intensity = intensity_median_absolute_deviation(&img.to_luma8(), false);
/// ```
pub fn intensity_median_absolute_deviation(img: &Image<Luma<u8>>, with_zeros: bool) -> f64 {
    let median = intensity_median(img, with_zeros);
    let lower_bound = if with_zeros { 0 } else { 1 };
    let mut deviations = Vec::new();
    for pixel in img.pixels() {
        if pixel[0] >= lower_bound {
            deviations.push((pixel[0] as f64 - median).abs());
        }
    }
    deviations.sort_by(|a, b| a.partial_cmp(b).unwrap());
    let mid = deviations.len() / 2;
    if deviations.len() % 2 == 0 {
        (deviations[mid] + deviations[mid - 1]) / 2.0
    } else {
        deviations[mid]
    }
}

/// Calculate the histogram of pixel intensity in grayscale-converted image
///
/// # Arguments
///
/// * `img` - A GrayImage object
/// * `bins` - Number of bins in histogram
/// * `with_zeros` - If true, include zero intensity pixels in calculation
/// * `with_max` - Maximum intensity value for histogram; if None, use max in image
///
/// # Examples
///
/// ```no_run
/// use image::DynamicImage;
/// use fqmv_core::descriptors::intensity::intensity_histogram;
/// let img = DynamicImage::new_luma8(32, 32);
/// let histogram = intensity_histogram(&img.to_luma8(), 16, true, None);
/// ```
pub fn intensity_histogram(
    img: &Image<Luma<u8>>,
    bins: usize,
    with_zeros: bool,
    with_max: Option<f64>,
) -> Vec<f64> {
    let max_intensity = if with_max.is_some() {
        with_max.unwrap()
    } else {
        intensity_maximum(img)
    };

    let min_intensity = if with_zeros { 0.0 } else { 1.0 };
    let mut histogram = vec![0.0; bins];
    let bin_width = (max_intensity - min_intensity) / bins as f64;
    for pixel in img.pixels() {
        let pixel = pixel[0] as f64;
        if !with_zeros && pixel == 0.0 {
            continue;
        }

        if pixel > max_intensity {
            continue;
        }

        let mut bin = ((pixel - min_intensity) / bin_width) as usize;
        if bin >= bins {
            bin -= 1;
        }
        histogram[bin] += 1.0;
    }
    histogram
}

/// Calculate the skewness of intensity histogram in grayscale-converted image
///
/// # Arguments
///
/// * `img` - A GrayImage object
/// * `bins` - Number of bins in histogram
/// * `with_zeros` - If true, include zero intensity pixels in calculation
/// * `with_max` - Maximum intensity value for histogram; if None, use max in image
///
/// # Examples
///
/// ```no_run
/// use image::DynamicImage;
/// use fqmv_core::descriptors::intensity::intensity_histogram_skewness;
/// let img = DynamicImage::new_luma8(32, 32);
/// let skewness = intensity_histogram_skewness(&img.to_luma8(), 16, true, None);
/// ```
pub fn intensity_histogram_skewness(
    img: &Image<Luma<u8>>,
    bins: usize,
    with_zeros: bool,
    with_max: Option<f64>,
) -> f64 {
    let histogram = intensity_histogram(img, bins, with_zeros, with_max);
    let mean = histogram.iter().sum::<f64>() as f64 / bins as f64;
    let std = (histogram.iter().map(|&x| (x - mean).powf(2.0)).sum::<f64>() / bins as f64).sqrt();

    if std == 0.0 {
        println!("Warning: standard deviation across intensity histogram is zero; skewness is undefined");
        return 0.0;
    }

    let skewness = histogram.iter()
        .map(|&x| ((x - mean) / std).powf(3.0))
        .sum::<f64>();

    skewness / bins as f64
}

/// Calculate the kurtosis of intensity histogram in grayscale-converted image
///
/// # Arguments
///
/// * `img` - A GrayImage object
/// * `bins` - Number of bins in histogram
/// * `with_zeros` - If true, include zero intensity pixels in calculation
/// * `with_max` - Maximum intensity value for histogram; if None, use max in image
///
/// # Examples
///
/// ```no_run
/// use image::DynamicImage;
/// use fqmv_core::descriptors::intensity::intensity_histogram_kurtosis;
/// let img = DynamicImage::new_luma8(32, 32);
/// let kurtosis = intensity_histogram_kurtosis(&img.to_luma8(), 16, true, None);
/// ```
pub fn intensity_histogram_kurtosis(
    img: &Image<Luma<u8>>,
    bins: usize,
    with_zeros: bool,
    with_max: Option<f64>,
) -> f64 {
    let histogram = intensity_histogram(img, bins, with_zeros, with_max);
    let mean = histogram.iter().sum::<f64>() as f64 / bins as f64;
    let std = (histogram.iter().map(|&x| (x - mean).powf(2.0)).sum::<f64>() / bins as f64).sqrt();

    if std == 0.0 {
        println!("Warning: standard deviation across intensity histogram is zero; kurtosis is undefined");
        return 0.0;
    }

    let kurtosis = histogram.iter()
        .map(|&x| ((x - mean) / std).powf(4.0))
        .sum::<f64>();

    kurtosis / bins as f64
}

/// Non-redundant computation of intensity descriptors in grayscale-converted image
///
/// # Arguments
///
/// * `img` - A GrayImage object
/// * `bins` - Number of bins in histogram
/// * `with_zeros` - If true, include zero intensity pixels in calculation
/// * `with_max` - Maximum intensity value for histogram; if None, use max in image
///
/// # Examples
///
/// ```no_run
/// use image::DynamicImage;
/// use fqmv_core::descriptors::intensity::intensity_descriptors;
/// let img = DynamicImage::new_luma8(32, 32);
/// let descriptors = intensity_descriptors(&img.to_luma8(), 16, false, None);
/// ```
pub fn intensity_descriptors(
    img: &Image<Luma<u8>>,
    bins: usize,
    with_zeros: bool,
    with_max: Option<f64>,
) -> Vec<f64> {
    let lower_bound = if with_zeros { 0 } else { 1 };

    let mut intensity_max = 0;
    let mut intensity_min = lower_bound;
    let mut intensity_integrated = 0.0;
    let mut intensities = Vec::new();
        
    let mut count = 0;
    for pixel in img.pixels() {
        if pixel[0] >= lower_bound {
            intensities.push(pixel[0]);
            if pixel[0] > intensity_max {
                intensity_max = pixel[0];
            }

            if pixel[0] < intensity_min {
                intensity_min = pixel[0];
            }

            count += 1;
        }

        intensity_integrated += pixel[0] as f64;
    }

    let intensity_max = intensity_max as f64;
    let intensity_min = intensity_min as f64;
    let intensity_mean = intensity_integrated / count as f64;

    if intensities.len() == 0 {
        // TO-DO: If all pixels are zero and with_zeros is true then
        // the rest of the descriptors can't be computed; I'm not sure
        // if this is the best way to handle these cases so I'll leave
        // this note here for now
        return vec![
            0.0,
            0.0,
            0.0,
            0.0,
            f64::NAN,
            f64::NAN,
            f64::NAN,
            f64::NAN,
            f64::NAN,
        ];
    }

    intensities.sort();
    let mid = intensities.len() / 2;
    let intensity_median = if intensities.len() % 2 == 0 {
        (intensities[mid] + intensities[mid - 1]) as f64 / 2.0
    } else {
        intensities[mid] as f64
    };

    let upper_bound = if with_max.is_some() {
        with_max.unwrap()
    } else {
        intensity_max
    };

    let bin_width = (upper_bound - lower_bound as f64) / bins as f64;

    let mut intensity_std = 0.0;
    let mut histogram = vec![0.0; bins];
    let mut deviations = Vec::new();
    for pixel in img.pixels() {
        let pixel = pixel[0] as f64;
        if pixel >= lower_bound as f64 {
            intensity_std += (pixel - intensity_mean).powf(2.0);
            deviations.push((pixel - intensity_median).abs());
        }

        if !with_zeros && pixel == 0.0 {
            continue;
        }

        if pixel > upper_bound {
            continue;
        }

        let mut bin = ((pixel - lower_bound as f64) / bin_width) as usize;
        if bin >= bins {
            bin -= 1;
        }
        histogram[bin] += 1.0;
    }
    
    let intensity_std = (intensity_std / count as f64).sqrt();

    deviations.sort_by(|a, b| a.partial_cmp(b).unwrap());
    let mid = deviations.len() / 2;
    let intensity_mad = if deviations.len() % 2 == 0 {
        (deviations[mid] + deviations[mid - 1]) / 2.0
    } else {
        deviations[mid]
    };

    let mut skewness = 0.0;
    let mut kurtosis = 0.0;
    let histogram_mean = histogram.iter().sum::<f64>() / bins as f64;
    let histogram_std = (histogram.iter().map(|&x| (x - histogram_mean).powf(2.0)).sum::<f64>() / bins as f64).sqrt();

    if histogram_std == 0.0 {
        println!("Warning: standard deviation of intensity histogram is zero; skewness and kurtosis are undefined");
        skewness = 0.0;
        kurtosis = 0.0;
    } else {
        for bin in histogram.iter() {
            skewness += ((bin - histogram_mean) / histogram_std).powf(3.0);
            kurtosis += ((bin - histogram_mean) / histogram_std).powf(4.0);
        }

        skewness /= bins as f64;
        kurtosis /= bins as f64;
    }

    vec![
        intensity_max,
        intensity_min,
        intensity_integrated,
        intensity_mean,
        intensity_std,
        intensity_median,
        intensity_mad,
        skewness,
        kurtosis,
    ]
}
    

