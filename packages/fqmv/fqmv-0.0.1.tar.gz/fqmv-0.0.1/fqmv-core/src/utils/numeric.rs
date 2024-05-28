use std::ops::{Add, Div, Mul, Sub, SubAssign, AddAssign, DivAssign, MulAssign};

/// A trait for writing generic code over any numeric type
pub trait Numeric:    
Copy
+ Clone
+ PartialEq
+ PartialOrd
+ Add<Self, Output = Self>
+ Sub<Self, Output = Self>
+ Div<Self, Output = Self>
+ Mul<Self, Output = Self>
+ AddAssign
+ SubAssign
+ DivAssign
+ MulAssign
{
	/// Returns the data type as a string
	fn dtype() -> &'static str;
	/// Converts numeric to a `usize`.
	fn to_usize(self) -> usize;
	/// Converts numeric to a `isize`.
	fn to_isize(self) -> isize; 
	/// Converts numeric to a `u8`.
	fn to_u8(self) -> u8;
	/// Converts numeric to a `u16`.
	fn to_u16(self) -> u16;
	/// Converts numeric to a `u32`.
	fn to_u32(self) -> u32;
	/// Converts numeric to a `u64`.
	fn to_u64(self) -> u64;
	/// Converts numeric to a `i8`.
	fn to_i8(self) -> i8;
	/// Converts numeric to a `i16`.
	fn to_i16(self) -> i16;
	/// Converts numeric to a `i32`.
	fn to_i32(self) -> i32;
	/// Converts numeric to a `i64`.
	fn to_i64(self) -> i64;
	/// Converts numeric to a `f32`.
	fn to_f32(self) -> f32;
	/// Converts numeric to a `f64`.
	fn to_f64(self) -> f64;
	/// Converts a `usize` to a numeric.
	fn from_usize(v: usize) -> Self;
	// Converts a `isize` to a numeric.
	fn from_isize(v: isize) -> Self;
	/// Converts a `u8` to a numeric.
	fn from_u8(v: u8) -> Self;
	/// Converts a `u16` to a numeric.
	fn from_u16(v: u16) -> Self;
	/// Converts a `u32` to a numeric.
	fn from_u32(v: u32) -> Self;
	/// Converts a `u64` to a numeric.
	fn from_u64(v: u64) -> Self;
	/// Converts a `i8` to a numeric.
	fn from_i8(v: i8) -> Self;
	/// Converts a `i16` to a numeric.
	fn from_i16(v: i16) -> Self;
	/// Converts a `i32` to a numeric.
	fn from_i32(v: i32) -> Self;
	/// Converts a `i64` to a numeric.
	fn from_i64(v: i64) -> Self;
	/// Converts a `f32` to a numeric.
	fn from_f32(v: f32) -> Self;
	/// Converts a `f64` to a numeric.
	fn from_f64(v: f64) -> Self;
	/// Returns the representation of "infinity" for this numeric type.
	fn infinity() -> Self;
	/// Returns the representation of "negative infinity" for this numeric type.
	fn neg_infinity() -> Self;
	/// Returns the maximum value for this numeric type.
	fn max_value() -> Self;
	/// Returns the minimum value for this numeric type.
	fn min_value() -> Self;
	/// Returns the maximum
	fn max(self, other: Self) -> Self {
		if self > other {
			self
		} else {
			other
		}
	}
	/// Returns the minimum
	fn min(self, other: Self) -> Self {
		if self < other {
			self
		} else {
			other
		}
	}
	/// Returns the square root.
	fn sqrt(self) -> Self;
	// Returns the exp
	fn exp(self) -> Self;
	/// Returns the absolute value.
	fn abs(self) -> Self;
	/// Return the power
	fn powf(self, exp: Self) -> Self;
	/// Return the atan
	fn atan(self) -> Self;
	/// Return the atan2
	fn atan2(self, y: Self) -> Self;
	// Return the ceil
	fn ceil(self) -> Self;
	/// Returns the floor
	fn floor(self) -> Self;
	/// Returns the epsilon
	fn epsilon() -> Self;
	/// Returns PI
	fn pi() -> Self;
	/// Returns zero
	fn zero() -> Self;
	/// Returns one
	fn one() -> Self;
	/// Returns two
	fn two() -> Self;
	// Remainder of the division
	fn rem(self, other: Self) -> Self {
		self - (self / other).floor() * other
	}
	// Round to the nearest integer
	fn round(self) -> Self;
	// Compare two values
	fn cmp(self, b: Self) -> std::cmp::Ordering;
}

