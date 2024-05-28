use image::{ImageBuffer, Rgb, Luma};

pub fn gray_image() -> ImageBuffer<Luma<u8>, Vec<u8>> {
    let mut img = ImageBuffer::from_fn(4, 4, |_, _| {
        Luma([0u8])
    });

    img.put_pixel(0, 0, Luma([255u8]));
    img.put_pixel(1, 0, Luma([255u8]));
    img.put_pixel(1, 1, Luma([255u8]));
    img.put_pixel(0, 1, Luma([255u8]));

    img
}

pub fn rgb_image() -> ImageBuffer<Rgb<u8>, Vec<u8>> {
    let mut img = ImageBuffer::from_fn(4, 4, |_, _| {
        Rgb([0u8, 0u8, 0u8])
    });

    img.put_pixel(0, 0, Rgb([255u8, 0u8, 0u8]));
    img.put_pixel(1, 0, Rgb([255u8, 0u8, 0u8]));
    img.put_pixel(1, 1, Rgb([255u8, 0u8, 0u8]));
    img.put_pixel(0, 1, Rgb([255u8, 0u8, 0u8]));

    img
}

pub fn mask() -> ImageBuffer<Luma<u16>, Vec<u16>> {
    let mut img = ImageBuffer::from_fn(4, 4, |_, _| {
        Luma([0u16])
    });

    img.put_pixel(0, 0, Luma([1u16]));
    img.put_pixel(1, 0, Luma([1u16]));
    img.put_pixel(1, 1, Luma([1u16]));
    img.put_pixel(0, 1, Luma([1u16]));

    img
}

pub fn polygons() -> Vec<Vec<[f64; 2]>> {
    vec![
        vec![[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0]],
    ]
}
