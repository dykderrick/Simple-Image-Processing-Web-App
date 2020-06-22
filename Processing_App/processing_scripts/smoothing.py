# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/6
# @Author  : Yingke Ding
# @File    : smoothing.py
# @Software: PyCharm
import cv2
import numpy as np

from Processing_App.processing_scripts.image import Image


class SmoothedImage(Image):
    def __init__(self, image_path):
        super().__init__(image_path, "SMOOTHED")

        self._set_smooth_image()

    def _set_smooth_image(self):
        img = cv2.imread(self._image_path)

        kernel = np.ones((5, 5), np.float32) / 25

        self.processed_image = cv2.filter2D(img, -1, kernel)  # TODO needs to be refactored
