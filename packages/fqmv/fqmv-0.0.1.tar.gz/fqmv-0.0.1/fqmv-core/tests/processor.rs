use image::{Rgb, Luma, ImageBuffer};

use fqmv_core::data::Processor;
use fqmv_core::data::runners::process_image_mask_runner;

use fqmv_core::types::{Image, Mask};
use fqmv_core::process::lines::extract_contours;
use fqmv_core::io::{read_boxes, read_image, read_labels, read_polygons};

fn rgb_mask() -> (Image<Rgb<u8>>, Mask) {
    let mut rgb: Image<Rgb<u8>> = ImageBuffer::new(10, 10);
    let mut mask: Mask = ImageBuffer::new(10, 10);

    for i in 2..8 {
        for j in 2..8 {
            if i > 4 {
                if j > 4 {
                    rgb.get_pixel_mut(i, j).0 = [100, 100, 100];
                    mask.get_pixel_mut(i, j).0 = [1];
                } else {
                    rgb.get_pixel_mut(i, j).0 = [200, 200, 200];
                    mask.get_pixel_mut(i, j).0 = [8];
                }
            }
        }
    }

    (rgb, mask)
}

fn grayscale_mask() -> (Image<Luma<u8>>, Mask) {
    let mut gray: Image<Luma<u8>> = ImageBuffer::new(10, 10);
    let mut mask: Mask = ImageBuffer::new(10, 10);

    for i in 2..8 {
        for j in 2..8 {
            if i > 4 {
                if j > 4 {
                    gray.get_pixel_mut(i, j).0 = [100];
                    mask.get_pixel_mut(i, j).0 = [1];
                } else {
                    gray.get_pixel_mut(i, j).0 = [200];
                    mask.get_pixel_mut(i, j).0 = [8];
                }
            }
        }
    }

    (gray, mask)
}

#[test]
fn test_image_mask_rgb() {
    let (rgb, mask) = rgb_mask();

    let mut processor = Processor::new_from_mask(rgb, mask.clone());

    let processed_objects = processor.run(
        Some(0), 
        None, 
        None, 
        None,
        None,
        Some("ompbl".to_string()),
    );

    let objects = processed_objects.objects.clone().unwrap();
    let masked_objects = processed_objects.foreground_objects.clone().unwrap();
    let polygons = processed_objects.polygons.clone().unwrap();
    let bounding_boxes = processed_objects.bounding_boxes.clone().unwrap();
    let labels = processed_objects.labels.clone().unwrap();

    assert_eq!(labels, vec![1, 8]);

    polygons[0].iter().for_each(|i| {
        assert_eq!(mask.get_pixel(i[0] as u32, i[1] as u32).0[0], 1);
    });

    polygons[1].iter().for_each(|i| {
        assert_eq!(mask.get_pixel(i[0] as u32, i[1] as u32).0[0], 8);
    });

    assert_eq!(objects.len(), 2);
    assert_eq!(masked_objects.len(), 2);
    assert_eq!(polygons.len(), 2);
    assert_eq!(bounding_boxes.len(), 2);
    assert_eq!(labels.len(), 2);

    assert_eq!(bounding_boxes[0][0], 5.0);
    assert_eq!(bounding_boxes[0][1], 5.0);
    assert_eq!(bounding_boxes[0][2], 7.0);
    assert_eq!(bounding_boxes[0][3], 7.0);
    assert_eq!(bounding_boxes[1][0], 5.0);
    assert_eq!(bounding_boxes[1][1], 2.0);
    assert_eq!(bounding_boxes[1][2], 7.0);
    assert_eq!(bounding_boxes[1][3], 4.0);

    assert_eq!(objects[0].dimensions(), (3, 3));
    assert_eq!(objects[1].dimensions(), (3, 3));

    for i in 0..3 {
        for j in 0..3 {
            for k in 0..3 {
                assert_eq!(objects[0].get_pixel(i, j).0[k], 100);
            }
        }
    }

    for i in 0..3 {
        for j in 0..3 {
            for k in 0..3 {
                assert_eq!(objects[1].get_pixel(i, j).0[k], 200);
            }
        }
    }
}

