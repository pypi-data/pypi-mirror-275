// Utility functions for general use
use chrono;
use colored::*;
use kdam::{tqdm, Bar};

use crate::Numeric;

pub fn vector_multiply<T>(v1: &[T], v2: &[T]) -> Vec<T>
where
    T: std::ops::Mul<Output = T> + Copy,
{
    if v1.len() != v2.len() {
        panic!("Cannot multiply vectors of different lengths!")
    }

    v1.iter().zip(v2).map(|(&i1, &i2)| i1 * i2).collect()
}

pub fn is_shape_closed<T: Numeric>(points: &[[T; 2]]) -> bool {
    points[0] == points[points.len()-1]
}

pub fn is_valid_string(s: &str, valid_chars: &[char]) -> bool {
    for c in s.chars() {
        if !valid_chars.contains(&c) {
            return false;
        }
    }
    true
}

pub fn is_not_directory(path: &str, error_msg: &str) {
    if std::fs::metadata(path)
        .expect("Failed to read metadata")
        .is_dir()
    {
        println!("{}", error_msg);
        std::process::exit(1);
    }
}

pub fn does_parent_dir_exist(path: &str, error_msg: &str) {
    if let Some(parent_dir) = std::path::Path::new(path).parent() {
        if !parent_dir.exists() {
            println!("{}", error_msg);
            std::process::exit(1);
        }
    }
}

#[macro_export]
macro_rules! print_points {
    ($matrix:expr) => {
        for i in 0..$matrix.nrows() {
            print!("[{:6.2},{:6.2}]", $matrix[(i, 0)], $matrix[(i, 1)]);
            println!();
        }
    };
}

pub fn progress_bar(n: usize, desc: &str) -> Bar {
    let pb = tqdm!(
        total = n,
        force_refresh = true,
        desc = progress_timestamp(desc),
        animation = "arrow",
        bar_format = "{desc suffix=' '}|{animation}|{count}/{total} [{percentage:.0}%] in {elapsed human=true} ({rate:.1}/s, eta: {remaining human=true})"
    );
    pb
}

/// Progress log specifying current timestamp
pub fn progress_timestamp(desc: &str) -> String {
    let time = chrono::Local::now();
    let ymd = time.format("%Y-%m-%dT").to_string();
    let ymd = &ymd[..ymd.len() - 1];
    let hms = time.format("%H:%M:%S").to_string();
    let time = format!("{} | {}", ymd, hms);

    format!(
        "{} {} {} {} {} {}", 
        "[".bold(),
        time, 
        "|".bold(),
        "fqmv".truecolor(255, 187, 0).bold(), 
        "]".bold(),
        desc
    )
}

/// A macro for the progress timestamp to print to stdout
#[macro_export]
macro_rules! progress_log {
    ($desc:expr) => {
        println!("{}", fqmv_core::helpers::progress_timestamp($desc));
    };
}

/// A function for the progress timestamp to print to stdout
pub fn progress_log(desc: &str) {
    println!("{}", progress_timestamp(desc));
}

/// Formats a positive number with commas
pub fn thousands_format<T>(number: T) -> String where T: std::fmt::Display {
    let number = number.to_string();
    if number.len() > 4 {        
        number.as_bytes()
        .rchunks(3)
        .rev()
        .map(std::str::from_utf8)
        .collect::<Result<Vec<&str>, _>>()
        .unwrap()
        .join(",")
    } else {
        number.to_string()
    }
}
