# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/6
# @Author  : Yingke Ding
# @File    : retrieve_image_info.py
# @Software: PyCharm
import os

import cv2
import numpy as np
from fs import filesize


class ImageInfo:
    """
    This class gets image's file size, height, width, and color info of an image.
    """

    def __init__(self, img_path, is_gray_image=False):
        """
        Constructor.
        :param img_path:
        :param is_gray_image: if True, color info will be different.
        """
        self._img_path = img_path
        self._is_gray_image = is_gray_image

        self._set_file_size()
        self._set_image_size()
        self._set_color_info()

    def _set_file_size(self):
        self._file_size = filesize.traditional(os.path.getsize(self._img_path))

    def _set_image_size(self):
        shape = cv2.imread(self._img_path).shape
        self._img_size = str(shape[1]) + " x " + str(shape[0])

    def _set_color_info(self):
        """
        This method actually doesn't have practical meaning.
        Just read 3 channels of an image, and traverse every pixel, get average value for each channel.
        :return:
        """
        if not self._is_gray_image:  # colorful image
            image = cv2.imread(self._img_path)
            rs = []
            gs = []
            bs = []

            for row_pixels in image:
                for pixel in row_pixels:
                    pixel = pixel.tolist()
                    rs.append(pixel[0])
                    gs.append(pixel[1])
                    bs.append(pixel[2])

            self._percentages = "Avg(R): " + str(int(sum(rs) / len(rs))) + ", " + \
                                "Avg(G): " + str(int(sum(gs) / len(rs))) + ", " + \
                                "Avg(B): " + str(int(sum(bs) / len(rs)))

        else:  # gray level image
            image = cv2.imread(self._img_path, cv2.IMREAD_GRAYSCALE)

            mean = float(np.mean(np.array(image)))
            self._percentages = "Avg(pixel): " + str(round(mean, 2))

    def _get_file_size(self):
        return self._file_size

    def _get_image_size(self):
        return self._img_size

    def _get_rgb_percentages(self):
        return self._percentages

    def info_getter(self):
        return {
            "file_size": self._get_file_size(),
            "image_size": self._get_image_size(),
            "color_percentages": self._get_rgb_percentages()
        }
