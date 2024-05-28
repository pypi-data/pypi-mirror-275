use crate::Numeric;
use crate::geometry::hull;
use crate::helpers::is_shape_closed;
use crate::geometry::ellipse::fit_ellipse_lstsq as fit_ellipse;

/// Computes the area of a polygon using the shoelace formula 
/// 
/// # Arguments
/// 
/// * `points` - A vector of points defining the polygon
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::descriptors::form;
/// let points = vec![[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0], [0.0, 0.0]];
/// let area = form::polygon_area(&points);
/// ```
pub fn polygon_area<T: Numeric>(points: &[[T; 2]]) -> T {
    let mut area = T::zero();
    for i in 0..points.len() {
        if i == points.len()-1 {
            if points[i] == points[0] {
                break;
            } else {
                area += points[i][0] * points[0][1] - points[0][0] * points[i][1];
            }
        } else {
            area += points[i][0] * points[i+1][1] - points[i+1][0] * points[i][1];
        }
    }

    area.abs() / T::two() 
}

/// Computes the bounding box area of a polygon
/// 
/// # Arguments
/// 
/// * `points` - A vector of points defining the polygon
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::descriptors::form;
/// let points = vec![[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0], [0.0, 0.0]];
/// let area = form::polygon_area_bbox(&points);
/// ```
pub fn polygon_area_bbox<T: Numeric>(points: &[[T; 2]]) -> T {
    let (mut xmin, mut ymin) = (points[0][0], points[0][1]);
    let (mut xmax, mut ymax) = (points[0][0], points[0][1]);
    
    for point in points.iter().skip(1) {
        xmin = if point[0] < xmin {point[0]} else {xmin};
        ymin = if point[1] < ymin {point[1]} else {ymin};
        xmax = if point[0] > xmax {point[0]} else {xmax};
        ymax = if point[1] > ymax {point[1]} else {ymax};
    }

    (xmax - xmin) * (ymax - ymin)
}

/// Computes the elongation of a polygon
/// 
/// # Arguments
/// 
/// * `points` - A vector of points defining the polygon
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::descriptors::form;
/// let points = vec![[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0], [0.0, 0.0]];
/// let elongation = form::polygon_elongation(&points);
/// ```
pub fn polygon_elongation<T: Numeric>(points: &[[T; 2]]) -> T {
    let (mut xmin, mut ymin) = (points[0][0], points[0][1]);
    let (mut xmax, mut ymax) = (points[0][0], points[0][1]);
    
    for point in points.iter().skip(1) {
        xmin = if point[0] < xmin {point[0]} else {xmin};
        ymin = if point[1] < ymin {point[1]} else {ymin};
        xmax = if point[0] > xmax {point[0]} else {xmax};
        ymax = if point[1] > ymax {point[1]} else {ymax};
    }

    // Ensure measure is bounded between [0, 1]
    let elongation = (xmax - xmin) / (ymax - ymin);
    if elongation > T::one() {
        T::one() / elongation
    } else {
        elongation
    }
}

/// Computes the convex hull area of a polygon
/// 
/// # Arguments
/// 
/// * `points` - A vector of points defining the polygon
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::descriptors::form;
/// let points = vec![[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0], [0.0, 0.0]];
/// let area = form::polygon_area_convex(&points);
/// ```
pub fn polygon_area_convex<T: Numeric>(points: &[[T; 2]]) -> T {
    polygon_area(&hull::convex_hull_graham(points))
}

