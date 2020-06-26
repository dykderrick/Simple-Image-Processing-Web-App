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

    def _median_smoothing(self, img, kernel, padding_way='ZERO'):
        padding_size = kernel // 2

        layer_size = len(img.shape)

        height, width = img.shape[:2]

        if layer_size == 3:  # rgb image
            mat_mutbase = np.zeros_like(img)
            for l in range(mat_mutbase.shape[2]):
                mat_mutbase[:, :, l] = self._median_smoothing(img[:, :, l], kernel, padding_way)
            return mat_mutbase
        elif layer_size == 2:  # gray
            mat_base = np.zeros((height + padding_size * 2, width + padding_size * 2), dtype=img.dtype)

            mat_base[padding_size:-padding_size, padding_size:-padding_size] = img

            if padding_way is 'ZERO':
                pass
            elif padding_way is 'REPLICA':
                for r in range(padding_size):
                    mat_base[r, padding_size:-padding_size] = img[0, :]
                    mat_base[-(1 + r), padding_size:-padding_size] = img[-1, :]
                    mat_base[padding_size:-padding_size, r] = img[:, 0]
                    mat_base[padding_size:-padding_size, -(1 + r)] = img[:, -1]

            result = np.zeros((height, width), dtype=img.dtype)

            for x in range(height):
                for y in range(width):
                    line = mat_base[x:x + kernel, y:y + kernel].flatten()
                    line = np.sort(line)
                    result[x, y] = line[(kernel * kernel) // 2]
            return result

    def _process(self):
        """
        Overwritten method.
        Will use box filter.
        :return:
        """

        img = cv2.imread(self._image_path)

        """
        # OpenCV implementation
        
        img = cv2.imread(self._image_path)

        # defines a box filter.
        kernel = np.ones((3, 3), np.float32) / 9

        # use OpenCV build-in method to calc convolution.
        self.processed_image = cv2.filter2D(img, -1, kernel)
        """

        kernel = 5

        self.processed_image = self._median_smoothing(img, kernel)
