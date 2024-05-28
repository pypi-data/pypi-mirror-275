use image::Luma;
use rayon::iter::ParallelIterator;
use kdam::{rayon::prelude::*, TqdmParallelIterator, TqdmIterator};
use polars::prelude::*;

use crate::types::Image;
use crate::helpers::progress_bar;
use crate::descriptors::form::polygon_descriptors;
use crate::descriptors::intensity::intensity_descriptors;
use crate::descriptors::moments::moments_descriptors;
use crate::descriptors::texture::texture_descriptors;
use crate::descriptors::zernike::zernike_descriptors;

use crate::descriptors::names::{
    POLYGON_DESCRIPTOR_NAMES,
    INTENSITY_DESCRIPTOR_NAMES,
    MOMENTS_DESCRIPTOR_NAMES,
    TEXTURE_DESCRIPTOR_NAMES,
    ZERNIKE_DESCRIPTOR_NAMES
};

/// Batch computation of polygon descriptors (operates on contours)
///
/// # Arguments
///
/// * `polygons` - A vector of polygons
/// * `parallel` - If true, use parallel computation
pub fn batch_polygon_descriptors(
    polygons: &Vec<Vec<[f64; 2]>>, 
    parallel: bool
) -> Vec<Vec<f64>> {
    let pb = progress_bar(polygons.len(), "Computing polygon descriptors");

    let descriptors: Vec<Vec<f64>> = if parallel {
        polygons
            .par_iter()
            .tqdm_with_bar(pb)
            .map(|polygon| polygon_descriptors(polygon))
            .collect()
    } else {
        polygons
            .iter()
            .tqdm_with_bar(pb)
            .map(|polygon| polygon_descriptors(polygon))
            .collect()
    };

    descriptors
}

/// Get dataframe of polygon descriptors
///
/// # Arguments
///
/// * `polygons` - A vector of polygons
pub fn batch_polygon_descriptors_df(
    polygons: &Vec<Vec<[f64; 2]>>
) -> DataFrame {
    let descriptors = polygons
        .iter()
        .map(|polygon| polygon_descriptors(polygon))
        .collect();

    batch_to_df(descriptors, POLYGON_DESCRIPTOR_NAMES.iter().map(|&s| s).collect())
}

/// Batch computation of intensity descriptors (operates on grayscale images)
///
/// # Arguments
///
/// * `images` - A vector of grayscale images
/// * `bins` - Number of bins in histogram
/// * `with_zeros` - If true, include zero intensity pixels in calculation
/// * `with_max` - Maximum intensity value for histogram; if None, use max in image
/// * `parallel` - If true, use parallel computation
pub fn batch_intensity_descriptors(
    images: &Vec<Image<Luma<u8>>>,
    bins: usize,
    with_zeros: bool,
    with_max: Option<f64>,
    parallel: bool
) -> Vec<Vec<f64>> {
    let pb = progress_bar(images.len(), "Computing intensity descriptors");

    let descriptors: Vec<Vec<f64>> = if parallel {
        images
            .par_iter()
            .tqdm_with_bar(pb)
            .map(|img| intensity_descriptors(
                img,
                bins,
                with_zeros,
                with_max
            ))
            .collect()
    } else {
        images
            .iter()
            .tqdm_with_bar(pb)
            .map(|img| intensity_descriptors(
                img,
                bins,
                with_zeros,
                with_max
            ))
            .collect()
    };

    descriptors
}

/// Get dataframe of intensity descriptors
///
/// # Arguments
///
/// * `images` - A vector of grayscale images
/// * `bins` - Number of bins in histogram
/// * `with_zeros` - If true, include zero intensity pixels in calculation
/// * `with_max` - Maximum intensity value for histogram; if None, use max in image
pub fn batch_intensity_descriptors_df(
    images: &Vec<Image<Luma<u8>>>,
    bins: usize,
    with_zeros: bool,
    with_max: Option<f64>,
) -> DataFrame {
    let descriptors = images
        .iter()
        .map(|img| intensity_descriptors(
            img,
            bins,
            with_zeros,
            with_max
        ))
        .collect();

    batch_to_df(descriptors, INTENSITY_DESCRIPTOR_NAMES.iter().map(|&s| s).collect())
}