/// Computes the perimeter of a polygon
/// 
/// # Arguments
/// 
/// * `points` - A vector of points defining the polygon
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::descriptors::form;
/// let points = vec![[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0], [0.0, 0.0]];
/// let perimeter = form::polygon_perimeter(&points);
/// ```
pub fn polygon_perimeter<T: Numeric>(points: &[[T; 2]]) -> T {
    let mut perimeter = T::zero();

    for i in 0..points.len()-1 {
        perimeter += (
            (points[i][0] - points[i+1][0])
            * (points[i][0] - points[i+1][0])
            + (points[i][1] - points[i+1][1])
            * (points[i][1] - points[i+1][1])
        ).sqrt();
    }

    if !is_shape_closed(points) {
        perimeter += (
            (points[points.len()-1][0] - points[0][0])
            * (points[points.len()-1][0] - points[0][0])
            + (points[points.len()-1][1] - points[0][1])
            * (points[points.len()-1][1] - points[0][1])
        ).sqrt();
    }

    perimeter
}

/// Computes the thread length of a polygon
/// 
/// # Arguments
/// 
/// * `points` - A vector of points defining the polygon
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::descriptors::form;
/// let points = vec![[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0], [0.0, 0.0]];
/// let thread_length = form::polygon_thread_length(&points);
/// ```
pub fn polygon_thread_length<T: Numeric>(points: &[[T; 2]]) -> T {
    let perimeter = polygon_perimeter(points);
    let area = polygon_area(points);
    let left = perimeter.powf(T::two());
    let right = T::from_f64(16.0) * area;
    let coefficient = if left <= right {
        T::zero()
    } else {
        (left - right).sqrt()
    };

    (perimeter + coefficient) / T::from_f64(4.0)
}

/// Computes the thread width of a polygon
/// 
/// # Arguments
/// 
/// * `points` - A vector of points defining the polygon
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::descriptors::form;
/// let points = vec![[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0], [0.0, 0.0]];
/// let thread_width = form::polygon_thread_width(&points);
/// ```
pub fn polygon_thread_width<T: Numeric>(points: &[[T; 2]]) -> T {
    let perimeter = polygon_perimeter(points);
    let area = polygon_area(points);
    let left = perimeter.powf(T::two());
    let right = T::from_f64(16.0) * area;
    let coefficient = if left <= right {
        T::zero()
    } else {
        (left - right).sqrt()
    };
    
    let thread_length = (perimeter + coefficient) / T::from_f64(4.0);
    area / thread_length
}

/// Compute the solidity of a polygon
/// 
/// # Arguments
/// 
/// * `points` - A vector of points defining the polygon
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::descriptors::form;
/// let points = vec![[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0], [0.0, 0.0]];
/// let solidity = form::polygon_solidity(&points);
/// ```
pub fn polygon_solidity<T: Numeric>(points: &[[T; 2]]) -> T {
    polygon_area(points) / polygon_area_convex(points)
}

/// Compute the extent of a polygon
/// 
/// # Arguments
/// 
/// * `points` - A vector of points defining the polygon
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::descriptors::form;
/// let points = vec![[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0], [0.0, 0.0]];
/// let extent = form::polygon_extent(&points);
/// ```
pub fn polygon_extent<T: Numeric>(points: &[[T; 2]]) -> T {
    polygon_area(points) / polygon_area_bbox(points)
}

/// Compute the form factor of a polygon
/// 
/// # Arguments
/// 
/// * `points` - A vector of points defining the polygon
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::descriptors::form;
/// let points = vec![[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0], [0.0, 0.0]];
/// let form_factor = form::polygon_form_factor(&points);
/// ```
pub fn polygon_form_factor<T: Numeric>(points: &[[T; 2]]) -> T {
    let perimeter = polygon_perimeter(points);
    T::from_f64(4.0) * T::pi() * polygon_area(points) 
    / (perimeter * perimeter)
}

/// Compute the centroid of a polygon
/// 
/// # Arguments
/// 
/// * `points` - A vector of points defining the polygon
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::descriptors::form;
/// let points = vec![[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0], [0.0, 0.0]];
/// let centroid = form::polygon_centroid(&points);
/// ```
pub fn polygon_centroid<T: Numeric>(points: &[[T; 2]]) -> (T, T) {
    let (mut centroid_x, mut centroid_y) = (T::zero(), T::zero());
    let include_last = if is_shape_closed(points) {1} else {0};
    for i in 0..(points.len()-include_last) {
        centroid_x += points[i][0];
        centroid_y += points[i][1];
    }
    
    let n = T::from_usize(points.len() - include_last);
    centroid_x /= n;
    centroid_y /= n;

    (centroid_x, centroid_y)
}

