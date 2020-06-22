# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/6
# @Author  : Yingke Ding
# @File    : gray_scale.py
# @Software: PyCharm
import cv2
import numpy as np

from Processing_App.processing_scripts.image import Image


class GrayImage(Image):
    def __init__(self, image_path, gray_scale):
        super().__init__(image_path, str(gray_scale) + "GRAYED")
        self._gray_scale = int(gray_scale)

        self._process()

    def _process(self):
        img = cv2.imread(self._image_path)
        h, w, c = img.shape

        if c != 3:
            raise Exception("ALREADY GRAYED")

        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # TODO
        scaled_pixels = []
        for index, row_pixels in enumerate(gray_img):
            scaled_row_pixels = [int(pixel * self._gray_scale / 255) for pixel in row_pixels]
            scaled_pixels.append(scaled_row_pixels)

        self.processed_image = np.array(scaled_pixels, dtype=np.uint8)
