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
    """
    This class defines a process of smoothing the raw image.
    """

    def __init__(self, image_path):
        super().__init__(image_path, "SMOOTHED")

        self._process()

    def _process(self):
        """
        Overwritten method.
        Will use box filter.
        :return:
        """
        img = cv2.imread(self._image_path)

        # defines a box filter.
        kernel = np.ones((3, 3), np.float32) / 9

        # use OpenCV build-in method to calc convolution.
        self.processed_image = cv2.filter2D(img, -1, kernel)
