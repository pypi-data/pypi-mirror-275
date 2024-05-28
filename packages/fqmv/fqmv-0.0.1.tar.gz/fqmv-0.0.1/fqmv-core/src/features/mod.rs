// Features should be accessed as function names not encapsulating module
// e.g features::glcm and not features::glcm::glcm
mod glcm;
pub use glcm::glcm;