impl Numeric for f32 {
	fn dtype() -> &'static str {
		"f32"
	}

	fn to_usize(self) -> usize {
		self as usize
	}

	fn to_isize(self) -> isize {
		self as isize
	}

	fn to_u8(self) -> u8 {
		self as u8
	}

	fn to_u16(self) -> u16 {
		self as u16
	}

	fn to_u32(self) -> u32 {
		self as u32
	}

	fn to_u64(self) -> u64 {
		self as u64
	}

	fn to_i8(self) -> i8 {
		self as i8
	}

	fn to_i16(self) -> i16 {
		self as i16
	}

	fn to_i32(self) -> i32 {
		self as i32
	}

	fn to_i64(self) -> i64 {
		self as i64
	}

	fn to_f32(self) -> f32 {
		self
	}

	fn to_f64(self) -> f64 {
		self as f64
	}

	fn from_usize(v: usize) -> f32 {
		v as f32
	}

	fn from_isize(v: isize) -> f32 {
		v as f32
	}

	fn from_u8(v: u8) -> f32 {
		v as f32
	}

	fn from_u16(v: u16) -> f32 {
		v as f32
	}

	fn from_u32(v: u32) -> f32 {
		v as f32
	}

	fn from_u64(v: u64) -> f32 {
		v as f32
	}

	fn from_i8(v: i8) -> f32 {
		v as f32
	}

	fn from_i16(v: i16) -> f32 {
		v as f32
	}

	fn from_i32(v: i32) -> f32 {
		v as f32
	}

	fn from_i64(v: i64) -> f32 {
		v as f32
	}

	fn from_f32(v: f32) -> f32 {
		v
	}

	fn from_f64(v: f64) -> f32 {
		v as f32
	}

	fn infinity() -> f32 {
		f32::INFINITY
	}

	fn neg_infinity() -> f32 {
		f32::NEG_INFINITY
	}

	fn max_value() -> f32 {
		f32::MAX
	}

	fn min_value() -> f32 {
		f32::MIN
	}

	fn max(self, other: f32) -> f32 {
		f32::max(self, other)
	}

	fn min(self, other: f32) -> f32 {
		f32::min(self, other)
	}

	fn sqrt(self) -> f32 {
		f32::sqrt(self)
	}

	fn exp(self) -> f32 {
		f32::exp(self)
	}

	fn abs(self) -> f32 {
		f32::abs(self)
	}

	fn powf(self, exp: Self) -> Self {
		f32::powf(self, exp)
	}

	fn atan(self) -> f32 {
		f32::atan(self)
	}

	fn atan2(self, y: Self) -> Self {
		f32::atan2(self, y)
	}

	fn ceil(self) -> f32 {
		f32::ceil(self)
	}

	fn floor(self) -> f32 {
		f32::floor(self)
	}

	fn epsilon() -> f32 {
		f32::EPSILON
	}

	fn pi() -> f32 {
		std::f32::consts::PI
	}

	fn zero() -> f32 {
		0.0
	}

	fn one() -> f32 {
		1.0
	}

	fn two() -> f32 {
		2.0
	}

	fn rem(self, other: f32) -> f32 {
		self - (self / other).floor() * other
	}

	fn round(self) -> f32 {
		self.round()
	}

	fn cmp(self, b: f32) -> std::cmp::Ordering {
		self.partial_cmp(&b).unwrap()
	}
}

