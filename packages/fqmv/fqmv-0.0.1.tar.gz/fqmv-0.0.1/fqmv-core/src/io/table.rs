/// Helper functions for reading and writing tables
use std::fs::File;
use polars::prelude::*;

/// Read a table from a CSV file
///
/// # Arguments
///
/// * `input` - A string containing the name of the input file
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::io::table::read_table_csv;
/// let df = read_table_csv("input.csv");
/// ```
pub fn read_table_csv(input: &str) -> PolarsResult<DataFrame> {
    CsvReader::from_path(input)?
        .has_header(true)
        .finish()
}

/// Read a table from a TSV file
///
/// # Arguments
///
/// * `input` - A string containing the name of the input file
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::io::table::read_table_tsv;
/// let df = read_table_tsv("input.tsv");
/// ```
pub fn read_table_tsv(input: &str) -> PolarsResult<DataFrame> {
    CsvReader::from_path(input)?
        .has_header(true)
        .with_separator("\t".as_bytes()[0])
        .finish()
}

/// Read a table from a parquet file
///
/// # Arguments
///
/// * `input` - A string containing the name of the input file
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::io::table::read_table_parquet;
/// let df = read_table_parquet("input.parquet");
/// ```
pub fn read_table_parquet(input: &str) -> PolarsResult<DataFrame> {
    let input_file = File::open(input).unwrap();
    ParquetReader::new(input_file).finish()
}

/// Read a table from a JSON file
///
/// # Arguments
///
/// * `input` - A string containing the name of the input file
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::io::table::read_table_json;
/// let df = read_table_json("input.json");
/// ```
pub fn read_table_json(input: &str) -> PolarsResult<DataFrame> {
    let input_file = File::open(input).unwrap();
    JsonReader::new(input_file).finish()
}

pub fn read_table(filename: &str) -> PolarsResult<DataFrame> {
    let format = filename.split('.').last().unwrap();
    match format {
        "csv" => read_table_csv(filename),
        "tsv" => read_table_tsv(filename),
        "txt" => read_table_tsv(filename),
        "json" => read_table_json(filename),
        "parquet" => read_table_parquet(filename),
        "pq" => read_table_parquet(filename),
        _ => panic!("Invalid table format. Supported formats are csv, tsv, txt, json, parquet/pq."),
    }
}

/// Write a table to a CSV file
/// 
/// # Arguments
///
/// * `df` - A DataFrame
/// * `output` - A string containing the name of the output file
/// * `header` - A boolean indicating whether the output file should contain a header
/// 
/// # Examples
///
/// ```no_run
/// use fqmv_core::io::table::{read_table, write_table_csv};
/// let mut df = read_table("input.csv").unwrap();
/// write_table_csv(&mut df, "output.csv", true)
/// ```
pub fn write_table_csv(df: &mut DataFrame, output: &str, header: bool) {
    let mut output_file: File = File::create(output).unwrap();
    CsvWriter::new(&mut output_file)
        .include_header(header)
        .finish(df)
        .unwrap();
}

/// Write a table to a TSV file
///
/// # Arguments
///
/// * `df` - A DataFrame
/// * `output` - A string containing the name of the output file
/// * `header` - A boolean indicating whether the output file should contain a header
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::io::table::{read_table, write_table_tsv};
/// let mut df = read_table("input.csv").unwrap();
/// write_table_tsv(&mut df, "output.tsv", true)
/// ```
pub fn write_table_tsv(df: &mut DataFrame, output: &str, header: bool) {
    let mut output_file: File = File::create(output).unwrap();
    CsvWriter::new(&mut output_file)
        .include_header(header)
        .with_separator("\t".as_bytes()[0])
        .finish(df)
        .unwrap();
}

/// Write a table to a parquet file
///
/// # Arguments
///
/// * `df` - A DataFrame
/// * `output` - A string containing the name of the output file
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::io::table::{read_table, write_table_parquet};
/// let mut df = read_table("input.csv").unwrap();
/// write_table_parquet(&mut df, "output.parquet")
/// ```
pub fn write_table_parquet(df: &mut DataFrame, output: &str) {
    let mut output_file: File = File::create(output).unwrap();
    ParquetWriter::new(&mut output_file)
        .finish(df)
        .unwrap();
}

/// Write a table to a JSON file
///
/// # Arguments
///
/// * `df` - A DataFrame
/// * `output` - A string containing the name of the output file
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::io::table::{read_table, write_table_json};
/// let mut df = read_table("input.csv").unwrap();
/// write_table_json(&mut df, "output.json")
/// ```
pub fn write_table_json(df: &mut DataFrame, output: &str) {
    let mut output_file: File = File::create(output).unwrap();
    JsonWriter::new(&mut output_file)
        .finish(df)
        .unwrap();
}

