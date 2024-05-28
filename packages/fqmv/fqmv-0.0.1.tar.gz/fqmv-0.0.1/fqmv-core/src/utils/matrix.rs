// Structs for defining matrices and operations on them

/// A flat matrix representation with standard 2-dimensional indexing
///
/// # Examples
/// 
/// ```no_run
/// use fqmv_core::utils::matrix::Matrix;
/// let mut matrix = Matrix::new(3, 3);
/// matrix[(0, 0)] = 1.0;
/// assert_eq!(matrix[(0, 0)], 1.0);
/// ```
#[derive(Debug, Clone)]
pub struct Matrix {
    pub data: Vec<f64>,
    pub rows: usize,
    pub cols: usize,
}

impl Matrix {
    pub fn new(rows: usize, cols: usize) -> Self {
        let data = vec![0.0; rows * cols];
        Self { data, rows, cols }
    }

    pub fn dimensions(self) -> (usize, usize) {
        (self.rows, self.cols)
    }

    pub fn max(&self) -> f64 {
        *self.data.iter().max_by(|a, b| a.total_cmp(b)).unwrap()
    }

    pub fn min(&self) -> f64 {
        *self.data.iter().min_by(|a, b| a.total_cmp(b)).unwrap()
    }

    pub fn sum(&self) -> f64 {
        self.data.iter().sum()
    }

    pub fn row_sum(&self) -> Vec<f64> {
        let mut row_sum = vec![0.0; self.rows];
        for i in 0..self.rows {
            for j in 0..self.cols {
                row_sum[i] += self[(i, j)];
            }
        }
        row_sum
    }

    pub fn col_sum(&self) -> Vec<f64> {
        let mut col_sum = vec![0.0; self.cols];
        for i in 0..self.cols {
            for j in 0..self.rows {
                col_sum[i] += self[(j, i)];
            }
        }
        col_sum
    }

    pub fn divide(&self, value: f64) -> Matrix {
        let mut result = Matrix::new(self.rows, self.cols);
        for i in 0..self.rows {
            for j in 0..self.cols {
                result[(i, j)] = self[(i, j)] / value;
            }
        }
        result
    }

    pub fn normalize(&mut self) {
        let sum: f64 = self.data.iter().sum();
        for i in 0..self.rows {
            for j in 0..self.cols {
                self[(i, j)] /= sum;
            }
        }
    }

    pub fn rescale(&mut self, min: f64, max: f64) {
        let current_min = self.min();
        let current_max = self.max();

        if min == max {
            println!("Warning: Minimum and maximum values cannot be equal");
            std::process::exit(1);
        }

        if current_min != min || current_max != max {
            for i in 0..self.cols {
                for j in 0..self.rows {
                    self[(j, i)] = (self[(j, i)] - current_min) / (current_max - current_min) * (max - min) + min;
                }
            }
        }
    }

}

impl std::ops::Index<(usize, usize)> for Matrix {
    type Output = f64;

    fn index(&self, index: (usize, usize)) -> &Self::Output {
        if index.0 >= self.rows || index.1 >= self.cols {
            panic!("Index out of bounds");
        }

        // (row, column) indexing
        let (row, col) = index;
        &self.data[row * self.cols + col]
    }
}

impl std::ops::IndexMut<(usize, usize)> for Matrix {
    fn index_mut(&mut self, index: (usize, usize)) -> &mut Self::Output {
        if index.0 >= self.rows || index.1 >= self.cols {
            panic!("Index out of bounds");
        }

        let (row, col) = index;
        &mut self.data[row * self.cols + col]
    }
}