/// Compute eccentricity of a polygon
///
/// # Arguments
///
/// * `points` - A vector of points defining the polygon
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::descriptors::form;
/// let points = vec![[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0], [0.0, 0.0]];
/// let eccentricity = form::polygon_eccentricity(&points);
/// ```
pub fn polygon_eccentricity<T: Numeric>(points: &[[T; 2]]) -> T {
    let ellipse = fit_ellipse(points);
    ellipse[2]
}

/// Compute major axis length of a polygon
///
/// # Arguments
///
/// * `points` - A vector of points defining the polygon
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::descriptors::form;
/// let points = vec![[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0], [0.0, 0.0]];
/// let major_axis_length = form::polygon_major_axis_length(&points);
/// ```
pub fn polygon_major_axis_length<T: Numeric>(points: &[[T; 2]]) -> T {
    let ellipse = fit_ellipse(points);
    ellipse[0]
}

/// Compute minor axis length of a polygon
///
/// # Arguments
///
/// * `points` - A vector of points defining the polygon
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::descriptors::form;
/// let points = vec![[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0], [0.0, 0.0]];
/// let minor_axis_length = form::polygon_minor_axis_length(&points);
/// ```
pub fn polygon_minor_axis_length<T: Numeric>(points: &[[T; 2]]) -> T {
    let ellipse = fit_ellipse(points);
    ellipse[1]
}

/// Compute the major axis curl of a polygon
///
/// # Arguments
///
/// * `points` - A vector of points defining the polygon
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::descriptors::form;
/// let points = vec![[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0], [0.0, 0.0]];
/// let curl_major = form::polygon_curl_major(&points);
/// ```
pub fn polygon_curl_major<T: Numeric>(points: &[[T; 2]]) -> T {
    let major_axis_length = polygon_major_axis_length(points);
    let thread_length = polygon_thread_length(points);
    major_axis_length / thread_length
}

/// Compute the bounding box length curl of a polygon
///
/// # Arguments
///
/// * `points` - A vector of points defining the polygon
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::descriptors::form;
/// let points = vec![[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0], [0.0, 0.0]];
/// let curl_bbox = form::polygon_curl_bbox(&points);
/// ```
pub fn polygon_curl_bbox<T: Numeric>(points: &[[T; 2]]) -> T {
    let (mut xmin, mut ymin) = (points[0][0], points[0][1]);
    let (mut xmax, mut ymax) = (points[0][0], points[0][1]);
    
    for point in points.iter().skip(1) {
        xmin = if point[0] < xmin {point[0]} else {xmin};
        ymin = if point[1] < ymin {point[1]} else {ymin};
        xmax = if point[0] > xmax {point[0]} else {xmax};
        ymax = if point[1] > ymax {point[1]} else {ymax};
    }

    let bbox_length = if (xmax - xmin) > (ymax - ymin) {
        xmax - xmin
    } else {
        ymax - ymin
    };

    let thread_length = polygon_thread_length(points);
    bbox_length / thread_length
}

/// Compute the equivalent diameter of a polygon
///
/// # Arguments
///
/// * `points` - A vector of points defining the polygon
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::descriptors::form;
/// let points = vec![[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0], [0.0, 0.0]];
/// let equivalent_diameter = form::polygon_equivalent_diameter(&points);
/// ```
pub fn polygon_equivalent_diameter<T: Numeric>(points: &[[T; 2]]) -> T {
    let area = polygon_area(points);
    let radius = (area / T::pi()).sqrt();
    radius * T::two() 
}