impl Numeric for f64 {
	fn dtype() -> &'static str {
		"f64"
	}

	fn to_usize(self) -> usize {
		self as usize
	}

	fn to_isize(self) -> isize {
		self as isize
	}

	fn to_u8(self) -> u8 {
		self as u8
	}

	fn to_u16(self) -> u16 {
		self as u16
	}

	fn to_u32(self) -> u32 {
		self as u32
	}

	fn to_u64(self) -> u64 {
		self as u64
	}

	fn to_i8(self) -> i8 {
		self as i8
	}

	fn to_i16(self) -> i16 {
		self as i16
	}

	fn to_i32(self) -> i32 {
		self as i32
	}

	fn to_i64(self) -> i64 {
		self as i64
	}

	fn to_f32(self) -> f32 {
		self as f32
	}

	fn to_f64(self) -> f64 {
		self
	}

	fn from_usize(v: usize) -> f64 {
		v as f64
	}

	fn from_isize(v: isize) -> f64 {
		v as f64
	}

	fn from_u8(v: u8) -> f64 {
		v as f64
	}

	fn from_u16(v: u16) -> f64 {
		v as f64
	}

	fn from_u32(v: u32) -> f64 {
		v as f64
	}

	fn from_u64(v: u64) -> f64 {
		v as f64
	}

	fn from_i8(v: i8) -> f64 {
		v as f64
	}

	fn from_i16(v: i16) -> f64 {
		v as f64
	}

	fn from_i32(v: i32) -> f64 {
		v as f64
	}

	fn from_i64(v: i64) -> f64 {
		v as f64
	}

	fn from_f32(v: f32) -> f64 {
		v as f64
	}

	fn from_f64(v: f64) -> f64 {
		v
	}

	fn infinity() -> f64 {
		f64::INFINITY
	}

	fn neg_infinity() -> f64 {
		f64::NEG_INFINITY
	}

	fn max_value() -> f64 {
		f64::MAX
	}

	fn min_value() -> f64 {
		f64::MIN
	}

	fn max(self, other: f64) -> f64 {
		f64::max(self, other)
	}

	fn min(self, other: f64) -> f64 {
		f64::min(self, other)
	}

	fn sqrt(self) -> f64 {
		f64::sqrt(self)
	}

	fn exp(self) -> f64 {
		f64::exp(self)
	}

	fn abs(self) -> f64 {
		f64::abs(self)
	}

	fn powf(self, exp: Self) -> Self {
		f64::powf(self, exp)
	}

	fn atan(self) -> Self {
		f64::atan(self)
	}

	fn atan2(self, y: Self) -> Self {
		f64::atan2(self, y)
	}

	fn ceil(self) -> f64 {
		f64::ceil(self)
	}

	fn floor(self) -> f64 {
		f64::floor(self)
	}

	fn epsilon() -> f64 {
		f64::EPSILON
	}

	fn pi() -> f64 {
		std::f64::consts::PI
	}

	fn zero() -> f64 {
		0.0
	}

	fn one() -> f64 {
		1.0
	}

	fn two() -> f64 {
		2.0
	}

	fn rem(self, other: f64) -> f64 {
		self - (self / other).floor() * other
	}

	fn round(self) -> f64 {
		self.round()
	}

	fn cmp(self, b: f64) -> std::cmp::Ordering {
		self.partial_cmp(&b).unwrap()
	}
}

impl Numeric for u8 {
	fn dtype() -> &'static str {
		"u8"
	}

	fn to_usize(self) -> usize {
		self as usize
	}

	fn to_isize(self) -> isize {
		self as isize
	}

	fn to_u8(self) -> u8 {
		self
	}

	fn to_u16(self) -> u16 {
		self as u16
	}

	fn to_u32(self) -> u32 {
		self as u32
	}

	fn to_u64(self) -> u64 {
		self as u64
	}

	fn to_i8(self) -> i8 {
		self as i8
	}

	fn to_i16(self) -> i16 {
		self as i16
	}

	fn to_i32(self) -> i32 {
		self as i32
	}

	fn to_i64(self) -> i64 {
		self as i64
	}

	fn to_f32(self) -> f32 {
		self as f32
	}

	fn to_f64(self) -> f64 {
		self as f64
	}

	fn from_usize(v: usize) -> u8 {
		v as u8
	}

	fn from_isize(v: isize) -> u8 {
		v as u8
	}

	fn from_u8(v: u8) -> u8 {
		v
	}

	fn from_u16(v: u16) -> u8 {
		v as u8
	}

	fn from_u32(v: u32) -> u8 {
		v as u8
	}

	fn from_u64(v: u64) -> u8 {
		v as u8
	}

	fn from_i8(v: i8) -> u8 {
		v as u8
	}

	fn from_i16(v: i16) -> u8 {
		v as u8
	}

	fn from_i32(v: i32) -> u8 {
		v as u8
	}

	fn from_i64(v: i64) -> u8 {
		v as u8
	}

	fn from_f32(v: f32) -> u8 {
		v as u8
	}

	fn from_f64(v: f64) -> u8 {
		v as u8
	}

	fn infinity() -> u8 {
		u8::MAX
	}

	fn neg_infinity() -> u8 {
		u8::MIN
	}

	fn max_value() -> u8 {
		u8::MAX
	}

	fn min_value() -> u8 {
		u8::MIN
	}

	fn sqrt(self) -> u8 {
		(self as f32).sqrt() as u8
	}

	fn exp(self) -> u8 {
		(self as f32).exp() as u8
	}

	fn abs(self) -> u8 {
		self
	}

	fn powf(self, exp: Self) -> Self {
		(self as f32).powf(exp as f32) as u8
	}

	fn atan(self) -> Self {
		(self as f32).atan() as u8
	}

	fn atan2(self, y: Self) -> Self {
		(self as f32).atan2(y as f32) as u8
	}

	fn ceil(self) -> u8 {
		(self as f32).ceil() as u8
	}

	fn floor(self) -> u8 {
		(self as f32).floor() as u8
	}

	fn epsilon() -> u8 {
		0
	}

	fn pi() -> u8 {
		std::f32::consts::PI as u8
	}

	fn zero() -> u8 {
		0
	}


	fn one() -> u8 {
		1
	}

	fn two() -> u8 {
		2
	}

	fn rem(self, other: u8) -> u8 {
		self - (self / other) * other
	}

	fn round(self) -> u8 {
		self
	}

	fn cmp(self, b: u8) -> std::cmp::Ordering {
		self.partial_cmp(&b).unwrap()
	}
}

