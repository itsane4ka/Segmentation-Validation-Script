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
