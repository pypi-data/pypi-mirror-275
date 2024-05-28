pub mod processor;
pub mod runners;
pub use processor::Processor;

use image::{Rgb, Luma};
use crate::types::Image;

pub enum ImageContainer {
    Gray8(Image<Luma<u8>>),
    Rgb8(Image<Rgb<u8>>),
}