impl Numeric for u16 {
	fn dtype() -> &'static str {
		"u16"
	}

	fn to_usize(self) -> usize {
		self as usize
	}

	fn to_isize(self) -> isize {
		self as isize
	}

	fn to_u8(self) -> u8 {
		self as u8
	}

	fn to_u16(self) -> u16 {
		self
	}

	fn to_u32(self) -> u32 {
		self as u32
	}

	fn to_u64(self) -> u64 {
		self as u64
	}

	fn to_i8(self) -> i8 {
		self as i8
	}

	fn to_i16(self) -> i16 {
		self as i16
	}

	fn to_i32(self) -> i32 {
		self as i32
	}

	fn to_i64(self) -> i64 {
		self as i64
	}

	fn to_f32(self) -> f32 {
		self as f32
	}

	fn to_f64(self) -> f64 {
		self as f64
	}

	fn from_usize(v: usize) -> u16 {
		v as u16
	}

	fn from_isize(v: isize) -> u16 {
		v as u16
	}

	fn from_u8(v: u8) -> u16 {
		v as u16
	}

	fn from_u16(v: u16) -> u16 {
		v
	}

	fn from_u32(v: u32) -> u16 {
		v as u16
	}

	fn from_u64(v: u64) -> u16 {
		v as u16
	}

	fn from_i8(v: i8) -> u16 {
		v as u16
	}

	fn from_i16(v: i16) -> u16 {
		v as u16
	}

	fn from_i32(v: i32) -> u16 {
		v as u16
	}

	fn from_i64(v: i64) -> u16 {
		v as u16
	}

	fn from_f32(v: f32) -> u16 {
		v as u16
	}

	fn from_f64(v: f64) -> u16 {
		v as u16
	}

	fn infinity() -> u16 {
		u16::MAX
	}

	fn neg_infinity() -> u16 {
		u16::MIN
	}

	fn max_value() -> u16 {
		u16::MAX
	}

	fn min_value() -> u16 {
		u16::MIN
	}

	fn sqrt(self) -> u16 {
		(self as f32).sqrt() as u16
	}

	fn exp(self) -> u16 {
		(self as f32).exp() as u16
	}

	fn abs(self) -> u16 {
		self
	}

	fn powf(self, exp: Self) -> Self {
		(self as f32).powf(exp as f32) as u16
	}

	fn atan(self) -> Self {
		(self as f32).atan() as u16
	}

	fn atan2(self, y: Self) -> Self {
		(self as f32).atan2(y as f32) as u16
	}

	fn ceil(self) -> u16 {
		(self as f32).ceil() as u16
	}

	fn floor(self) -> u16 {
		(self as f32).floor() as u16
	}

	fn epsilon() -> u16 {
		0
	}

	fn pi() -> u16 {
		std::f32::consts::PI as u16
	}

	fn zero() -> u16 {
		0
	}

	fn one() -> u16 {
		1
	}

	fn two() -> u16 {
		2
	}

	fn rem(self, other: u16) -> u16 {
		self - (self / other) * other
	}

	fn round(self) -> u16 {
		self
	}

	fn cmp(self, b: u16) -> std::cmp::Ordering {
		self.partial_cmp(&b).unwrap()
	}
}