#[test]
fn test_image_mask_grayscale() {
    let (gray, mask) = grayscale_mask();

    let mut processor = Processor::new_from_mask(gray, mask.clone());

    let processed_objects = processor.run(
        Some(0), 
        None, 
        None, 
        None,
        None,
        Some("ompbl".to_string()),
    );

    let objects = processed_objects.objects.clone().unwrap();
    let masked_objects = processed_objects.foreground_objects.clone().unwrap();
    let polygons = processed_objects.polygons.clone().unwrap();
    let bounding_boxes = processed_objects.bounding_boxes.clone().unwrap();
    let labels = processed_objects.labels.clone().unwrap();

    assert_eq!(labels, vec![1, 8]);

    polygons[0].iter().for_each(|i| {
        assert_eq!(mask.get_pixel(i[0] as u32, i[1] as u32).0[0], 1);
    });

    polygons[1].iter().for_each(|i| {
        assert_eq!(mask.get_pixel(i[0] as u32, i[1] as u32).0[0], 8);
    });

    assert_eq!(objects.len(), 2);
    assert_eq!(masked_objects.len(), 2);
    assert_eq!(polygons.len(), 2);
    assert_eq!(bounding_boxes.len(), 2);
    assert_eq!(labels.len(), 2);

    assert_eq!(bounding_boxes[0][0], 5.0);
    assert_eq!(bounding_boxes[0][1], 5.0);
    assert_eq!(bounding_boxes[0][2], 7.0);
    assert_eq!(bounding_boxes[0][3], 7.0);
    assert_eq!(bounding_boxes[1][0], 5.0);
    assert_eq!(bounding_boxes[1][1], 2.0);
    assert_eq!(bounding_boxes[1][2], 7.0);
    assert_eq!(bounding_boxes[1][3], 4.0);

    assert_eq!(objects[0].dimensions(), (3, 3));
    assert_eq!(objects[1].dimensions(), (3, 3));

    for i in 0..3 {
        for j in 0..3 {
            assert_eq!(objects[0].get_pixel(i, j).0[0], 100);
        }
    }

    for i in 0..3 {
        for j in 0..3 {
            assert_eq!(objects[1].get_pixel(i, j).0[0], 200);
        }
    }
}

#[test]
fn test_image_polygon_rgb() {
    let (rgb, mask) = rgb_mask();
    let polygons = extract_contours::<f64>(&mask, Some(&vec![1, 8]));

    let mut processor = Processor::new_from_polygons(rgb, polygons.clone());

    let processed_objects = processor.run(
        None, 
        None, 
        None, 
        None,
        None,
        Some("ompbl".to_string()),
    );

    let objects = processed_objects.objects.clone().unwrap();
    let masked_objects = processed_objects.foreground_objects.clone().unwrap();
    let polygons = processed_objects.polygons.clone().unwrap();
    let bounding_boxes = processed_objects.bounding_boxes.clone().unwrap();
    let labels = processed_objects.labels.clone().unwrap();

    assert_eq!(labels, vec![1, 2]);

    polygons[0].iter().for_each(|i| {
        assert_eq!(mask.get_pixel(i[0] as u32, i[1] as u32).0[0], 1);
    });

    polygons[1].iter().for_each(|i| {
        assert_eq!(mask.get_pixel(i[0] as u32, i[1] as u32).0[0], 8);
    });

    assert_eq!(objects.len(), 2);
    assert_eq!(masked_objects.len(), 2);
    assert_eq!(polygons.len(), 2);
    assert_eq!(bounding_boxes.len(), 2);
    assert_eq!(labels.len(), 2);

    assert_eq!(bounding_boxes[0][0], 5.0);
    assert_eq!(bounding_boxes[0][1], 5.0);
    assert_eq!(bounding_boxes[0][2], 7.0);
    assert_eq!(bounding_boxes[0][3], 7.0);
    assert_eq!(bounding_boxes[1][0], 5.0);
    assert_eq!(bounding_boxes[1][1], 2.0);
    assert_eq!(bounding_boxes[1][2], 7.0);
    assert_eq!(bounding_boxes[1][3], 4.0);

    assert_eq!(objects[0].dimensions(), (3, 3));
    assert_eq!(objects[1].dimensions(), (3, 3));

    for i in 0..3 {
        for j in 0..3 {
            for k in 0..3 {
                assert_eq!(objects[0].get_pixel(i, j).0[k], 100);
            }
        }
    }

    for i in 0..3 {
        for j in 0..3 {
            for k in 0..3 {
                assert_eq!(objects[1].get_pixel(i, j).0[k], 200);
            }
        }
    }
}

