use fqmv_core::io::read_image;
use fqmv_core::io::write_image;
use fqmv_core::io::read_polygons;
use fqmv_core::io::write_polygons;
use image::DynamicImage;

fn data_gray() -> Vec<String> {
    vec![
        "test_grayscale.bmp".to_string(),
        "test_grayscale.jpeg".to_string(),
        "test_grayscale.png".to_string(),
        "test_grayscale.pbm".to_string(),
        "test_grayscale.tga".to_string(),
        "test_grayscale.tif".to_string(),
        "test_grayscale.webp".to_string(),
    ]
}

fn data_rgb() -> Vec<String> {
    vec![
        "test_rgb.bmp".to_string(),
        "test_rgb.jpeg".to_string(),
        "test_rgb.png".to_string(),
        "test_rgb.pbm".to_string(),
        "test_rgb.tga".to_string(),
        "test_rgb.tif".to_string(),
        "test_rgb.webp".to_string(),
    ]
}

fn data_mask() -> Vec<String> {
    vec![
        "test_mask_binary.png".to_string(),
        "test_mask_integer.png".to_string(),
    ]
}

fn data_npy_gray() -> Vec<String> {
    vec![
        "test_grayscale.npy".to_string(),
        "test_grayscale_f32.npy".to_string(),
        "test_grayscale_f64.npy".to_string(),
        "test_grayscale_i32.npy".to_string(),
        "test_grayscale_i64.npy".to_string(),
        "test_grayscale_u16.npy".to_string(),
    ]
}

fn data_npy_rgb() -> Vec<String> {
    vec![
        "test_rgb.npy".to_string(),
        "test_rgb_f32.npy".to_string(),
        "test_rgb_f64.npy".to_string(),
        "test_rgb_i32.npy".to_string(),
        "test_rgb_i64.npy".to_string(),
        "test_rgb_u16.npy".to_string(),
    ]
}

fn data_npy_mask() -> Vec<String> {
    vec![
        "test_mask_binary_1.npy".to_string(),
        "test_mask_binary_1_u16.npy".to_string(),
        "test_mask_binary_255.npy".to_string(),
        "test_mask_binary_255_u16.npy".to_string(),
        "test_mask_integer.npy".to_string(),
        "test_mask_integer_u16.npy".to_string(),
    ]
}

fn data_polygons() -> Vec<String> {
    vec![
        "test_polygons.json".to_string(),
        "test_polygons.npy".to_string(),
    ]
}

#[test]
fn test_read_gray() {
    let base = image::open("../data/test_grayscale.png").unwrap().to_luma8();
    let (base_w, base_h) = base.dimensions();
    for data in data_gray().iter() {
        let path = format!("../data/{}", data.as_str());
        let img = read_image(&path).unwrap().into_luma8();

        assert_eq!(img.dimensions(), (base_w, base_h));

        if data.contains("jpeg") || data.contains("webp") {
            let mut diffs = Vec::new();
            for (p1, p2) in img.pixels().zip(base.pixels()) {
                let diff = p1[0] as i32 - p2[0] as i32;
                diffs.push(diff);
            }
            let mean_diff = diffs.iter().sum::<i32>() / diffs.len() as i32;
            
            // Expectation over all compressed pixels should be close to zero
            assert!(mean_diff.abs() < 1);
        } else {
            for (p1, p2) in img.pixels().zip(base.pixels()) {
                assert_eq!(p1[0], p2[0]);
            }
        }
    }
}

#[test]
fn test_read_rgb() {
    let base = image::open("../data/test_rgb.png").unwrap().to_rgb8();
    let (base_w, base_h) = base.dimensions();
    for data in data_rgb().iter() {
        let path = format!("../data/{}", data.as_str());
        let img = read_image(&path).unwrap().into_rgb8();

        assert_eq!(img.dimensions(), (base_w, base_h));

        if data.contains("jpeg") || data.contains("webp") {
            let mut diffs = Vec::new();
            for (p1, p2) in img.pixels().zip(base.pixels()) {
                let diff = p1[0] as i32 - p2[0] as i32;
                diffs.push(diff);
            }
            let mean_diff = diffs.iter().sum::<i32>() / diffs.len() as i32;
            
            // Expectation over all compressed pixels should be close to zero
            assert!(mean_diff.abs() < 1);
        } else {
            for (p1, p2) in img.pixels().zip(base.pixels()) {
                assert_eq!(p1[0], p2[0]);
                assert_eq!(p1[1], p2[1]);
                assert_eq!(p1[2], p2[2]);
            }
        }
    }
}

#[test]
fn test_read_mask() {
    let data = data_mask();
    let binary = data.iter().filter(|x| x.contains("binary")).collect::<Vec<_>>();
    let integer = data.iter().filter(|x| x.contains("integer")).collect::<Vec<_>>();

    let binary = image::open(format!("../data/{}", binary[0])).unwrap().to_luma8();
    let binary_sum = binary.pixels().map(|x| x[0] as u32).sum::<u32>();
    assert_eq!(binary_sum, 120970);

    let integer = image::open(format!("../data/{}", integer[0])).unwrap().to_luma8();
    let integer_sum_1 = integer.pixels().map(|x| x[0].eq(&1) as u32).sum::<u32>();
    let integer_sum_2 = integer.pixels().map(|x| x[0].eq(&2) as u32).sum::<u32>();
    assert_eq!(integer_sum_1, 30700);
    assert_eq!(integer_sum_2, 90275);
}