/// Batch computation of binary image moments descriptors (operates on binary masks)
///
/// # Arguments
///
/// * `masks` - A vector of binary images
/// * `parallel` - If true, use parallel computation
pub fn batch_moments_descriptors(
    masks: &Vec<Image<Luma<u8>>>,
    parallel: bool
) -> Vec<Vec<f64>> {
    let pb = progress_bar(masks.len(), "Computing moments descriptors");

    let descriptors: Vec<Vec<f64>> = if parallel {
        masks
            .par_iter()
            .tqdm_with_bar(pb)
            .map(moments_descriptors)
            .collect()
    } else {
        masks
            .iter()
            .tqdm_with_bar(pb)
            .map(moments_descriptors)
            .collect()
    };

    descriptors
}

/// Get dataframe of moments descriptors
///
/// # Arguments
///
/// * `masks` - A vector of binary images
pub fn batch_moments_descriptors_df(
    masks: &Vec<Image<Luma<u8>>>,
) -> DataFrame {
    let descriptors = masks
        .iter()
        .map(moments_descriptors)
        .collect();

    batch_to_df(descriptors, MOMENTS_DESCRIPTOR_NAMES.iter().map(|&s| s).collect())
}

/// Batch computation of texture descriptors (operates on grayscale images)
///
/// # Arguments
///
/// * `images` - Vector of DynamicImage objects
/// * `parallel` - If true, use parallel computation
pub fn batch_texture_descriptors(
    images: &Vec<Image<Luma<u8>>>,
    parallel: bool
) -> Vec<Vec<f64>> {
    let pb = progress_bar(images.len(), "Computing texture descriptors");

    let descriptors: Vec<Vec<f64>> = if parallel {
        images
            .par_iter()
            .tqdm_with_bar(pb)
            .map(texture_descriptors)
            .collect()
    } else {
        images
            .iter()
            .tqdm_with_bar(pb)
            .map(texture_descriptors)
            .collect()
    };

    descriptors
}

/// Get dataframe of texture descriptors
///
/// # Arguments
///
/// * `images` - Vector of DynamicImage objects
pub fn batch_texture_descriptors_df(
    images: &Vec<Image<Luma<u8>>>,
) -> DataFrame {
    let descriptors = images
        .iter()
        .map(texture_descriptors)
        .collect();

    batch_to_df(descriptors, TEXTURE_DESCRIPTOR_NAMES.iter().map(|&s| s).collect())
}

/// Batch computation of zernike descriptors (operates on binary masks)
///
/// # Arguments
///
/// * `masks` - A vector of binary images
/// * `center` - If true, center mask prior to computing the descriptors
/// * `parallel` - If true, use parallel computation
pub fn batch_zernike_descriptors(
    masks: &Vec<Image<Luma<u8>>>,
    center: bool,
    parallel: bool
) -> Vec<Vec<f64>> {
    let pb = progress_bar(masks.len(), "Computing zernike descriptors");

    let descriptors: Vec<Vec<f64>> = if parallel {
        masks
            .par_iter()
            .tqdm_with_bar(pb)
            .map(|mask| zernike_descriptors(mask, Some(center)))
            .collect()
    } else {
        masks
            .iter()
            .tqdm_with_bar(pb)
            .map(|mask| zernike_descriptors(mask, Some(center)))
            .collect()
    };

    descriptors
}

/// Get dataframe of zernike descriptors
///
/// # Arguments
///
/// * `masks` - A vector of binary images
/// * `center` - If true, center mask prior to computing the descriptors
pub fn batch_zernike_descriptors_df(
    masks: &Vec<Image<Luma<u8>>>,
    center: bool,
) -> DataFrame {
    let descriptors = masks
        .iter()
        .map(|mask| zernike_descriptors(mask, Some(center)))
        .collect();

    batch_to_df(descriptors, ZERNIKE_DESCRIPTOR_NAMES.iter().map(|&s| s).collect())
}

/// Convert a nested batch of descriptors to a DataFrame
pub fn batch_to_df(data: Vec<Vec<f64>>, column_names: Vec<&str>) -> DataFrame {
    let mut columns: Vec<Series> = Vec::with_capacity(data[0].len());
    for i in 0..data[0].len() {
        let column: Vec<f64> = data.iter().map(|row| row[i]).collect();
        columns.push(Series::new(column_names[i], column));
    }

    DataFrame::new(columns).unwrap()
}
