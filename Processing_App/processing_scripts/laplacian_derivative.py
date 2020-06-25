# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/6
# @Author  : Yingke Ding
# @File    : laplacian_derivative.py
# @Software: PyCharm
import cv2
import numpy as np

from Processing_App.processing_scripts.image import Image


class LaplacianImage(Image):
    """
    This class defines a 2nd derivative process method for image -- laplacian filter.
    """

    def __init__(self, image_path):
        """
        Constructor.
        :param image_path:
        """
        super().__init__(image_path, "LAPLACIAN")

        self._process()

    def _process(self):
        """
        Overwritten method.
        Make convolution between laplacian filter and the grayed image of raw image.
        :return:
        """

        # OpenCV implementation

        # img = cv2.imread(self._image_path)
        # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # self.processed_image = cv2.Laplacian(img, cv2.CV_64F)

        # My implementation
        img = cv2.imread(self._image_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        laplace_filter = np.array([
            [0, 1, 0],
            [1, -4, 1],
            [0, 1, 0],
        ])

        m, n = gray.shape

        self.processed_image = np.copy(gray)

        for i in range(1, m - 1):
            for j in range(1, n - 1):
                result = np.sum(laplace_filter * gray[i - 1:i + 2, j - 1:j + 2])

                self.processed_image[i, j] = gray[i, j] + 0.1 * result  # Add a sharpen to result