#[test]
fn test_read_npy_gray() {
    let base = image::open("../data/test_grayscale.png").unwrap().to_luma8();
    let (base_w, base_h) = base.dimensions();
    for data in data_npy_gray().iter() {
        let path = format!("../data/{}", data.as_str());
        let img = read_image(&path).unwrap().into_luma8();
        assert_eq!(img.dimensions(), (base_w, base_h));

        if data == "test_grayscale.npy" {
            let img = read_image(&path).unwrap().into_luma8();
            for (p1, p2) in img.pixels().zip(base.pixels()) {
                assert_eq!(p1[0], p2[0]);
            }
        } else {
            let img = read_image(&path).unwrap().into_luma16();
            for (p1, p2) in img.pixels().zip(base.pixels()) {
                assert_eq!(p1[0], p2[0] as u16);
            }
        }
    }
}

#[test]
fn test_read_npy_rgb() {
    let base = image::open("../data/test_rgb.png").unwrap().to_rgb8();
    let (base_w, base_h) = base.dimensions();
    for data in data_npy_rgb().iter() {
        let path = format!("../data/{}", data.as_str());
        let img = read_image(&path).unwrap().into_rgb8();
        assert_eq!(img.dimensions(), (base_w, base_h));

        if data == "test_rgb.npy" {
            let img = read_image(&path).unwrap().into_rgb8();
            for (p1, p2) in img.pixels().zip(base.pixels()) {
                assert_eq!(p1[0], p2[0]);
                assert_eq!(p1[1], p2[1]);
                assert_eq!(p1[2], p2[2]);
            }
        } else {
            let img = read_image(&path).unwrap().into_rgb16();
            for (p1, p2) in img.pixels().zip(base.pixels()) {
                assert_eq!(p1[0], p2[0] as u16);
                assert_eq!(p1[1], p2[1] as u16);
                assert_eq!(p1[2], p2[2] as u16);
            }
        }
    }
}

#[test]
fn test_read_npy_mask() {
    let data = data_npy_mask();
    let binary_1 = data.iter().filter(|x| x.contains("binary_1")).collect::<Vec<_>>();
    let binary_255 = data.iter().filter(|x| x.contains("binary_255")).collect::<Vec<_>>();
    let integer = data.iter().filter(|x| x.contains("integer")).collect::<Vec<_>>();

    for binary in binary_1.iter() {
        if binary.contains("u16") {
            let binary = read_image(&format!("../data/{}", binary)).unwrap().into_luma16();
            let binary_sum = binary.pixels().map(|x| x[0] as u32).sum::<u32>();
            assert_eq!(binary_sum, 120970);
        } else {
            let binary = read_image(&format!("../data/{}", binary)).unwrap().into_luma8();
            let binary_sum = binary.pixels().map(|x| x[0] as u32).sum::<u32>();
            assert_eq!(binary_sum, 120970);
        }
    }

    for binary in binary_255.iter() {
        if binary.contains("u16") {
            let binary = read_image(&format!("../data/{}", binary)).unwrap().into_luma16();
            let binary_sum = binary.pixels().map(|x| x[0] as u32).sum::<u32>();
            assert_eq!(binary_sum, 120970 * 255);
        } else {
            let binary = read_image(&format!("../data/{}", binary)).unwrap().into_luma8();
            let binary_sum = binary.pixels().map(|x| x[0] as u32).sum::<u32>();
            assert_eq!(binary_sum, 120970 * 255);
        }
    }

    for integer_ in integer.iter() {
        if integer_.contains("u16") {
            let integer = read_image(&format!("../data/{}", integer_)).unwrap().into_luma16();
            let integer_sum_1 = integer.pixels().map(|x| x[0].eq(&1) as u32).sum::<u32>();
            let integer_sum_2 = integer.pixels().map(|x| x[0].eq(&2) as u32).sum::<u32>();
            assert_eq!(integer_sum_1, 30700);
            assert_eq!(integer_sum_2, 90275);
        } else {
            let integer = read_image(&format!("../data/{}", integer_)).unwrap().into_luma8();
            let integer_sum_1 = integer.pixels().map(|x| x[0].eq(&1) as u32).sum::<u32>();
            let integer_sum_2 = integer.pixels().map(|x| x[0].eq(&2) as u32).sum::<u32>();
            assert_eq!(integer_sum_1, 30700);
            assert_eq!(integer_sum_2, 90275);
        }
    }
}