impl Numeric for u32 {
	fn dtype() -> &'static str {
		"u32"
	}

	fn to_usize(self) -> usize {
		self as usize
	}

	fn to_isize(self) -> isize {
		self as isize
	}

	fn to_u8(self) -> u8 {
		self as u8
	}

	fn to_u16(self) -> u16 {
		self as u16
	}

	fn to_u32(self) -> u32 {
		self
	}

	fn to_u64(self) -> u64 {
		self as u64
	}

	fn to_i8(self) -> i8 {
		self as i8
	}

	fn to_i16(self) -> i16 {
		self as i16
	}

	fn to_i32(self) -> i32 {
		self as i32
	}

	fn to_i64(self) -> i64 {
		self as i64
	}

	fn to_f32(self) -> f32 {
		self as f32
	}

	fn to_f64(self) -> f64 {
		self as f64
	}

	fn from_usize(v: usize) -> u32 {
		v as u32
	}

	fn from_isize(v: isize) -> u32 {
		v as u32
	}

	fn from_u8(v: u8) -> u32 {
		v as u32
	}

	fn from_u16(v: u16) -> u32 {
		v as u32
	}

	fn from_u32(v: u32) -> u32 {
		v
	}

	fn from_u64(v: u64) -> u32 {
		v as u32
	}

	fn from_i8(v: i8) -> u32 {
		v as u32
	}

	fn from_i16(v: i16) -> u32 {
		v as u32
	}

	fn from_i32(v: i32) -> u32 {
		v as u32
	}

	fn from_i64(v: i64) -> u32 {
		v as u32
	}

	fn from_f32(v: f32) -> u32 {
		v as u32
	}

	fn from_f64(v: f64) -> u32 {
		v as u32
	}

	fn infinity() -> u32 {
		u32::MAX
	}

	fn neg_infinity() -> u32 {
		u32::MIN
	}

	fn max_value() -> u32 {
		u32::MAX
	}

	fn min_value() -> u32 {
		u32::MIN
	}

	fn sqrt(self) -> u32 {
		(self as f32).sqrt() as u32
	}

	fn exp(self) -> u32 {
		(self as f32).exp() as u32
	}

	fn abs(self) -> u32 {
		self
	}

	fn powf(self, exp: Self) -> Self {
		(self as f32).powf(exp as f32) as u32
	}

	fn atan(self) -> Self {
		(self as f32).atan() as u32
	}

	fn atan2(self, y: Self) -> Self {
		(self as f32).atan2(y as f32) as u32
	}

	fn ceil(self) -> u32 {
		(self as f32).ceil() as u32
	}

	fn floor(self) -> u32 {
		(self as f32).floor() as u32
	}

	fn epsilon() -> u32 {
		0
	}

	fn pi() -> u32 {
		std::f32::consts::PI as u32
	}

	fn zero() -> u32 {
		0
	}

	fn one() -> u32 {
		1
	}

	fn two() -> u32 {
		2
	}

	fn rem(self, other: u32) -> u32 {
		self - (self / other) * other
	}

	fn round(self) -> u32 {
		self
	}

	fn cmp(self, b: u32) -> std::cmp::Ordering {
		self.partial_cmp(&b).unwrap()
	}
}

impl Numeric for u64 {
	fn dtype() -> &'static str {
		"u64"
	}

	fn to_usize(self) -> usize {
		self as usize
	}

	fn to_isize(self) -> isize {
		self as isize
	}

	fn to_u8(self) -> u8 {
		self as u8
	}

	fn to_u16(self) -> u16 {
		self as u16
	}

	fn to_u32(self) -> u32 {
		self as u32
	}

	fn to_u64(self) -> u64 {
		self
	}

	fn to_i8(self) -> i8 {
		self as i8
	}

	fn to_i16(self) -> i16 {
		self as i16
	}

	fn to_i32(self) -> i32 {
		self as i32
	}

	fn to_i64(self) -> i64 {
		self as i64
	}

	fn to_f32(self) -> f32 {
		self as f32
	}

	fn to_f64(self) -> f64 {
		self as f64
	}

	fn from_usize(v: usize) -> u64 {
		v as u64
	}

	fn from_isize(v: isize) -> u64 {
		v as u64
	}

	fn from_u8(v: u8) -> u64 {
		v as u64
	}

	fn from_u16(v: u16) -> u64 {
		v as u64
	}

	fn from_u32(v: u32) -> u64 {
		v as u64
	}

	fn from_u64(v: u64) -> u64 {
		v
	}

	fn from_i8(v: i8) -> u64 {
		v as u64
	}

	fn from_i16(v: i16) -> u64 {
		v as u64
	}

	fn from_i32(v: i32) -> u64 {
		v as u64
	}

	fn from_i64(v: i64) -> u64 {
		v as u64
	}

	fn from_f32(v: f32) -> u64 {
		v as u64
	}

	fn from_f64(v: f64) -> u64 {
		v as u64
	}

	fn infinity() -> u64 {
		u64::MAX
	}

	fn neg_infinity() -> u64 {
		u64::MIN
	}

	fn max_value() -> u64 {
		u64::MAX
	}

	fn min_value() -> u64 {
		u64::MIN
	}

	fn sqrt(self) -> u64 {
		(self as f64).sqrt() as u64
	}

	fn exp(self) -> u64 {
		(self as f64).exp() as u64
	}

	fn abs(self) -> u64 {
		self
	}

	fn powf(self, exp: Self) -> Self {
		(self as f64).powf(exp as f64) as u64
	}

	fn atan(self) -> Self {
		(self as f64).atan() as u64
	}

	fn atan2(self, y: Self) -> Self {
		(self as f64).atan2(y as f64) as u64
	}

	fn ceil(self) -> u64 {
		(self as f64).ceil() as u64
	}

	fn floor(self) -> u64 {
		(self as f64).floor() as u64
	}

	fn epsilon() -> u64 {
		0
	}

	fn pi() -> u64 {
		std::f64::consts::PI as u64
	}

	fn zero() -> u64 {
		0
	}

	fn one() -> u64 {
		1
	}

	fn two() -> u64 {
		2
	}

	fn rem(self, other: u64) -> u64 {
		self - (self / other) * other
	}

	fn round(self) -> u64 {
		self
	}

	fn cmp(self, b: u64) -> std::cmp::Ordering {
		self.partial_cmp(&b).unwrap()
	}
}

