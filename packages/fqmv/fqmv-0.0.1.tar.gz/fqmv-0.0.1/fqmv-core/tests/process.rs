use image::{DynamicImage, Rgb, Luma};

use fqmv_core::types::{Image, Mask};
use fqmv_core::process::lines;
use fqmv_core::process::mask;
use fqmv_core::process::objects;
use fqmv_core::process::transform;

fn gray_mask() -> (Image<Luma<u8>>, Mask) {
    let mut gray = DynamicImage::new_luma8(10, 10).to_luma8();
    let mut mask = DynamicImage::new_luma16(10, 10).to_luma16();

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

fn gray_mask_nonsquare() -> (Image<Luma<u8>>, Mask) {
    let mut gray = DynamicImage::new_luma8(10, 10).to_luma8();
    let mut mask = DynamicImage::new_luma16(10, 10).to_luma16();

    for i in 2..8 {
        for j in 2..8 {
            if i > 4 {
                if j > 4 {
                    if i != 5 || j != 5 {
                        gray.get_pixel_mut(i, j).0 = [100];
                        mask.get_pixel_mut(i, j).0 = [1];
                    }
                } else {
                    if i != 5 || j != 2 {
                        gray.get_pixel_mut(i, j).0 = [200];
                        mask.get_pixel_mut(i, j).0 = [8];
                    } 
                }
            }
        }
    }

    (gray, mask)
}

fn rgb_mask() -> (Image<Rgb<u8>>, Mask) {
    let mut rgb = DynamicImage::new_rgb8(10, 10).to_rgb8();
    let mut mask = DynamicImage::new_luma16(10, 10).to_luma16();

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

fn rgb_mask_nonsquare() -> (Image<Rgb<u8>>, Mask) {
    let mut rgb = DynamicImage::new_rgb8(10, 10).to_rgb8();
    let mut mask = DynamicImage::new_luma16(10, 10).to_luma16();

    for i in 2..8 {
        for j in 2..8 {
            if i > 4 {
                if j > 4 {
                    if i != 5 || j != 5 {
                        rgb.get_pixel_mut(i, j).0 = [100, 100, 100];
                        mask.get_pixel_mut(i, j).0 = [1];
                    }
                } else {
                    if i != 5 || j != 2 {
                        rgb.get_pixel_mut(i, j).0 = [200, 200, 200];
                        mask.get_pixel_mut(i, j).0 = [8];
                    } 
                }
            }
        }
    }

    (rgb, mask)
}

#[test]
fn test_extract_objects_gray() {
    let (mut gray, mask) = gray_mask();
    let (labels, _, _) = mask::count_labels(&mask);
    let contours = lines::extract_contours(&mask, Some(&labels));
    let bounding_boxes = lines::extract_bounding_boxes(&contours, None);

    let objects = objects::extract_objects(
        &mut gray,
        &bounding_boxes,
        None,
        None,
    );

    let objects = objects.iter().map(|x| x).collect::<Vec<_>>();

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

    let resized_objects = objects::extract_objects(
        &mut gray,
        &bounding_boxes,
        Some((5, 5)),
        Some("linear"),
    );

    let resized_objects = resized_objects.iter().map(|x| x).collect::<Vec<_>>();

    assert_eq!(resized_objects[0].dimensions(), (5, 5));
    assert_eq!(resized_objects[1].dimensions(), (5, 5));

    for i in 0..5 {
        for j in 0..5 {
            assert_eq!(resized_objects[0].get_pixel(i, j).0[0], 100);
        }
    }

    for i in 0..5 {
        for j in 0..5 {
            assert_eq!(resized_objects[1].get_pixel(i, j).0[0], 200);
        }
    }
}

#[test]
fn test_extract_foreground_objects_gray() {
    let (mut gray, mut mask) = gray_mask_nonsquare();
    let (labels, _, _) = mask::count_labels(&mask);
    let contours = lines::extract_contours(&mask, Some(&labels.clone()));
    let bounding_boxes = lines::extract_bounding_boxes(&contours, None);

    let objects = objects::extract_foreground_objects(
        &mut gray,
        &mut mask,
        &bounding_boxes,
        &labels,
        None,
        None,
    );

    let objects = objects.iter().map(|x| x).collect::<Vec<_>>();

    assert_eq!(objects[0].dimensions(), (3, 3));
    assert_eq!(objects[1].dimensions(), (3, 3));

    for i in 0..3 {
        for j in 0..3 {
            if i == 0 && j == 0 {
                assert_eq!(objects[0].get_pixel(i, j).0[0], 0);
            } else {
                assert_eq!(objects[0].get_pixel(i, j).0[0], 100);
            }
        }
    }

    for i in 0..3 {
        for j in 0..3 {
            if i == 0 && j == 0 {
                assert_eq!(objects[1].get_pixel(i, j).0[0], 0);
            } else {
                assert_eq!(objects[1].get_pixel(i, j).0[0], 200);
            }
        }
    }

    let resized_objects = objects::extract_foreground_objects(
        &mut gray,
        &mut mask,
        &bounding_boxes,
        &labels,
        Some((6, 6)),
        Some("linear"),
    );

    let resized_objects = resized_objects.iter().map(|x| x).collect::<Vec<_>>();

    assert_eq!(resized_objects[0].dimensions(), (6, 6));
    assert_eq!(resized_objects[1].dimensions(), (6, 6));

    for i in 0..5 {
        for j in 0..5 {
            if i < 3 && j < 3 {
                assert!(resized_objects[0].get_pixel(i, j).0[0] < 100);
            } else {
                assert_eq!(resized_objects[0].get_pixel(i, j).0[0], 100);
            }
        }
    }
}

#[test]
fn test_extract_objects_rgb() {
    let (mut rgb, mask) = rgb_mask();
    let (labels, _, _) = mask::count_labels(&mask);
    let contours = lines::extract_contours(&mask, Some(&labels));
    let bounding_boxes = lines::extract_bounding_boxes(&contours, None);

    println!("{:?}", bounding_boxes);
    let objects = objects::extract_objects(
        &mut rgb,
        &bounding_boxes,
        None,
        None,
    );

    let objects = objects.iter().map(|x| x).collect::<Vec<_>>();

    assert_eq!(objects[0].dimensions(), (3, 3));
    assert_eq!(objects[1].dimensions(), (3, 3));

    for i in 0..3 {
        for j in 0..3 {
            assert_eq!(objects[0].get_pixel(i, j).0, [100, 100, 100]);
        }
    }

    for i in 0..3 {
        for j in 0..3 {
            assert_eq!(objects[1].get_pixel(i, j).0, [200, 200, 200]);
        }
    }

    let resized_objects = objects::extract_objects(
        &mut rgb,
        &bounding_boxes,
        Some((5, 5)),
        Some("linear"),
    );

    let resized_objects = resized_objects.iter().map(|x| x).collect::<Vec<_>>();

    assert_eq!(resized_objects[0].dimensions(), (5, 5));
    assert_eq!(resized_objects[1].dimensions(), (5, 5));

    for i in 0..5 {
        for j in 0..5 {
            assert_eq!(resized_objects[0].get_pixel(i, j).0, [100, 100, 100]);
        }
    }

    for i in 0..5 {
        for j in 0..5 {
            assert_eq!(resized_objects[1].get_pixel(i, j).0, [200, 200, 200]);
        }
    }
}

#[test]
fn test_extract_foreground_objects_rgb() {
    let (mut rgb, mut mask) = rgb_mask_nonsquare();
    let (labels, _, _) = mask::count_labels(&mask);
    let contours = lines::extract_contours(&mask, Some(&labels));
    let bounding_boxes = lines::extract_bounding_boxes(&contours, None);

    let objects = objects::extract_foreground_objects(
        &mut rgb,
        &mut mask,
        &bounding_boxes,
        &labels,
        None,
        None,
    );

    let objects = objects.iter().map(|x| x).collect::<Vec<_>>();

    assert_eq!(objects[0].dimensions(), (3, 3));
    assert_eq!(objects[1].dimensions(), (3, 3));

    for i in 0..3 {
        for j in 0..3 {
            if i == 0 && j == 0 {
                assert_eq!(objects[0].get_pixel(i, j).0, [0, 0, 0]);
            } else {
                assert_eq!(objects[0].get_pixel(i, j).0, [100, 100, 100]);
            }
        }
    }

    for i in 0..3 {
        for j in 0..3 {
            if i == 0 && j == 0 {
                assert_eq!(objects[1].get_pixel(i, j).0[0], 0);
            } else {
                assert_eq!(objects[1].get_pixel(i, j).0, [200, 200, 200]);
            }
        }
    }

    let resized_objects = objects::extract_foreground_objects(
        &mut rgb,
        &mut mask,
        &bounding_boxes,
        &labels,
        Some((6, 6)),
        Some("linear"),
    );

    let resized_objects = resized_objects.iter().map(|x| x).collect::<Vec<_>>();

    assert_eq!(resized_objects[0].dimensions(), (6, 6));
    assert_eq!(resized_objects[1].dimensions(), (6, 6));

    for i in 0..5 {
        for j in 0..5 {
            if i < 3 && j < 3 {
                assert!(resized_objects[0].get_pixel(i, j).0[0] < 100);
            } else {
                assert_eq!(resized_objects[0].get_pixel(i, j).0, [100, 100, 100]);
            }
        }
    }

    for i in 0..5 {
        for j in 0..5 {
            if i < 3 && j < 3 {
                assert!(resized_objects[1].get_pixel(i, j).0[0] < 200);
            } else {
                assert_eq!(resized_objects[1].get_pixel(i, j).0, [200, 200, 200]);
            }
        }
    }
}

#[test]
fn test_extract_background_objects_gray() {
    let (mut gray, mut mask) = gray_mask_nonsquare();
    let (labels, _, _) = mask::count_labels(&mask);
    let contours = lines::extract_contours(&mask, Some(&labels));
    let bounding_boxes = lines::extract_bounding_boxes(&contours, None);

    let objects = objects::extract_background_objects(
        &mut gray,
        &mut mask,
        &bounding_boxes,
        &labels,
        None,
        None,
    );

    let objects = objects.iter().map(|x| x).collect::<Vec<_>>();

    assert_eq!(objects[0].dimensions(), (3, 3));
    assert_eq!(objects[1].dimensions(), (3, 3));

    for i in 0..3 {
        for j in 0..3 {
            assert_eq!(objects[0].get_pixel(i, j).0[0], 0);
        }
    }

    for i in 0..3 {
        for j in 0..3 {
            assert_eq!(objects[1].get_pixel(i, j).0[0], 0);
        }
    }

    let resized_objects = objects::extract_background_objects(
        &mut gray,
        &mut mask,
        &bounding_boxes,
        &labels,
        Some((6, 6)),
        Some("linear"),
    );

    let resized_objects = resized_objects.iter().map(|x| x).collect::<Vec<_>>();

    assert_eq!(resized_objects[0].dimensions(), (6, 6));
    assert_eq!(resized_objects[1].dimensions(), (6, 6));

    for i in 0..5 {
        for j in 0..5 {
            assert_eq!(resized_objects[0].get_pixel(i, j).0[0], 0);
        }
    }
}

#[test]
fn test_extract_background_objects_rgb() {
    let (mut rgb, mut mask) = rgb_mask_nonsquare();
    let (labels, _, _) = mask::count_labels(&mask);
    let contours = lines::extract_contours(&mask, Some(&labels));
    let bounding_boxes = lines::extract_bounding_boxes(&contours, None);

    let objects = objects::extract_background_objects(
        &mut rgb,
        &mut mask,
        &bounding_boxes,
        &labels,
        None,
        None,
    );

    let objects = objects.iter().map(|x| x).collect::<Vec<_>>();

    assert_eq!(objects[0].dimensions(), (3, 3));
    assert_eq!(objects[1].dimensions(), (3, 3));

    for i in 0..3 {
        for j in 0..3 {
            assert_eq!(objects[0].get_pixel(i, j).0, [0, 0, 0]);
        }
    }

    for i in 0..3 {
        for j in 0..3 {
            assert_eq!(objects[1].get_pixel(i, j).0, [0, 0, 0]);
        }
    }

    let resized_objects = objects::extract_background_objects(
        &mut rgb,
        &mut mask,
        &bounding_boxes,
        &labels,
        Some((6, 6)),
        Some("linear"),
    );

    let resized_objects = resized_objects.iter().map(|x| x).collect::<Vec<_>>();

    assert_eq!(resized_objects[0].dimensions(), (6, 6));
    assert_eq!(resized_objects[1].dimensions(), (6, 6));

    for i in 0..5 {
        for j in 0..5 {
            assert_eq!(resized_objects[0].get_pixel(i, j).0, [0, 0, 0]);
        }
    }
}

#[test]
fn test_extract_all_objects_gray() {
    let (mut gray, mut mask) = gray_mask();
    let (labels, _, _) = mask::count_labels(&mask);
    let contours = lines::extract_contours(&mask, Some(&labels));
    let bounding_boxes = lines::extract_bounding_boxes(&contours, None);

    let (objects, foreground_objects, background_objects, _binary_objects) = objects::extract_all_objects(
        &mut gray,
        &mut mask,
        &bounding_boxes,
        &labels,
        None,
        None,
    );

    let objects_single = objects::extract_objects(
        &mut gray,
        &bounding_boxes,
        None,
        None,
    );

    let foreground_objects_single = objects::extract_foreground_objects(
        &mut gray,
        &mut mask,
        &bounding_boxes,
        &labels,
        None,
        None,
    );

    let background_objects_single = objects::extract_background_objects(
        &mut gray,
        &mut mask,
        &bounding_boxes,
        &labels,
        None,
        None,
    );

    let objects = objects.iter().map(|x| x).collect::<Vec<_>>();
    let foreground_objects = foreground_objects.iter().map(|x| x).collect::<Vec<_>>();
    let background_objects = background_objects.iter().map(|x| x).collect::<Vec<_>>();

    let objects_single = objects_single.iter().map(|x| x).collect::<Vec<_>>();
    let foreground_objects_single = foreground_objects_single.iter().map(|x| x).collect::<Vec<_>>();
    let background_objects_single = background_objects_single.iter().map(|x| x).collect::<Vec<_>>();

    assert_eq!(objects.len(), objects_single.len());
    assert_eq!(foreground_objects.len(), foreground_objects_single.len());
    assert_eq!(background_objects.len(), background_objects_single.len());

    for i in 0..objects.len() {
        assert_eq!(objects[i].dimensions(), objects_single[i].dimensions());
        assert_eq!(foreground_objects[i].dimensions(), foreground_objects_single[i].dimensions());
        assert_eq!(background_objects[i].dimensions(), background_objects_single[i].dimensions());
    }

    for i in 0..objects.len() {
        for j in 0..objects[i].dimensions().0 {
            for k in 0..objects[i].dimensions().1 {
                assert_eq!(objects[i].get_pixel(j, k).0[0], objects_single[i].get_pixel(j, k).0[0]);
                assert_eq!(foreground_objects[i].get_pixel(j, k).0[0], foreground_objects_single[i].get_pixel(j, k).0[0]);
                assert_eq!(background_objects[i].get_pixel(j, k).0[0], background_objects_single[i].get_pixel(j, k).0[0]);
            }
        }
    }
}    

#[test]
fn test_extract_all_objects_rgb() {
    let (mut rgb, mut mask) = rgb_mask();
    let (labels, _, _) = mask::count_labels(&mask);
    let contours = lines::extract_contours(&mask, Some(&labels));
    let bounding_boxes = lines::extract_bounding_boxes(&contours, None);

    let (objects, foreground_objects, background_objects, _binary_objects) = objects::extract_all_objects(
        &mut rgb,
        &mut mask,
        &bounding_boxes,
        &labels,
        None,
        None,
    );

    let objects_single = objects::extract_objects(
        &mut rgb,
        &bounding_boxes,
        None,
        None,
    );

    let foreground_objects_single = objects::extract_foreground_objects(
        &mut rgb,
        &mut mask,
        &bounding_boxes,
        &labels,
        None,
        None,
    );

    let background_objects_single = objects::extract_background_objects(
        &mut rgb,
        &mut mask,
        &bounding_boxes,
        &labels,
        None,
        None,
    );

    let objects = objects.iter().map(|x| x).collect::<Vec<_>>();
    let foreground_objects = foreground_objects.iter().map(|x| x).collect::<Vec<_>>();
    let background_objects = background_objects.iter().map(|x| x).collect::<Vec<_>>();

    let objects_single = objects_single.iter().map(|x| x).collect::<Vec<_>>();
    let foreground_objects_single = foreground_objects_single.iter().map(|x| x).collect::<Vec<_>>();
    let background_objects_single = background_objects_single.iter().map(|x| x).collect::<Vec<_>>();

    assert_eq!(objects.len(), objects_single.len());
    assert_eq!(foreground_objects.len(), foreground_objects_single.len());
    assert_eq!(background_objects.len(), background_objects_single.len());

    for i in 0..objects.len() {
        assert_eq!(objects[i].dimensions(), objects_single[i].dimensions());
        assert_eq!(foreground_objects[i].dimensions(), foreground_objects_single[i].dimensions());
        assert_eq!(background_objects[i].dimensions(), background_objects_single[i].dimensions());
    }

    for i in 0..objects.len() {
        for j in 0..objects[i].dimensions().0 {
            for k in 0..objects[i].dimensions().1 {
                assert_eq!(objects[i].get_pixel(j, k).0, objects_single[i].get_pixel(j, k).0);
                assert_eq!(foreground_objects[i].get_pixel(j, k).0, foreground_objects_single[i].get_pixel(j, k).0);
                assert_eq!(background_objects[i].get_pixel(j, k).0, background_objects_single[i].get_pixel(j, k).0);
            }
        }
    }
}

#[test]
fn test_transform_resize() {
    let mut gray = DynamicImage::new_luma8(10, 10).to_luma8();
    let mut mask = DynamicImage::new_luma16(10, 10).to_luma16();

    for i in 2..8 {
        for j in 2..8 {
            gray.get_pixel_mut(i, j).0 = [100];
            mask.get_pixel_mut(i, j).0 = [1];
        }
    }

    let resized_gray = transform::resize(&mut gray, 5, 5, "nearest");
    let resized_mask = transform::resize(&mut mask, 5, 5, "nearest");

    assert_eq!(resized_gray.dimensions(), (5, 5));
    assert_eq!(resized_mask.dimensions(), (5, 5));
}

#[test]
fn test_transform_crop() {
    let mut gray = DynamicImage::new_luma8(10, 10).to_luma8();
    let mut mask = DynamicImage::new_luma16(10, 10).to_luma16();

    for i in 2..8 {
        for j in 2..8 {
            gray.get_pixel_mut(i, j).0 = [100];
            mask.get_pixel_mut(i, j).0 = [1];
        }
    }

    let crop = transform::crop(&mut gray, 2, 2, 5, 5);
    let crop_box = transform::crop_box(&mut gray, &vec![2.0, 2.0, 6.0, 6.0]);

    assert_eq!(crop.dimensions(), (5, 5));
    assert_eq!(crop_box.dimensions(), (5, 5));

    for i in 0..5 {
        for j in 0..5 {
            assert_eq!(crop.get_pixel(i, j).0[0], crop_box.get_pixel(i, j).0[0]);
        }
    }
}
