import cv2
import unittest
from LidarSegmentationLabelsValidator import LidarSegmentationLabelsValidator

# constants
height_main = 1024
length_main = 1024
amount_of_layers = 3
images_path_list = []
images_opencv_list = []

# images
image_path1 = 'test/pic (1).png'
image_path2 = 'test/pic (1) bad.png'
image_path3 = 'test/pic (2).png'
image_path4 = 'test/pic (2) bad.png'
image_path5 = 'test/pic (3) bad.png'
image_path_list = [image_path1, image_path2, image_path3, image_path4, image_path5]

# results
expected_result1 = None
expected_result2 = 'UNDEFINED COLOR ERROR'
expected_result3 = None
expected_result4 = 'SIZE ERROR'
expected_result5 = 'SIZE ERROR', 'UNDEFINED COLOR ERROR'
expected_results_list = [expected_result1, expected_result2, expected_result3, expected_result4, expected_result5]

# -------------------------------------------------------------------------------------------


class TestLidarSegmentationLabelsValidator(unittest.TestCase):
    def setUp(self):
        for image_path in image_path_list:
            images_opencv_list.append(cv2.imread(image_path))

        for image_path, images_opencv_list in


        for image, expected in zip(images_path_list, ):
            pass

        self.lidarSegmentationLabelsValidator1 = LidarSegmentationLabelsValidator(
            image_path1, image_main1, height_main, length_main, amount_of_layers)

        self.lidarSegmentationLabelsValidator2 = LidarSegmentationLabelsValidator(
            image_path2, image_main2, height_main, length_main, amount_of_layers)

        self.lidarSegmentationLabelsValidator3 = LidarSegmentationLabelsValidator(
            image_path3, image_main3, height_main, length_main, amount_of_layers)

        self.lidarSegmentationLabelsValidator4 = LidarSegmentationLabelsValidator(
            image_path4, image_main4, height_main, length_main, amount_of_layers)

        self.lidarSegmentationLabelsValidator5 = LidarSegmentationLabelsValidator(
            image_path5, image_main5, height_main, length_main, amount_of_layers)

    def test_validate_image_size(self):
        self.assertEqual(self.lidarSegmentationLabelsValidator1.validate_image_size(), None)
        self.assertEqual(self.lidarSegmentationLabelsValidator2.validate_image_size(), None)
        self.assertEqual(self.lidarSegmentationLabelsValidator3.validate_image_size(), None)
        self.assertEqual(self.lidarSegmentationLabelsValidator4.validate_image_size(), 'SIZE ERROR')
        self.assertEqual(self.lidarSegmentationLabelsValidator5.validate_image_size(), 'SIZE ERROR')

    def test_check_pixels(self):
        self.assertEqual(self.lidarSegmentationLabelsValidator1.check_pixels(), None)
        self.assertEqual(self.lidarSegmentationLabelsValidator2.check_pixels(), 'UNDEFINED COLOR ERROR')
        self.assertEqual(self.lidarSegmentationLabelsValidator3.check_pixels(), None)
        self.assertEqual(self.lidarSegmentationLabelsValidator4.check_pixels(), None)
        self.assertEqual(self.lidarSegmentationLabelsValidator5.check_pixels(), 'UNDEFINED COLOR ERROR')


if __name__ == "__main__":
    unittest.main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
""" Testing the Lidar Label Annotation
"""

import cv2
import time
import unittest
import numpy as np
from DataValidator import LabelValidator
from annotation_errors import AnnotationErrors
from lookup_table_web_of_rail import LABEL_RGB_PALETTE as LABEL_RGB_PALETTE_WEB_OF_RAIL
from lookup_table_lidar_segmentation import LABEL_RGB_PALETTE as LABEL_RGB_PALETTE_LIDAR
from lookup_table_simple_for_testing import LABEL_RGB_PALETTE as LABEL_RGB_PALETTE_SIMPLE


def generate_picture_1(height, length, color_map):
    photo = np.zeros((100, 100, 3), dtype="uint8")
    expected_result = [None, None]
    pic = cv2.imwrite('test/pic1.png', photo)
    return [photo, expected_result]


def generate_picture_3(height, length, color_map):
    photo = np.zeros((500, 4000, 3), dtype="uint8")
    photo[100:102, 300:302] = 185, 14, 24                       # non color map color
    return photo


class TestDataValidator(unittest.TestCase):
    def setUp(self):
        # constants
        self.height_main = 100
        self.length_main = 100
        self.amount_of_layers = 3
        self.folder = "createdTests/"
        self.image_path_list = []
        self.images_opencv_list = []
        self.expected_results_list = []
        self.SegmentationValidatorList = []
        self.color_map = LABEL_RGB_PALETTE_SIMPLE

        self.images_opencv_list.append(generate_picture_1(self.height_main, self.length_main, self.color_map)[0])
        self.expected_results_list.append(generate_picture_1(self.height_main, self.length_main, self.color_map)[1])
        print(self.images_opencv_list, self.expected_results_list)
        # self.images_opencv_list.append(generate_picture_2(self.height_main, self.length_main, self.color_map)[0])
        # self.images_opencv_list.append(generate_picture_3(self.height_main, self.length_main, self.color_map)[0])

"""
        for image_path, images_opencv in zip(self.image_path_list, self.images_opencv_list):
            self.SegmentationValidatorList.append(LabelValidator(image_path, images_opencv, self.height_main,
                                                                 self.length_main, self.amount_of_layers,
                                                                 LABEL_RGB_PALETTE_WEB_OF_RAIL))
            
            
    def test_check_errors(self):
        for segmentationValidator, expected in zip(self.SegmentationValidatorList, self.expected_results_list):
            # additionally check timing
            start_time = time.time()
            print(segmentationValidator.check_errors(), "; ", expected)
            end_time = time.time()
            print(end_time - start_time)

            self.assertEqual(segmentationValidator.check_errors(), expected)
"""

if __name__ == "__main__":
    a = TestDataValidator()
    a.setUp()
    #unittest.main()






