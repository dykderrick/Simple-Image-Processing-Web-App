# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/6
# @Author  : Yingke Ding
# @File    : retrieve_image_info.py
# @Software: PyCharm
import os

import cv2


class ImageInfo:
    def __init__(self, img_path):
        self._img_path = img_path
        self._set_file_size()
        self._set_image_size()
        self._set_rgb_percentages()

    def _set_file_size(self):
        # TODO: Needs to be refactored to KB, MB...
        self._file_size = str(os.path.getsize(self._img_path)) + " Bytes"

    def _set_image_size(self):
        shape = cv2.imread(self._img_path).shape
        self._img_size = str(shape[1]) + " x " + str(shape[0])

    def _set_rgb_percentages(self):
        # TODO: Needs to be reconsidered
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

        self._percentages = "R: " + str(round((sum(rs) / (len(rs) * 255)), 2)) + ", " + \
                            "G: " + str(round((sum(gs) / (len(gs) * 255)), 2)) + ", " + \
                            "B: " + str(round((sum(bs) / (len(bs) * 255)), 2))

    def _get_file_size(self):
        return self._file_size

    def _get_image_size(self):
        return self._img_size

    def _get_rgb_percentages(self):
        return self._percentages

    def info_getter(self):
        return {"file_size": self._get_file_size(),
                "image_size": self._get_image_size(),
                "rgb_percentages": self._get_rgb_percentages()
                }
