# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/6
# @Author  : Yingke Ding
# @File    : resize.py
# @Software: PyCharm
import cv2

from Processing_App.processing_scripts.image import Image


class ResizedImage(Image):
    def __init__(self, image_path, scale_percent):
        self._scale_percent = int(float(scale_percent) * 100)

        super().__init__(image_path, str(self._scale_percent) + "RESIZED")

        self._process(self._scale_percent)

    def _process(self, scale_percent=50):
        img = cv2.imread(self._image_path)

        # calculate the 50 percent of original dimensions
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)

        dsize = (width, height)

        self.processed_image = cv2.resize(img, dsize)