/// Compute the minimum radius of a polygon
///
/// # Arguments
///
/// * `points` - A vector of points defining the polygon
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::descriptors::form;
/// let points = vec![[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0], [0.0, 0.0]];
/// let minimum_radius = form::polygon_minimum_radius(&points);
/// ```
pub fn polygon_minimum_radius<T: Numeric>(points: &[[T; 2]]) -> T {
    let (x_centroid, y_centroid) = polygon_centroid(points);
    let mut minimum_radius = T::max_value(); 
    for point in points.iter() {
        let (x, y) = (point[0], point[1]);
        let distance = (x_centroid - x) * (x_centroid - x) + (y_centroid - y) * (y_centroid - y);        
        if distance < minimum_radius {
            minimum_radius = distance;
        }
    }
    minimum_radius.sqrt()
}

/// Compute the maximum radius of a polygon
///
/// # Arguments
///
/// * `points` - A vector of points defining the polygon
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::descriptors::form;
/// let points = vec![[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0], [0.0, 0.0]];
/// let maximum_radius = form::polygon_maximum_radius(&points);
/// ```
pub fn polygon_maximum_radius<T: Numeric>(points: &[[T; 2]]) -> T {
    let (x_centroid, y_centroid) = polygon_centroid(points);
    let mut maximum_radius = T::zero();
    for point in points.iter() {
        let (x, y) = (point[0], point[1]);
        let distance = (x_centroid - x) * (x_centroid - x) + (y_centroid - y) * (y_centroid - y);        
        if distance > maximum_radius {
            maximum_radius = distance;
        }
    }
    maximum_radius.sqrt()
}

/// Compute the mean radius of a polygon
///
/// # Arguments
///
/// * `points` - A vector of points defining the polygon
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::descriptors::form;
/// let points = vec![[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0], [0.0, 0.0]];
/// let mean_radius = form::polygon_mean_radius(&points);
/// ```
pub fn polygon_mean_radius<T: Numeric>(points: &[[T; 2]]) -> T {
    let (x_centroid, y_centroid) = polygon_centroid(points);
    let include_last = if is_shape_closed(points) {1} else {0};    
    let mut mean_radius = T::zero();
    for i in 0..(points.len()-include_last) {
        let (x, y) = (points[i][0], points[i][1]);
        let distance = (x_centroid - x) * (x_centroid - x) + (y_centroid - y) * (y_centroid - y);
        mean_radius += distance.sqrt();
    }    
    mean_radius /= T::from_usize(points.len() - include_last);
    mean_radius
}

/// Compute the maximum Feret diameter of a polygon
///
/// # Arguments
///
/// * `points` - A vector of points defining the polygon
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::descriptors::form;
/// let points = vec![[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0], [0.0, 0.0]];
/// let feret_diameter_maximum = form::polygon_feret_diameter_maximum(&points);
/// ```
pub fn polygon_feret_diameter_maximum<T: Numeric>(points: &[[T; 2]]) -> T {
    let norm = |x: [T; 2]| -> T {
        (x[0] * x[0] + x[1] * x[1]).sqrt()
    };

    let cross_product = |x: [T; 2], y: [T; 2]| -> T { 
        x[0] * y[1] - x[1] * y[0]
    };

    let n = points.len();
    let mut feret_diameter_maximum = T::zero();
    for i in 0..n {
        let p1 = points[i];
        let p2 = points[(i + 1) % n];
        let diff_a = [p2[0] - p1[0], p2[1] - p1[1]];

        for j in 0..n {
            let diff_b = [points[j][0] - p1[0], points[j][1] - p1[1]];
            let distance = (cross_product(
                diff_a,
                diff_b
            ) / norm(diff_a)).abs();

            if distance > feret_diameter_maximum {
                feret_diameter_maximum = distance;
            }
        }
    }

    feret_diameter_maximum
}