impl Numeric for i8 {
	fn dtype() -> &'static str {
		"i8"
	}

	fn to_usize(self) -> usize {
		self as usize
	}

	fn to_isize(self) -> isize {
		self as isize
	}

	fn to_u8(self) -> u8 {
		self as u8
	}

	fn to_u16(self) -> u16 {
		self as u16
	}

	fn to_u32(self) -> u32 {
		self as u32
	}

	fn to_u64(self) -> u64 {
		self as u64
	}

	fn to_i8(self) -> i8 {
		self
	}

	fn to_i16(self) -> i16 {
		self as i16
	}

	fn to_i32(self) -> i32 {
		self as i32
	}

	fn to_i64(self) -> i64 {
		self as i64
	}

	fn to_f32(self) -> f32 {
		self as f32
	}

	fn to_f64(self) -> f64 {
		self as f64
	}

	fn from_usize(v: usize) -> i8 {
		v as i8
	}

	fn from_isize(v: isize) -> i8 {
		v as i8
	}

	fn from_u8(v: u8) -> i8 {
		v as i8
	}

	fn from_u16(v: u16) -> i8 {
		v as i8
	}

	fn from_u32(v: u32) -> i8 {
		v as i8
	}

	fn from_u64(v: u64) -> i8 {
		v as i8
	}

	fn from_i8(v: i8) -> i8 {
		v
	}

	fn from_i16(v: i16) -> i8 {
		v as i8
	}

	fn from_i32(v: i32) -> i8 {
		v as i8
	}

	fn from_i64(v: i64) -> i8 {
		v as i8
	}

	fn from_f32(v: f32) -> i8 {
		v as i8
	}

	fn from_f64(v: f64) -> i8 {
		v as i8
	}

	fn infinity() -> i8 {
		i8::MAX
	}

	fn neg_infinity() -> i8 {
		i8::MIN
	}

	fn max_value() -> i8 {
		i8::MAX
	}

	fn min_value() -> i8 {
		i8::MIN
	}

	fn sqrt(self) -> i8 {
		(self as f32).sqrt() as i8
	}

	fn exp(self) -> i8 {
		(self as f32).exp() as i8
	}

	fn abs(self) -> i8 {
		self.abs()
	}

	fn powf(self, exp: Self) -> Self {
		(self as f32).powf(exp as f32) as i8
	}

	fn atan(self) -> Self {
		(self as f32).atan() as i8
	}

	fn atan2(self, y: Self) -> Self {
		(self as f32).atan2(y as f32) as i8
	}

	fn ceil(self) -> i8 {
		(self as f32).ceil() as i8
	}

	fn floor(self) -> i8 {
		(self as f32).floor() as i8
	}

	fn epsilon() -> i8 {
		0
	}

	fn pi() -> i8 {
		std::f32::consts::PI as i8
	}

	fn zero() -> i8 {
		0
	}

	fn one() -> i8 {
		1
	}

	fn two() -> i8 {
		2
	}

	fn rem(self, other: i8) -> i8 {
		self - (self / other) * other
	}

	fn round(self) -> i8 {
		self
	}

	fn cmp(self, b: i8) -> std::cmp::Ordering {
		self.partial_cmp(&b).unwrap()
	}
}

