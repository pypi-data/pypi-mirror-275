use image::Luma;

use fqmv_core::types::Image;

pub fn to_gray(image: Vec<Vec<u8>>) -> Image<Luma<u8>> {
    Image::<Luma<u8>>::from_raw(
        image.len() as u32,
        image[0].len() as u32,
        image.into_iter().flatten().collect()
    ).unwrap_or_else(|| 
        panic!("Invalid image. Must be uint8 grayscale image.")
    )
}
