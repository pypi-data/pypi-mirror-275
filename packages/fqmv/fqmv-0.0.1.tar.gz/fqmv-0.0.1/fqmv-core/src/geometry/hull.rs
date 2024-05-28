/// Implementations of various convex hull algorithms
use std::cmp::Ordering;

use crate::Numeric;

/// Computes the convex hull of a polygon using the Graham scan algorithm
///
/// # Arguments
/// 
/// * `points` - A vector of points defining the polygon
/// 
/// # Returns
/// 
/// A vector of ordered points defining the closed convex hull
///
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::geometry::hull;
/// let points = vec![[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0]];
/// let hull = hull::convex_hull_graham(&points);
/// ```
///
/// # References
///
/// 1. "An Efficient Algorithm for Determining the Convex Hull of a Finite
///    Planar Set". Information Processing Letters. R.L. Graham. (1972).
pub fn convex_hull_graham<T: Numeric>(points: &[[T; 2]]) -> Vec<[T; 2]> {
    // Convert matrix to Vec<[f64; 2]> in a single iter
    let mut candidates = points.to_owned();

    // Find the pivot point
    let mut index = 0;
    let mut px = points[0][0];
    let mut py = points[0][1];
    for (i, point) in points.iter().enumerate().skip(1) {
        if point[1] < py || (point[1] == py && point[0] < px) {
            px = point[0];
            py = point[1];
            index = i;
        }
    }

    candidates.swap(0, index);

    candidates.sort_by(|a, b| {                
        let cross_product = (a[1] - py) * (b[0] - a[0]) - (a[0] - px) * (b[1] - a[1]);
        if cross_product == T::zero() {
            let dist_a = (a[0] - px).powf(T::two()) + (a[1] - py).powf(T::two());
            let dist_b = (b[0] - px).powf(T::two()) + (b[1] - py).powf(T::two());
            if dist_a >= dist_b {
                Ordering::Less
            } else {
                Ordering::Greater
            }            
        } else {
            let dy_a = a[1] - py;
            let dx_a = a[0] - px;
            let dy_b = b[1] - py;
            let dx_b = b[0] - px;
            (dy_a.atan2(dx_a)).partial_cmp(&(dy_b.atan2(dx_b))).unwrap()
        }
    });

    let mut stack: Vec<[T; 2]> = candidates[0..1].to_vec();

    for point in candidates.iter().skip(1) {
        while stack.len() > 1 && stack_cross_product(point, &stack) < T::zero() {
            stack.pop();            
        }
                 
        if point != &stack[stack.len() - 1] {
            stack.push(*point);
        }
    }    

    if stack[0] != stack[stack.len()-1] {
        stack.push(stack[0]);
    }
    
    stack
}

/// Compute the cross product between a proposal point and points on current stack
/// 
/// # Arguments
/// 
/// * `point` - A point to be tested
/// * `stack` - A vector of points defining the current stack
/// 
/// # Notes
/// 
/// This is a helper function for the Graham scan algorithm
fn stack_cross_product<T: Numeric>(point: &[T; 2], stack: &[[T; 2]]) -> T {
    (stack[stack.len() - 1][0] - stack[stack.len() - 2][0]) 
    * (point[1] - stack[stack.len() - 2][1]) 
    - (stack[stack.len() - 1][1] - stack[stack.len() - 2][1]) 
    * (point[0] - stack[stack.len() - 2][0])
}