impl Numeric for i16 {
	fn dtype() -> &'static str {
		"i16"
	}

	fn to_usize(self) -> usize {
		self as usize
	}

	fn to_isize(self) -> isize {
		self as isize
	}

	fn to_u8(self) -> u8 {
		self as u8
	}

	fn to_u16(self) -> u16 {
		self as u16
	}

	fn to_u32(self) -> u32 {
		self as u32
	}

	fn to_u64(self) -> u64 {
		self as u64
	}

	fn to_i8(self) -> i8 {
		self as i8
	}

	fn to_i16(self) -> i16 {
		self
	}

	fn to_i32(self) -> i32 {
		self as i32
	}

	fn to_i64(self) -> i64 {
		self as i64
	}

	fn to_f32(self) -> f32 {
		self as f32
	}

	fn to_f64(self) -> f64 {
		self as f64
	}

	fn from_usize(v: usize) -> i16 {
		v as i16
	}

	fn from_isize(v: isize) -> i16 {
		v as i16
	}

	fn from_u8(v: u8) -> i16 {
		v as i16
	}

	fn from_u16(v: u16) -> i16 {
		v as i16
	}

	fn from_u32(v: u32) -> i16 {
		v as i16
	}

	fn from_u64(v: u64) -> i16 {
		v as i16
	}

	fn from_i8(v: i8) -> i16 {
		v as i16
	}

	fn from_i16(v: i16) -> i16 {
		v
	}

	fn from_i32(v: i32) -> i16 {
		v as i16
	}

	fn from_i64(v: i64) -> i16 {
		v as i16
	}

	fn from_f32(v: f32) -> i16 {
		v as i16
	}

	fn from_f64(v: f64) -> i16 {
		v as i16
	}

	fn infinity() -> i16 {
		i16::MAX
	}

	fn neg_infinity() -> i16 {
		i16::MIN
	}

	fn max_value() -> i16 {
		i16::MAX
	}

	fn min_value() -> i16 {
		i16::MIN
	}

	fn sqrt(self) -> i16 {
		(self as f32).sqrt() as i16
	}

	fn exp(self) -> i16 {
		(self as f32).exp() as i16
	}

	fn abs(self) -> i16 {
		self.abs()
	}

	fn powf(self, exp: Self) -> Self {
		(self as f32).powf(exp as f32) as i16
	}

	fn atan(self) -> Self {
		(self as f32).atan() as i16
	}

	fn atan2(self, y: Self) -> Self {
		(self as f32).atan2(y as f32) as i16
	}

	fn ceil(self) -> i16 {
		(self as f32).ceil() as i16
	}

	fn floor(self) -> i16 {
		(self as f32).floor() as i16
	}

	fn epsilon() -> i16 {
		0
	}

	fn pi() -> i16 {
		std::f32::consts::PI as i16
	}

	fn zero() -> i16 {
		0
	}

	fn one() -> i16 {
		1
	}

	fn two() -> i16 {
		2
	}

	fn rem(self, other: i16) -> i16 {
		self - (self / other) * other
	}

	fn round(self) -> i16 {
		self
	}

	fn cmp(self, b: i16) -> std::cmp::Ordering {
		self.partial_cmp(&b).unwrap()
	}
}

impl Numeric for i32 {
	fn dtype() -> &'static str {
		"i32"
	}

	fn to_usize(self) -> usize {
		self as usize
	}

	fn to_isize(self) -> isize {
		self as isize
	}

	fn to_u8(self) -> u8 {
		self as u8
	}

	fn to_u16(self) -> u16 {
		self as u16
	}

	fn to_u32(self) -> u32 {
		self as u32
	}

	fn to_u64(self) -> u64 {
		self as u64
	}

	fn to_i8(self) -> i8 {
		self as i8
	}

	fn to_i16(self) -> i16 {
		self as i16
	}

	fn to_i32(self) -> i32 {
		self
	}

	fn to_i64(self) -> i64 {
		self as i64
	}

	fn to_f32(self) -> f32 {
		self as f32
	}

	fn to_f64(self) -> f64 {
		self as f64
	}

	fn from_usize(v: usize) -> i32 {
		v as i32
	}

	fn from_isize(v: isize) -> i32 {
		v as i32
	}

	fn from_u8(v: u8) -> i32 {
		v as i32
	}

	fn from_u16(v: u16) -> i32 {
		v as i32
	}

	fn from_u32(v: u32) -> i32 {
		v as i32
	}

	fn from_u64(v: u64) -> i32 {
		v as i32
	}

	fn from_i8(v: i8) -> i32 {
		v as i32
	}

	fn from_i16(v: i16) -> i32 {
		v as i32
	}

	fn from_i32(v: i32) -> i32 {
		v
	}

	fn from_i64(v: i64) -> i32 {
		v as i32
	}

	fn from_f32(v: f32) -> i32 {
		v as i32
	}

	fn from_f64(v: f64) -> i32 {
		v as i32
	}

	fn infinity() -> i32 {
		i32::MAX
	}

	fn neg_infinity() -> i32 {
		i32::MIN
	}

	fn max_value() -> i32 {
		i32::MAX
	}

	fn min_value() -> i32 {
		i32::MIN
	}

	fn sqrt(self) -> i32 {
		(self as f64).sqrt() as i32
	}

	fn exp(self) -> i32 {
		(self as f64).exp() as i32
	}

	fn abs(self) -> i32 {
		self.abs()
	}

	fn powf(self, exp: Self) -> Self {
		(self as f64).powf(exp as f64) as i32
	}

	fn atan(self) -> Self {
		(self as f64).atan() as i32
	}

	fn atan2(self, y: Self) -> Self {
		(self as f64).atan2(y as f64) as i32
	}

	fn ceil(self) -> i32 {
		(self as f64).ceil() as i32
	}

	fn floor(self) -> i32 {
		(self as f64).floor() as i32
	}

	fn epsilon() -> i32 {
		0
	}

	fn pi() -> i32 {
		std::f64::consts::PI as i32
	}

	fn zero() -> i32 {
		0
	}

	fn one() -> i32 {
		1
	}

	fn two() -> i32 {
		2
	}

	fn rem(self, other: i32) -> i32 {
		self - (self / other) * other
	}

	fn round(self) -> i32 {
		self
	}

	fn cmp(self, b: i32) -> std::cmp::Ordering {
		self.partial_cmp(&b).unwrap()
	}
}