#[test]
fn test_write_gray() {
    for data in data_gray().iter() {
        let path = format!("../data/{}", data.as_str());
        let ext = path.split('.').last().unwrap();
        let img = read_image(&path).unwrap().into_luma8();

        let out_path = format!("../data/TEST_WRITE_GRAYSCALE.{}", ext); 
        let _ = write_image(&out_path, DynamicImage::ImageLuma8(img.clone()));
        let img_out = read_image(&out_path).unwrap().into_luma8();

        if !data.contains("jpeg") {
            for (p1, p2) in img.pixels().zip(img_out.pixels()) {
                assert_eq!(p1[0], p2[0]);
            }
        }

        std::fs::remove_file(out_path).unwrap();
    }
}

#[test]
fn test_write_rgb() {
    for data in data_rgb().iter() {
        let path = format!("../data/{}", data.as_str());
        let ext = path.split('.').last().unwrap();
        let img = read_image(&path).unwrap().into_rgb8();

        let out_path = format!("../data/TEST_WRITE_RGB.{}", ext); 
        let _ = write_image(&out_path, DynamicImage::ImageRgb8(img.clone()));
        let img_out = read_image(&out_path).unwrap().into_rgb8();

        if !data.contains("jpeg") {
            for (p1, p2) in img.pixels().zip(img_out.pixels()) {
                assert_eq!(p1[0], p2[0]);
                assert_eq!(p1[1], p2[1]);
                assert_eq!(p1[2], p2[2]);
            }
        }

        std::fs::remove_file(out_path).unwrap();
    }
}

#[test]
fn test_write_npy_gray() {
    for data in data_npy_gray().iter() {
        let path = format!("../data/{}", data.as_str());
        let ext = path.split('.').last().unwrap();
        let img = read_image(&path).unwrap().into_luma8();

        let out_path = format!("../data/TEST_WRITE_GRAYSCALE.{}", ext); 
        let _ = write_image(&out_path, DynamicImage::ImageLuma8(img.clone()));
        let img_out = read_image(&out_path).unwrap().into_luma8();

        if data == "test_grayscale.npy" {
            for (p1, p2) in img.pixels().zip(img_out.pixels()) {
                assert_eq!(p1[0], p2[0]);
            }
        } else {
            for (p1, p2) in img.pixels().zip(img_out.pixels()) {
                assert_eq!(p1[0], p2[0] as u8);
            }
        }

        std::fs::remove_file(out_path).unwrap();
    }
}

#[test]
fn test_write_npy_rgb() {
    for data in data_npy_rgb().iter() {
        let path = format!("../data/{}", data.as_str());
        let ext = path.split('.').last().unwrap();
        println!("{}", path);
        let img = read_image(&path).unwrap().into_rgb8();

        let out_path = format!("../data/TEST_WRITE_RGB.{}", ext); 
        write_image(&out_path, DynamicImage::ImageRgb8(img.clone())).unwrap();
        let img_out = read_image(&out_path).unwrap().into_rgb8();

        if data == "test_rgb.npy" {
            for (p1, p2) in img.pixels().zip(img_out.pixels()) {
                assert_eq!(p1[0], p2[0]);
                assert_eq!(p1[1], p2[1]);
                assert_eq!(p1[2], p2[2]);
            }
        } else {
            for (p1, p2) in img.pixels().zip(img_out.pixels()) {
                assert_eq!(p1[0], p2[0] as u8);
                assert_eq!(p1[1], p2[1] as u8);
                assert_eq!(p1[2], p2[2] as u8);
            }
        }

        std::fs::remove_file(out_path).unwrap();
    }
}

#[test]
fn test_polygons() {
    let data = data_polygons();
    let json = data.iter().filter(|x| x.contains("json")).collect::<Vec<_>>();
    let npy = data.iter().filter(|x| x.contains("npy")).collect::<Vec<_>>();

    let json = read_polygons(&format!("../data/{}", json[0])).unwrap();
    let npy = read_polygons(&format!("../data/{}", npy[0])).unwrap();

    for polygon in json.iter() {
        for point in polygon.iter() {
            assert_eq!(point.len(), 2);
        }
    }

    for polygon in npy.iter() {
        for point in polygon.iter() {
            assert_eq!(point.len(), 2);
        }
    }

    let out_path = "../data/TEST_WRITE_POLYGONS.json";
    let _ = write_polygons(&out_path, &json);
    let json_out = read_polygons(&out_path).unwrap();
    for (polygon, polygon_out) in json.iter().zip(json_out.iter()) {
        for (point, point_out) in polygon.iter().zip(polygon_out.iter()) {
            assert_eq!(point[0], point_out[0]);
            assert_eq!(point[1], point_out[1]);
        }
    }
    std::fs::remove_file(out_path).unwrap();

    let out_path = "../data/TEST_WRITE_POLYGONS.npy";
    let _ = write_polygons(&out_path, &npy);
    let npy_out = read_polygons(&out_path).unwrap();
    for (polygon, polygon_out) in npy.iter().zip(npy_out.iter()) {
        for (point, point_out) in polygon.iter().zip(polygon_out.iter()) {
            assert_eq!(point[0], point_out[0]);
            assert_eq!(point[1], point_out[1]);
        }
    }
    std::fs::remove_file(out_path).unwrap();
}