/// Save a vector of polar Series to a table
///
/// # Arguments
///
/// * `series` - A vector of polar Series
/// * `output` - A string containing the name of the output file
/// * `format` - A string containing the format of the output file (csv or parquet)
///
/// # Examples
///
/// ```no_run
/// use polars::prelude::*;
/// use fqmv_core::io::table::write_table_series;
/// let series = vec![
///     Series::new("a", &[1, 2, 3]),
///     Series::new("b", &[1, 1, 1]),
/// ];
/// write_table_series(series, "output.csv", "csv")
/// ```
pub fn write_table_series(
    series: Vec<Series>,
    output: &str,
    format: &str,
) {
    let mut df = DataFrame::new(series).unwrap();
    match format {
        "csv" => write_table_csv(&mut df, output, true),
        "tsv" => write_table_tsv(&mut df, output, true),
        "txt" => write_table_tsv(&mut df, output, true),
        "parquet" => write_table_parquet(&mut df, output),
        "pq" => write_table_parquet(&mut df, output),
        "json" => write_table_json(&mut df, output),
        _ => {
            println!("Invalid format. Only csv, tsv, txt, json, or parquet files are supported.");
            std::process::exit(1);
        }
    }
}

/// Write a DataFrame to disk
///
/// # Arguments
///
/// * `df` - A DataFrame
/// * `output` - A string containing the name of the output file
/// * `id` - An optional string specifying a single id to prepend as first column
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::io::table::{read_table, write_table};
/// let mut df = read_table("input.csv").unwrap();
/// write_table(&mut df, "output.csv")
/// ```
pub fn write_table(df: &mut DataFrame, output: &str) {
    let format = output.split('.').last().unwrap();
    match format {
        "csv" => write_table_csv(df, output, true),
        "tsv" => write_table_tsv(df, output, true),
        "txt" => write_table_tsv(df, output, true),
        "parquet" => write_table_parquet(df, output),
        "pq" => write_table_parquet(df, output),
        "json" => write_table_json(df, output),
        _ => {
            println!("Invalid format. Only csv, tsv, txt, json, or parquet files are supported.");
            std::process::exit(1);
        }
    }
}

/// Save a set of continuous descriptors and associated identifiers to a table
///
/// # Arguments
///
/// * `data` - A vector of f64 vectors containing the columns of descriptors
/// * `data_columns` - A vector of strings containing the names of the descriptor columns
/// * `identifiers` - An optional DataFrame containing the identifiers
/// * `output` - A string containing the name of the output file
/// * `format` - A string containing the format of the output file (csv or parquet)
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::utils::toy;
/// use fqmv_core::io::table::read_table;
/// use fqmv_core::io::table::write_table_descriptors;
///
/// let descriptors = vec![vec![0.0, 1.0], vec![1.0, 2.0], vec![2.0, 3.0]];
/// let identifiers = read_table("identifiers.csv").unwrap();
///
/// write_table_descriptors(
///     &descriptors, 
///     &vec!["lag", "noise"], 
///     Some(&identifiers),
///     Some(vec!["sample_1", "sample_2", "sample_3"]),
///     "output.csv", 
/// )
/// ```
pub fn write_table_descriptors(
    data: &Vec<Vec<f64>>,
    data_columns: &Vec<&str>,
    identifiers: Option<&DataFrame>,
    names: Option<Vec<&str>>,
    output: &str,
) {
    let format = output.split('.').last().unwrap();
    if !identifiers.is_none() {
        let (nrows, _) = identifiers.unwrap().shape();
        if nrows != data.len() {
            println!("Error: The number of identifiers does not match the number of data vectors.");
            std::process::exit(1);
        }
    }

    if data[0].len() != data_columns.len() {
        println!("Error: The number of data columns must equal number of data vectors.");
        std::process::exit(1);
    }

    let mut series = vec![];
    for i in 0..data[0].len() {
        let mut column = vec![];
        for j in 0..data.len() {
            column.push(data[j][i]);
        }
        series.push(Series::new(data_columns[i], column));
    }

    let mut df = if !identifiers.is_none() {
        let df = DataFrame::new(series).unwrap();
        polars::functions::concat_df_horizontal(&[identifiers.unwrap().clone(), df]).unwrap()
    } else {
        DataFrame::new(series).unwrap()
    };

    if !names.is_none() {
        let names = Series::new("name", names.unwrap());
        let names_df = DataFrame::new(vec![names]).unwrap();
        df = polars::functions::concat_df_horizontal(&[names_df, df]).unwrap();
    }

    match format {
        "csv" => write_table_csv(&mut df, output, true),
        "tsv" => write_table_tsv(&mut df, output, true),
        "txt" => write_table_tsv(&mut df, output, true),
        "parquet" => write_table_parquet(&mut df, output),
        "pq" => write_table_parquet(&mut df, output),
        "json" => write_table_json(&mut df, output),
        _ => {
            println!("Invalid format. Only csv, tsv, txt, json, or parquet files are supported.");
            std::process::exit(1);
        }
    }
}
