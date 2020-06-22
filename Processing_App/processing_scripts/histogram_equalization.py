# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/6
# @Author  : Yingke Ding
# @File    : histogram_equalization.py
# @Software: PyCharm
import os

import cv2
import numpy as np

from Simple_Image_Processing_Web_App import settings


class HistogramEqualizeImage:
    def __init__(self, image_path):
        self._image_file_name = os.path.splitext(image_path)[0].split("/")[-1]
        self._image_file_type = os.path.splitext(image_path)[-1]  # include "."  e.g. "IMG.jpeg" -> ".jpeg"
        self._image_path = image_path

        self._set_histogram_equalization_image()

    def _set_histogram_equalization_image(self):
        img = cv2.imread(self._image_path)
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        pixel_count = [0 for i in range(256)]

        for row_pixels in gray_img:
            for pixel in row_pixels:
                pixel_count[pixel] += 1

        cumulative_histogram = [0 for i in range(256)]
        for i in range(1, 256):
            cumulative_histogram[i] = cumulative_histogram[i - 1] + pixel_count[i]

        lookup_table = [int(element * 255 / (gray_img.shape[0] * gray_img.shape[1])) for element in cumulative_histogram]

        equalized_pixels = []
        for index, row_pixels in enumerate(gray_img):
            equalized_row_pixels = [lookup_table[pixel] for pixel in row_pixels]
            equalized_pixels.append(equalized_row_pixels)

        self.equalized_image = np.array(equalized_pixels, dtype=np.uint8)

    def save_equalized_image(self):
        save_path = settings.MEDIA_ROOT + "/user_upload_images/" + self._image_file_name + "_EQUALIZED" + self._image_file_type

        cv2.imwrite(save_path, self.equalized_image)

        return os.path.exists(save_path), save_path
