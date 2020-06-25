# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/6
# @Author  : Yingke Ding
# @File    : histogram_equalization.py
# @Software: PyCharm
import cv2
import numpy as np

from Processing_App.processing_scripts.image import Image


class HistogramEqualizeImage(Image):
    """
    This class inherits from Image.
    Will calc histogram equalized image of an image.
    """

    def __init__(self, image_path):
        """
        Constructor.
        Specify process_type with "EQUALIZED".
        :param image_path:
        """
        super().__init__(image_path, "EQUALIZED")
        self._process()

    def _process(self):
        """
        Overwritten method.
        Histogram equalization makes each gray pixel in a gray level image to be equally distributed.
        Use Algorithm 5.1 in Chapter 4.2.
        :return:
        """
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

        self.processed_image = np.array(equalized_pixels, dtype=np.uint8)
