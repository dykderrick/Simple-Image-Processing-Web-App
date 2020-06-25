# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/6
# @Author  : Yingke Ding
# @File    : gray_scale.py
# @Software: PyCharm
import cv2
import numpy as np

from Processing_App.processing_scripts.image import Image


def _convert2gray(raw_image):
    """
    Use numpy to calc grayscale image.
    :param raw_image: r, g, b channels ndarray of image
    :return: general gray level image
    """
    # get r, g, b channels
    r, g, b = raw_image[:, :, 0], raw_image[:, :, 1], raw_image[:, :, 2]

    # calc general gray level
    # See reference: https://en.wikipedia.org/wiki/Grayscale#Converting_color_to_grayscale
    return 0.2989 * r + 0.5870 * g + 0.1140 * b


class GrayImage(Image):
    """
    This class defines a process of making image into a specific gray scale level.
    For example, gray_scale = 128 will make the image become a gray image with every pixel value is between 0 and 128.
    """

    def __init__(self, image_path, gray_scale):
        """
        Constructor.
        :param image_path: absolute path of image to be processed.
        :param gray_scale: int
        """
        super().__init__(image_path, str(gray_scale) + "GRAYED")
        self._gray_scale = int(gray_scale)

        self._process()

    def _convert2gray_scale(self, gray_img):
        """
        Convert a gray image into a specific gray scale.
        Just remapping.
        :param gray_img: single channel of image in a type of ndarray.
        :return: scaled_pixels ndarray.
        """
        scaled_pixels = []

        for index, row_pixels in enumerate(gray_img):
            # restrict gray range to [0, gray_scale]
            scaled_row_pixels = [int(pixel * self._gray_scale / 255) for pixel in row_pixels]
            scaled_pixels.append(scaled_row_pixels)

        return np.array(scaled_pixels, dtype=np.uint8)

    def _process(self):
        """
        Overwritten method.
        Will specify self.process_image to grayscale.
        :return: None
        """
        # load raw image
        raw_image = cv2.imread(self._image_path)

        # convert to general gray level
        gray_img = _convert2gray(raw_image)

        self.processed_image = self._convert2gray_scale(gray_img)