/// Compute the minimum Feret diameter of a polygon
///
/// # Arguments
///
/// * `points` - A vector of points defining the polygon
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::descriptors::form;
/// let points = vec![[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0], [0.0, 0.0]];
/// let feret_diameter_minimum = form::polygon_feret_diameter_minimum(&points);
/// ```
pub fn polygon_feret_diameter_minimum<T: Numeric>(points: &[[T; 2]]) -> T {
    let norm = |x: [T; 2]| -> T {
        (x[0] * x[0] + x[1] * x[1]).sqrt()
    };

    let cross_product = |x: [T; 2], y: [T; 2]| -> T { 
        x[0] * y[1] - x[1] * y[0]
    };

    let n = points.len();
    let mut feret_diameter_minimum = T::max_value();
    for i in 0..n {
        let p1 = points[i];
        let p2 = points[(i + 1) % n];
        let diff_a = [p2[0] - p1[0], p2[1] - p1[1]];

        let mut distance = T::zero();
        for j in 0..n {
            let diff_b = [points[j][0] - p1[0], points[j][1] - p1[1]];
            let d = (cross_product(
                diff_a,
                diff_b
            ) / norm(diff_a)).abs();

            if d > distance {
                distance = d;
            }
        }
        
        if distance < feret_diameter_minimum && distance > T::epsilon() {
            feret_diameter_minimum = distance;
        }
    }

    feret_diameter_minimum
}

