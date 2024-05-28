# fqmv-pyo3

The `fqmv-pyo3` crate exposes a subset of `fqmv-core` functions to python using [pyo3](https://github.com/PyO3).

## Install

The `fqmv` python package can be installed via pip:

```bash
pip install fqmv
```

Or, alternatively, from source using the [maturin](https://github.com/PyO3/maturin) package. This assumes you have Rust and cargo installed on your machine.

```
git clone https://github.com/tomouellette/fqmv
cd fqmv/fqmv-pyo3/
maturn build --release
pip install ../target/wheels/*.whl
```

## Functions

### Measure

#### Form

```python3
import fqmv
import numpy as np

polygon = np.random.rand(100, 2)

# Compute all morphometric descriptors
descriptors = fqmv.measure.polygon_descriptors(polygon)

# Compute individual morphometric descriptors
area = fqmv.measure.polygon_area(polygon)
area_bbox = fqmv.measure.polygon_area_bbox(polygon)
area_convex = fqmv.measure.polygon_area_convex(polygon)
elongation = fqmv.measure.polygon_elongation(polygon)
perimeter = fqmv.measure.polygon_perimeter(polygon)
thread_length = fqmv.measure.polygon_thread_length(polygon)
thread_width = fqmv.measure.polygon_thread_width(polygon)
solidity = fqmv.measure.polygon_solidity(polygon)
extent = fqmv.measure.polygon_extent(polygon)
form_factor = fqmv.measure.polygon_form_factor(polygon)
eccentricity = fqmv.measure.polygon_eccentricity(polygon)
major_axis_length = fqmv.measure.polygon_major_axis_length(polygon)
minor_axis_length = fqmv.measure.polygon_minor_axis_length(polygon)
curl_major = fqmv.measure.polygon_curl_major(polygon)
curl_bbox = fqmv.measure.polygon_curl_bbox(polygon)
equivalent_diameter = fqmv.measure.polygon_equivalent_diameter(polygon)
minimum_radius = fqmv.measure.polygon_minimum_radius(polygon)
maximum_radius = fqmv.measure.polygon_maximum_radius(polygon)
mean_radius = fqmv.measure.polygon_mean_radius(polygon)
feret_diameter_maximum = fqmv.measure.polygon_feret_diameter_maximum(polygon)
feret_diameter_minimum = fqmv.measure.polygon_feret_diameter_minimum(polygon)
```

#### Intensity

```python3
import fqmv
import numpy as np

image = np.random.randint(0, 256, (224, 224), dtype=np.uint8)

# Compute all intensity descriptors
descriptors = fqmv.measure.intensity_descriptors(image)

# Compute individual intensity descriptors
maximum = fqmv.measure.intensity_maximum(image)
minimum = fqmv.measure.intensity_minimum(image)
mean = fqmv.measure.intensity_mean(image)
integrated = fqmv.measure.intensity_integrated(image)
standard_deviation = fqmv.measure.intensity_standard_deviation(image)
median = fqmv.measure.intensity_median(image)
median_absolute_deviation = fqmv.measure.intensity_median_absolute_deviation(image)
skewness = fqmv.measure.intensity_histogram_skewness(image)
kurtosis = fqmv.measure.intensity_histogram_kurtosis(image)
```

#### Moments

```python3
import fqmv
import numpy as np

binary = np.zeros((224, 224), dtype=np.uint8)
binary[50:150,50:150] = 1

# Compute all moments descriptors
descriptors = fqmv.measure.moments_descriptors(binary)

# Compute individual moments descriptors
moments_raw = fqmv.measure.moments_raw(binary)
moments_central = fqmv.measure.moments_central(binary)
moments_hu = fqmv.measure.moments_hu(binary)
```

#### Texture

```python3
import fqmv
import numpy as np

image = np.random.randint(0, 256, (224, 224), dtype=np.uint8)

# Compute all texture descriptors
descriptors = fqmv.measure.texture_descriptors(image)

# Compute individual texture descriptors
energy = fqmv.measure.texture_energy(polygon)
contrast = fqmv.measure.texture_contrast(polygon)
correlation = fqmv.measure.texture_correlation(polygon)
sum_of_squares = fqmv.measure.texture_sum_of_squares(polygon)
inverse_difference = fqmv.measure.texture_inverse_difference(polygon)
sum_average = fqmv.measure.texture_sum_average(polygon)
sum_variance = fqmv.measure.texture_sum_variance(polygon)
sum_entropy = fqmv.measure.texture_sum_entropy(polygon)
entropy = fqmv.measure.texture_entropy(polygon)
difference_variance = fqmv.measure.texture_difference_variance(polygon)
difference_entropy = fqmv.measure.texture_difference_entropy(polygon)
infocorr_1 = fqmv.measure.texture_infocorr_1(polygon)
infocorr_2 = fqmv.measure.texture_infocorr_2(polygon)
haralick_features = fqmv.measure.haralick_features(polygon)
```

#### Zernike

```python3
import fqmv
import numpy as np

image = np.random.randint(0, 256, (224, 224), dtype=np.uint8)

# Compute all Zernike descriptors
descriptors = fqmv.measure.zernike_descriptors(image) 
```

### Geometry

```python3
import fqmv
import numpy as np

# Order points for an array or list of specified data type
polygon = fqmv.geometry.order_points_u8(polygon)
polygon = fqmv.geometry.order_points_i32(polygon)
polygon = fqmv.geometry.order_points_i64(polygon)
polygon = fqmv.geometry.order_points_f32(polygon)
polygon = fqmv.geometry.order_points_f64(polygon)

# Resample points for an array or list of specified data type
polygon = fqmv.geometry.resample_points_u8(polygon, n=64)
polygon = fqmv.geometry.resample_points_i32(polygon, n=64)
polygon = fqmv.geometry.resample_points_i64(polygon, n=64)
polygon = fqmv.geometry.resample_points_f32(polygon, n=64)
polygon = fqmv.geometry.resample_points_f64(polygon, n=64)

# Check if an [x,y] point is inside a polygon for a specified data type
is_inside = fqmv.geometry.point_in_polygon_u8(point, polygon)
is_inside = fqmv.geometry.point_in_polygon_i32(point, polygon)
is_inside = fqmv.geometry.point_in_polygon_i64(point, polygon)
is_inside = fqmv.geometry.point_in_polygon_f32(point, polygon)
is_inside = fqmv.geometry.point_in_polygon_f64(point, polygon)

# Align an f64 polygon to f64 reference polygon
aligned_polygon = fqmv.geometry.align_points_orthogonal(polygon, reference, scale=False)
```
