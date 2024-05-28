use image::{ImageBuffer, Pixel, Luma};

pub type Image<P> = ImageBuffer<P, Vec<<P as Pixel>::Subpixel>>;
pub type Mask = Image<Luma<u16>>;