#[test]
fn test_image_polygon_grayscale() {
    let (gray, mask) = grayscale_mask();
    let polygons = extract_contours::<f64>(&mask, Some(&vec![1, 8]));

    let mut processor = Processor::new_from_polygons(gray, polygons.clone());

    let processed_objects = processor.run(
        None, 
        None, 
        None, 
        None,
        None,
        Some("ompbl".to_string()),
    );

    let objects = processed_objects.objects.clone().unwrap();
    let masked_objects = processed_objects.foreground_objects.clone().unwrap();
    let polygons = processed_objects.polygons.clone().unwrap();
    let bounding_boxes = processed_objects.bounding_boxes.clone().unwrap();
    let labels = processed_objects.labels.clone().unwrap();

    assert_eq!(labels, vec![1, 2]);

    polygons[0].iter().for_each(|i| {
        assert_eq!(mask.get_pixel(i[0] as u32, i[1] as u32).0[0], 1);
    });

    polygons[1].iter().for_each(|i| {
        assert_eq!(mask.get_pixel(i[0] as u32, i[1] as u32).0[0], 8);
    });

    assert_eq!(objects.len(), 2);
    assert_eq!(masked_objects.len(), 2);
    assert_eq!(polygons.len(), 2);
    assert_eq!(bounding_boxes.len(), 2);
    assert_eq!(labels.len(), 2);

    assert_eq!(bounding_boxes[0][0], 5.0);
    assert_eq!(bounding_boxes[0][1], 5.0);
    assert_eq!(bounding_boxes[0][2], 7.0);
    assert_eq!(bounding_boxes[0][3], 7.0);
    assert_eq!(bounding_boxes[1][0], 5.0);
    assert_eq!(bounding_boxes[1][1], 2.0);
    assert_eq!(bounding_boxes[1][2], 7.0);
    assert_eq!(bounding_boxes[1][3], 4.0);

    assert_eq!(objects[0].dimensions(), (3, 3));
    assert_eq!(objects[1].dimensions(), (3, 3));

    for i in 0..3 {
        for j in 0..3 {
            assert_eq!(objects[0].get_pixel(i, j).0[0], 100);
        }
    }

    for i in 0..3 {
        for j in 0..3 {
            assert_eq!(objects[1].get_pixel(i, j).0[0], 200);
        }
    }
}

#[test]
fn test_write_processor() {
    let (rgb, mask) = rgb_mask();
    
    let mut processor = Processor::new_from_mask(rgb, mask.clone());

    let processed_objects = processor.run(
        Some(0), 
        None, 
        None, 
        None,
        None,
        Some("ompbl".to_string()),
    );

    processed_objects.write(
        std::path::Path::new("../data/TEST_PROCESSOR_WRITE/"),
        "test_processed",
        None,
        None,
        None,
    );

    // read in and check the files
    let object_1 = read_image(
        "../data/TEST_PROCESSOR_WRITE/objects/test_processed_object_1.png"
    ).unwrap().to_rgb8();

    let object_2 = read_image(
        "../data/TEST_PROCESSOR_WRITE/objects/test_processed_object_8.png"
    ).unwrap().to_rgb8();

    let masked_object_1 = read_image(
        "../data/TEST_PROCESSOR_WRITE/objects_foreground/test_processed_foreground_1.png"
    ).unwrap().to_rgb8();

    let masked_object_2 = read_image(
        "../data/TEST_PROCESSOR_WRITE/objects_foreground/test_processed_foreground_8.png"
    ).unwrap().to_rgb8();

    let polygons = read_polygons(
        "../data/TEST_PROCESSOR_WRITE/test_processed_polygons.json"
    ).unwrap();

    let bounding_boxes = read_boxes(
        "../data/TEST_PROCESSOR_WRITE/test_processed_bounding_boxes.json"
    ).unwrap();

    assert_eq!(object_1.dimensions(), (3, 3));
    assert_eq!(object_2.dimensions(), (3, 3));
    assert_eq!(masked_object_1.dimensions(), (3, 3));
    assert_eq!(masked_object_2.dimensions(), (3, 3));

    for i in 0..3 {
        for j in 0..3 {
            for k in 0..3 {
                assert_eq!(object_1.get_pixel(i, j).0[k], 100);
            }
        }
    }

    for i in 0..3 {
        for j in 0..3 {
            for k in 0..3 {
                assert_eq!(object_2.get_pixel(i, j).0[k], 200);
            }
        }
    }

    for i in 0..3 {
        for j in 0..3 {
            for k in 0..3 {
                assert_eq!(masked_object_1.get_pixel(i, j).0[k], 100);
            }
        }
    }

    for i in 0..3 {
        for j in 0..3 {
            for k in 0..3 {
                assert_eq!(masked_object_2.get_pixel(i, j).0[k], 200);
            }
        }
    }

    for (c, c_) in polygons.iter()
        .zip(processed_objects.polygons.clone().unwrap().iter()) 
    {
        assert_eq!(c, c_);
    }

    for (b, b_) in bounding_boxes.iter()
        .zip(processed_objects.bounding_boxes.clone().unwrap().iter()) 
    {
        assert_eq!(b, b_);
    }

    std::fs::remove_dir_all("../data/TEST_PROCESSOR_WRITE/").unwrap();
}

