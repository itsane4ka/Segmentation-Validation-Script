"""
Author -- Oleksandr Kats
Contact -- oleksandr.kats@tmconnected.com
Begin date -- 17.08.2022
"""

# coding = utf - 8

import os
import cv2
import sys
import functools
import numpy as np
from lookup_table import LABEL_RGB_PALETTE


class LidarSegmentationLabelsValidator:
    def __init__(self, path, image, height_required, length_required, amount_of_layers_required):
        self.path = path
        self.image = image
        self.height_required = height_required
        self.length_required = length_required
        self.LABEL_RGB_PALETTE = LABEL_RGB_PALETTE
        self.amount_of_layers_required = amount_of_layers_required

        # checking if the file is in image
        if os.path.splitext(str(path))[1] == '.png':
            print('Image ', path, ':\t', end=' ')

    def open(self):
        cv2.imshow('res:', self.image)
        cv2.waitKey(0)

    def validate_image_size(self):
        if self.image.shape[0] != self.height_required or self.image.shape[1] != self.length_required \
                or self.image.shape[2] != self.amount_of_layers_required:
            return ['SIZE ERROR', self.image.shape]
        else:
            return None

    def check_pixels(self):
        error_exist = False
        pixels_counter = 0
        pixel_color_present = False
        pixels_wrong_colored = []
        pixels_wrong_colored_coordinates = []

        # making a numpy array of picture pixels
        pixel_array = np.asarray(cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB))
        pixel_array.resize(self.height_required * self.length_required, 3)

        for pixel in pixel_array:
            pixel_color_present = False
            for color_rgb in self.LABEL_RGB_PALETTE:
                if functools.reduce(lambda x, y: x and y, map(lambda p, q: p == q, pixel, color_rgb), True):
                    pixel_color_present = True
                    break
            if not pixel_color_present:
                pixels_wrong_colored_coordinates.append([pixels_counter // 4000, pixels_counter % 4000])
                pixels_wrong_colored.append(pixel)
                error_exist = True
            pixels_counter += 1
        if error_exist:
            return ['UNDEFINED COLOR ERROR', pixels_wrong_colored, pixels_wrong_colored_coordinates]
        else:
            return None


if __name__ == '__main__':
    # dealing with the folder
    files_in_dir = os.listdir('test')
    print(len(files_in_dir), 'elements in folder.\n')

    # constant size
    errors_list = []
    height_main = 1024
    length_main = 1024
    amount_of_layers = 3

    for file_name in files_in_dir:
        try:
            # opening the image
            image_path = 'test/' + file_name
            #image_path = 'test/pic (246) - Bad.png'
            image_main = cv2.imread(image_path)
        except:
            raise FileNotFoundError('Could not open the file!')

        # passing the image for validation
        img = LidarSegmentationLabelsValidator(image_path, image_main, height_main, length_main, amount_of_layers)
        if img.validate_image_size() is None and img.check_pixels() is None:
            print('ok')
        elif img.validate_image_size() is not None and img.check_pixels() is not None:
            print('ERRORS COLOR AND SIZE')
        elif img.validate_image_size() is not None and img.check_pixels() is None:
            print('ERROR SIZE')
        else:
            print('ERROR COLOR')
        #img.open()