/// Non-redundant computation of all polygon descriptors
///
/// # Arguments
///
/// * `points` - A vector of points defining the polygon
///
/// # Examples
///
/// ```no_run
/// use fqmv_core::descriptors::form;
/// let points = vec![[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0], [0.0, 0.0]];
/// let descriptors = form::polygon_descriptors(&points);
/// ```
pub fn polygon_descriptors<T: Numeric>(points: &[[T; 2]]) -> Vec<T> {
    let n_points = points.len();

    let mut area = T::zero();
    let mut perimeter = T::zero();
    let mut centroid_x = T::zero();
    let mut centroid_y = T::zero();

    let mut minimum_radius = T::max_value();
    let mut maximum_radius = T::zero();
    let mut mean_radius = T::zero();
    
    let (mut xmin, mut ymin) = (points[0][0], points[0][1]);
    let (mut xmax, mut ymax) = (points[0][0], points[0][1]);

    for i in 0..n_points {
        xmin = if points[i][0] < xmin {points[i][0]} else {xmin};
        ymin = if points[i][1] < ymin {points[i][1]} else {ymin};
        xmax = if points[i][0] > xmax {points[i][0]} else {xmax};
        ymax = if points[i][1] > ymax {points[i][1]} else {ymax};

        if i != n_points-1 {
            area += points[i][0] * points[i+1][1] - points[i+1][0] * points[i][1];

            perimeter += (
                (points[i][0] - points[i+1][0])
                * (points[i][0] - points[i+1][0])
                + (points[i][1] - points[i+1][1])
                * (points[i][1] - points[i+1][1])
            ).sqrt();

            centroid_x += points[i][0];
            centroid_y += points[i][1];
        }
    }

    if !is_shape_closed(points) {
        area += points[n_points-1][0] * points[0][1] - points[0][0] * points[n_points-1][1];

        perimeter += (
            (points[n_points-1][0] - points[0][0])
            * (points[n_points-1][0] - points[0][0])
            + (points[n_points-1][1] - points[0][1])
            * (points[n_points-1][1] - points[0][1])
        ).sqrt();

        centroid_x += points[n_points-1][0];
        centroid_y += points[n_points-1][1];
    }

    let include_last = if is_shape_closed(points) {1} else {0};

    let n = T::from_usize(n_points - include_last);
    centroid_x /= n;
    centroid_y /= n;

    for i in 0..n_points-include_last {
        let (x, y) = (points[i][0], points[i][1]);
        let distance = (centroid_x - x) * (centroid_x - x) + (centroid_y - y) * (centroid_y - y);
        if distance < minimum_radius {
            minimum_radius = distance;
        }
        if distance > maximum_radius {
            maximum_radius = distance;
        }
        mean_radius += distance.sqrt();
    }

    let closed_hull = hull::convex_hull_graham(points);
    let ellipse = fit_ellipse(points);

    let norm = |x: [T; 2]| -> T { (x[0] * x[0] + x[1] * x[1]).sqrt() };
    let cross_product = |x: [T; 2], y: [T; 2]| -> T { x[0] * y[1] - x[1] * y[0] };

    let n_hull = closed_hull.len();
    let mut area_convex = T::zero();
    let mut feret_diameter_maximum = T::zero();
    let mut feret_diameter_minimum = T::max_value();
    for i in 0..n_hull {
        let p1 = closed_hull[i];
        let p2 = closed_hull[(i + 1) % n_hull];
        let diff_a = [p2[0] - p1[0], p2[1] - p1[1]];

        if i == n_hull-1 {
            if closed_hull[i] == closed_hull[0] {
                break;
            } else {
                area_convex += closed_hull[i][0]
                    * closed_hull[0][1]
                    - closed_hull[0][0] 
                    * closed_hull[i][1];
            }
        } else {
            area_convex += closed_hull[i][0]
                * closed_hull[i+1][1]
                - closed_hull[i+1][0]
                * closed_hull[i][1];
        }

        let mut distance = T::zero();
        for j in 0..n_hull {
            let diff_b = [closed_hull[j][0] - p1[0], closed_hull[j][1] - p1[1]];
            let d = (cross_product(
                diff_a,
                diff_b
            ) / norm(diff_a)).abs();

            if d > distance {
                distance = d;
            }

            if distance > feret_diameter_maximum {
                feret_diameter_maximum = distance;
            }
        }
        
        if distance < feret_diameter_minimum && distance > T::epsilon() {
            feret_diameter_minimum = distance;
        }
    }

    let area = area.abs() / T::two();
    let area_bbox = (xmax - xmin) * (ymax - ymin);
    let area_convex = area_convex.abs() / T::two();

    let elongation = (xmax - xmin) / (ymax - ymin);
    let elongation = if elongation > T::one() {
        T::one() / elongation
    } else {
        elongation
    };

    let left = perimeter.powf(T::two());
    let right = T::from_f64(16.0) * area;
    let coefficient = if left <= right {
        T::zero()
    } else {
        (left - right).sqrt()
    };

    let thread_length = (perimeter + coefficient) / T::from_f64(4.0);
    let thread_width = area / thread_length;

    let solidity = area / area_convex;
    let extent = area / area_bbox;
    let form_factor = T::from_f64(4.0) * T::pi() * area / (perimeter * perimeter);

    let major_axis_length = ellipse[0];
    let minor_axis_length = ellipse[1];
    let eccentricity = ellipse[2];
    let curl_major = major_axis_length / thread_length;
    let curl_bbox = if (xmax - xmin) > (ymax - ymin) {
        (xmax - xmin) / thread_length
    } else {
        (ymax - ymin) / thread_length
    };

    let equivalent_diameter = (area / T::pi()).sqrt() * T::two();
    let minimum_radius = minimum_radius.sqrt();
    let maximum_radius = maximum_radius.sqrt();
    mean_radius /= n;

    vec![
        centroid_x,
        centroid_y,
        area,
        area_bbox,
        area_convex,
        elongation,
        perimeter,
        thread_length,
        thread_width,
        solidity,
        extent,
        form_factor,
        eccentricity,
        major_axis_length,
        minor_axis_length,
        curl_major,
        curl_bbox,
        equivalent_diameter,
        minimum_radius,
        maximum_radius,
        mean_radius,
        feret_diameter_maximum,
        feret_diameter_minimum,
    ]
}