#[test]
fn test_image_mask_runner() {
    let (rgb, mask) = rgb_mask();
    
    // save the rgb and mask to same folder
    std::fs::create_dir_all("../data/TEST_PROCESSOR_WRITE_RUNNER/").unwrap();
    rgb.save("../data/TEST_PROCESSOR_WRITE_RUNNER/test_image_mask_runner_rgb.png").unwrap();
    mask.save("../data/TEST_PROCESSOR_WRITE_RUNNER/test_image_mask_runner_mask.png").unwrap();

    let mut processor = Processor::new_from_mask(rgb, mask.clone());

    let processed_objects = processor.run(
        Some(0), 
        None, 
        None, 
        None,
        None,
        Some("ompbl".to_string()),
    );

    processed_objects.write(
        std::path::Path::new("../data/TEST_PROCESSOR_WRITE_B/"),
        "test_processed",
        None,
        None,
        None,
    );

    process_image_mask_runner(
        Some("../data/TEST_PROCESSOR_WRITE_RUNNER/".to_string()),
        None,
        Some("_rgb".to_string()),
        Some("_mask".to_string()),
        None,
        None,
        None,
        Some(0),
        None,
        None,
        Some("ompbl".to_string()),
        None,
        Some("../data/TEST_PROCESSOR_WRITE_RUNNER_OUTPUT/".to_string()),
        None,
        None,
        None,
    );

    let polygons = processed_objects.polygons.clone().unwrap();
    let bounding_boxes = processed_objects.bounding_boxes.clone().unwrap();

    // read in objects from runner output path
    let output_folder = "../data/TEST_PROCESSOR_WRITE_RUNNER_OUTPUT/data/test_image_mask_runner";
    let object_1 = read_image(
        &format!("{}/objects/test_image_mask_runner_object_1.png", output_folder)
    ).unwrap().to_rgb8();

    let object_2 = read_image(
        &format!("{}/objects/test_image_mask_runner_object_8.png", output_folder)
    ).unwrap().to_rgb8();

    let masked_object_1 = read_image(
        &format!("{}/objects_foreground/test_image_mask_runner_foreground_1.png", output_folder)
    ).unwrap().to_rgb8();

    let masked_object_2 = read_image(
        &format!("{}/objects_foreground/test_image_mask_runner_foreground_8.png", output_folder)
    ).unwrap().to_rgb8();

    let polygons_runner = read_polygons(
        &format!("{}/test_image_mask_runner_polygons.json", output_folder)
    ).unwrap();

    let bounding_boxes_runner = read_boxes(
        &format!("{}/test_image_mask_runner_bounding_boxes.json", output_folder)
    ).unwrap();

    let labels_runner = read_labels(
        &format!("{}/test_image_mask_runner_labels.json", output_folder)
    ).unwrap();

    assert_eq!(labels_runner, vec![1, 8]);

    assert_eq!(object_1.dimensions(), (3, 3));
    assert_eq!(object_2.dimensions(), (3, 3));
    assert_eq!(masked_object_1.dimensions(), (3, 3));
    assert_eq!(masked_object_2.dimensions(), (3, 3));

    for i in 0..3 {
        for j in 0..3 {
            for k in 0..3 {
                assert_eq!(object_1.get_pixel(i, j).0[k], 100);
            }
        }
    }

    for i in 0..3 {
        for j in 0..3 {
            for k in 0..3 {
                assert_eq!(object_2.get_pixel(i, j).0[k], 200);
            }
        }
    }

    for i in 0..3 {
        for j in 0..3 {
            for k in 0..3 {
                assert_eq!(masked_object_1.get_pixel(i, j).0[k], 100);
            }
        }
    }

    for i in 0..3 {
        for j in 0..3 {
            for k in 0..3 {
                assert_eq!(masked_object_2.get_pixel(i, j).0[k], 200);
            }
        }
    }

    // ensure runner output is the same as processor output
    for (c, c_) in polygons.iter()
        .zip(polygons_runner.iter()) 
    {
        assert_eq!(c, c_);
    }

    for (b, b_) in bounding_boxes.iter()
        .zip(bounding_boxes_runner.iter()) 
    {
        assert_eq!(b, b_);
    }

    if std::path::Path::new("../data/TEST_PROCESSOR_WRITE_B/").exists() {
        std::fs::remove_dir_all("../data/TEST_PROCESSOR_WRITE_B/").unwrap();
    }

    std::fs::remove_dir_all("../data/TEST_PROCESSOR_WRITE_RUNNER/").unwrap();
    std::fs::remove_dir_all("../data/TEST_PROCESSOR_WRITE_RUNNER_OUTPUT/").unwrap();
}