impl Numeric for i64 {
	fn dtype() -> &'static str {
		"i64"
	}

	fn to_usize(self) -> usize {
		self as usize
	}

	fn to_isize(self) -> isize {
		self as isize
	}

	fn to_u8(self) -> u8 {
		self as u8
	}

	fn to_u16(self) -> u16 {
		self as u16
	}

	fn to_u32(self) -> u32 {
		self as u32
	}

	fn to_u64(self) -> u64 {
		self as u64
	}

	fn to_i8(self) -> i8 {
		self as i8
	}

	fn to_i16(self) -> i16 {
		self as i16
	}

	fn to_i32(self) -> i32 {
		self as i32
	}

	fn to_i64(self) -> i64 {
		self
	}

	fn to_f32(self) -> f32 {
		self as f32
	}

	fn to_f64(self) -> f64 {
		self as f64
	}

	fn from_usize(v: usize) -> i64 {
		v as i64
	}

	fn from_isize(v: isize) -> i64 {
		v as i64
	}

	fn from_u8(v: u8) -> i64 {
		v as i64
	}

	fn from_u16(v: u16) -> i64 {
		v as i64
	}

	fn from_u32(v: u32) -> i64 {
		v as i64
	}

	fn from_u64(v: u64) -> i64 {
		v as i64
	}

	fn from_i8(v: i8) -> i64 {
		v as i64
	}

	fn from_i16(v: i16) -> i64 {
		v as i64
	}

	fn from_i32(v: i32) -> i64 {
		v as i64
	}

	fn from_i64(v: i64) -> i64 {
		v
	}

	fn from_f32(v: f32) -> i64 {
		v as i64
	}

	fn from_f64(v: f64) -> i64 {
		v as i64
	}

	fn infinity() -> i64 {
		i64::MAX
	}

	fn neg_infinity() -> i64 {
		i64::MIN
	}

	fn max_value() -> i64 {
		i64::MAX
	}

	fn min_value() -> i64 {
		i64::MIN
	}

	fn sqrt(self) -> i64 {
		(self as f64).sqrt() as i64
	}

	fn exp(self) -> i64 {
		(self as f64).exp() as i64
	}

	fn abs(self) -> i64 {
		self.abs()
	}

	fn powf(self, exp: Self) -> Self {
		(self as f64).powf(exp as f64) as i64
	}

	fn atan(self) -> Self {
		(self as f64).atan() as i64
	}

	fn atan2(self, y: Self) -> Self {
		(self as f64).atan2(y as f64) as i64
	}

	fn ceil(self) -> i64 {
		(self as f64).ceil() as i64
	}

	fn floor(self) -> i64 {
		(self as f64).floor() as i64
	}

	fn epsilon() -> i64 {
		0
	}

	fn pi() -> i64 {
		std::f64::consts::PI as i64
	}

	fn zero() -> i64 {
		0
	}

	fn one() -> i64 {
		1
	}

	fn two() -> i64 {
		2
	}

	fn rem(self, other: i64) -> i64 {
		self - (self / other) * other
	}

	fn round(self) -> i64 {
		self
	}

	fn cmp(self, b: i64) -> std::cmp::Ordering {
		self.partial_cmp(&b).unwrap()
	}
}
