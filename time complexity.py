""" Testing the time of check_pixel() function
"""

import cv2
import time
import unittest
import numpy as np
from random import randrange
import matplotlib.pyplot as plt
from DataValidator import LabelValidator
from annotation_errors import AnnotationErrors
from lookup_table_web_of_rail import LABEL_RGB_PALETTE as LABEL_RGB_PALETTE_WEB_OF_RAIL
from lookup_table_lidar_segmentation import LABEL_RGB_PALETTE as LABEL_RGB_PALETTE_LIDAR
from lookup_table_simple_for_testing import LABEL_RGB_PALETTE as LABEL_RGB_PALETTE_SIMPLE


def generate_pic_three_colors(photo, height, length):
    for i in range((height * length * 2) // 3):
        x = randrange(height)
        y = randrange(length)
        bad_color = [10, 0, 255]                                                                # non color-map color
        if i % 3 == 0 or i % 3 == 1:
            photo[x][y] = [255, 255, 255]
        else:
            photo[x][y] = bad_color


def generate_picture(height, length, color_map, counter):
    photo = np.zeros((height, length, 3), dtype="uint8")
    generate_pic_three_colors(photo, height, length)
    picture_dir = "createdTests/pic" + str(counter) + ".png"
    pic = cv2.imwrite(picture_dir, photo)
    return [picture_dir, photo]


class TestDataValidator(unittest.TestCase):
    def setUp(self):
        # constants and useful variables
        self.height_main = 100
        self.length_main = 100
        self.amount_of_layers = 3
        self.folder = "createdTests/"
        self.timing = []
        self.image_path_list = []
        self.images_opencv_list = []
        self.pixels_on_picture = []
        self.SegmentationValidatorList = []
        self.color_map = LABEL_RGB_PALETTE_SIMPLE

        counter = 0
        pixels_on_picture = np.array([], dtype="int32")
        for i, j in zip(range(100, 2000, 300), range(100, 2000, 300)):
            self.image_path_list.append(generate_picture(i, j, self.color_map, counter)[0])
            self.images_opencv_list.append(generate_picture(i, j, self.color_map, counter)[1])
            self.pixels_on_picture = np.append(self.pixels_on_picture, i * j)
            counter += 1

        for image_path, images_opencv in zip(self.image_path_list, self.images_opencv_list):
            self.SegmentationValidatorList.append(LabelValidator(image_path, images_opencv, self.height_main,
                                                                 self.length_main, self.amount_of_layers,
                                                                 LABEL_RGB_PALETTE_SIMPLE))
        return pixels_on_picture

    def test_time(self):
        counter = 0
        self.timing = np.array([], dtype="int32")
        pixels_on_picture = np.array([], dtype="int32")

        for segmentationValidator in self.SegmentationValidatorList:
            start_time = time.time()
            segmentationValidator.check_errors()
            end_time = time.time()
            print("pic ", counter, ": ", end_time - start_time)
            self.timing = np.append(self.timing, end_time - start_time)
            counter += 1

        print(self.timing)
        print(self.pixels_on_picture)
        #plt.plot(self.pixels_on_picture, self.timing)

        fig, ax = plt.subplots()
        ax.plot(self.pixels_on_picture, self.timing)
        ax.grid()

        plt.title("Time complexity", fontsize=20)
        plt.xlabel("pixels amount (mil)")
        plt.ylabel("time processing")

        ax.vlines(1000000, self.timing.min(), self.timing.max(), color='r', linestyles="--")
        ax.vlines(2000000, self.timing.min(), self.timing.max(), color='r', linestyles="--")

        plt.savefig("time_complexity.png")
        plt.show()


if __name__ == "__main__":
    a = TestDataValidator()
    a.setUp()
    a.test_time()





