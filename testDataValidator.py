""" Testing the Lidar Label Annotation
"""
from unittest import TestCase

import cv2
import time
import random
import unittest
import numpy as np
from random import randrange
from DataValidator import LabelValidator
from annotation_errors import AnnotationErrors
from lookup_table_web_of_rail import LABEL_RGB_PALETTE as LABEL_RGB_PALETTE_WEB_OF_RAIL
from lookup_table_lidar_segmentation import LABEL_RGB_PALETTE as LABEL_RGB_PALETTE_LIDAR
from lookup_table_simple_for_testing import LABEL_RGB_PALETTE as LABEL_RGB_PALETTE_SIMPLE


def generate_pic_two_colors(photo, height, length):
    """ This method recreates a full-black picture into a black and white picture.
    Also have to mention that black and white are the only two colors located in
    the color map.
    """
    for i in range(height * length // 2):
        x = randrange(height)
        y = randrange(length)
        photo[x][y] = [255, 255, 255]


def generate_picture_1(height, length, color_map):
    """ This method is supposed to check a case when:
    1. the size is correct
    2. the colors are correct.
    (the picture is completely correct)
    """
    photo = np.zeros((height, length, 3), dtype="uint8")
    generate_pic_two_colors(photo, height, length)
    expected_result = [None, None]
    picture_dir = "createdTests/pic1.png"
    pic = cv2.imwrite(picture_dir, photo)
    return [picture_dir, photo, expected_result]


def generate_picture_2(height, length, color_map):
    """ This method is supposed to check a case when:
    1. the size is incorrect
    2. the colors are correct.
    """
    length += 10                                                                               # making it wrong size
    photo = np.zeros((height, length, 3), dtype="uint8")
    generate_pic_two_colors(photo, height, length)
    expected_result = [[AnnotationErrors.SIZE_ERROR, (height, length, 3)], None]

    picture_dir = "createdTests/pic2.png"
    pic = cv2.imwrite(picture_dir, photo)                                                      # putting picture visible
    return [picture_dir, photo, expected_result]                                               # into a folder


def generate_picture_3(height, length, color_map):
    """ This method is supposed to check a case when:
    1. the size is correct
    2. the colors are incorrect.
    """
    bad_color = [10, 0, 255]                                                                    # non color-map color
    photo = np.zeros((height, length, 3), dtype="uint8")
    generate_pic_two_colors(photo, height, length)
    photo[height // 2][length // 2] = bad_color
    bad_color[0], bad_color[2] = bad_color[2], bad_color[0]                                     # rgb --> bgr(for OpenCV)
    expected_result = [None, [AnnotationErrors.UNDEFINED_COLOR_ERROR, [(bad_color, [height // 2, length // 2])]]]

    picture_dir = "createdTests/pic3.png"
    pic = cv2.imwrite(picture_dir, photo)
    return [picture_dir, photo, expected_result]


def generate_picture_4(height, length, color_map):
    """ This method is supposed to check a case when:
    1. the size is incorrect
    2. the colors are incorrect.
    """
    height += 10                                                                                  # making it wrong size
    bad_color = [10, 0, 255]                                                                      # non color-map color
    photo = np.zeros((height, length, 3), dtype="uint8")
    generate_pic_two_colors(photo, height, length)
    photo[height // 2, length // 2] = bad_color
    bad_color[0], bad_color[2] = bad_color[2], bad_color[0]                                        # rgb --> bgr
    expected_result = [[AnnotationErrors.SIZE_ERROR, (height, length, 3)],
                       [AnnotationErrors.UNDEFINED_COLOR_ERROR, [(bad_color, [height // 2, length // 2])]]]

    picture_dir = "createdTests/pic4.png"
    pic = cv2.imwrite(picture_dir, photo)
    return [picture_dir, photo, expected_result]


def generate_picture_5(height, length, color_map):
    """ This method is supposed to check a case when:
    1. the size is correct
    2. the colors are incorrect.
    Including many bad pixels.
    """
    bad_color = [10, 0, 255]  # non color-map color
    photo = np.zeros((height, length, 3), dtype="uint8")
    generate_pic_two_colors(photo, height, length)

    # random generation is bad here, so we create array ba ourselves
    x_error_color_list = [7, 3, 10, 94, 68, 5, 46, 73, 26, 90]
    x_error_color_list.sort()
    y_error_color_list = [40, 9, 19, 80, 47, 69, 2, 52, 92, 48]

    bad_color_pixels_list = []
    for x_error_color, y_error_color in zip(x_error_color_list, y_error_color_list):
        photo[x_error_color][y_error_color] = bad_color
        bad_color_pixels_list.append((bad_color, [x_error_color, y_error_color]))
    bad_color[0], bad_color[2] = bad_color[2], bad_color[0]  # rgb --> bgr
    expected_result = [None, [AnnotationErrors.UNDEFINED_COLOR_ERROR, bad_color_pixels_list]]
    picture_dir = "createdTests/pic5.png"
    pic = cv2.imwrite(picture_dir, photo)
    return [picture_dir, photo, expected_result]


class DataValidatorTest(unittest.TestCase):
    def setUp(self):
        # constants and useful variables
        self.height_main = 100
        self.length_main = 100
        self.amount_of_layers = 3
        self.folder = "createdTests/"
        self.image_path_list = []
        self.images_opencv_list = []
        self.expected_results_list = []
        self.SegmentationValidatorList = []
        self.color_map = LABEL_RGB_PALETTE_SIMPLE
        self.list_of_picture_generation_funcs = [generate_picture_1, generate_picture_2,
                                                 generate_picture_3, generate_picture_4, generate_picture_5]

        # generating pictures using functions above
        for func in self.list_of_picture_generation_funcs:
            self.image_path_list.append(func(self.height_main, self.length_main, self.color_map)[0])
            self.images_opencv_list.append(func(self.height_main, self.length_main, self.color_map)[1])
            self.expected_results_list.append(func(self.height_main, self.length_main, self.color_map)[2])

        # generating LabelValidator objects
        for image_path, images_opencv in zip(self.image_path_list, self.images_opencv_list):
            self.SegmentationValidatorList.append(LabelValidator(image_path, images_opencv,
                                                                 self.height_main, self.length_main,
                                                                 self.amount_of_layers, self.color_map))

    def test_check_errors(self):
        """ This method is supposed to check the work of check_errors() function.
        Have to mention that there is no sense of checking validate_image_size() and check_errors()
        functions because check_errors() simply connects their work and returns a result.
        """
        counter = 0
        for labelValidator, expected in zip(self.SegmentationValidatorList,
                                            self.expected_results_list):
            # also checking the working time
            start_time = time.time()
            print(counter + 1, ": ", labelValidator.check_errors(), '; ', expected)
            end_time = time.time()
            print(end_time - start_time, end="\n")

            self.assertEqual(labelValidator.check_errors(), expected)
            counter += 1


if __name__ == "__main__":
    unittest.main()



