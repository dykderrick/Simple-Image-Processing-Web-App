# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/6
# @Author  : Yingke Ding
# @File    : rotate.py
# @Software: PyCharm
import cv2
import numpy as np

from Processing_App.processing_scripts.image import Image


def _rotate_k_meaning(k):
    if k == 1:
        return "90LEFT"
    elif k == 2:
        return "180"
    elif k == 3:
        return "90RIGHT"


class RotatedImage(Image):
    def __init__(self, image_path, rotate_k):
        """
        :param image_path:
        :param rotate_k: Number of times the array is rotated by 90 degrees.
        """
        super().__init__(image_path, _rotate_k_meaning(rotate_k))
        self._rotate_k = rotate_k

        self._process()

    def _process(self, axes=(0, 1)):
        # TODO need to be modified
        """
        :param axes: The array is rotated in the plane defined by the axes.
        :return:
        """
        raw_img = cv2.imread(self._image_path)

        axes = tuple(axes)
        if len(axes) != 2:
            raise ValueError("len(axes) must be 2.")

        if axes[0] == axes[1] or np.abs(axes[0] - axes[1]) == raw_img.ndim:
            raise ValueError("Axes must be different.")

        if (axes[0] >= raw_img.ndim or axes[0] < -raw_img.ndim
                or axes[1] >= raw_img.ndim or axes[1] < -raw_img.ndim):
            raise ValueError("Axes={} out of range for array of ndim={}."
                             .format(axes, raw_img.ndim))

        self._rotate_k %= 4

        if self._rotate_k == 0:
            self.processed_image = raw_img[:]
        if self._rotate_k == 2:
            self.processed_image = np.flip(np.flip(raw_img, axes[0]), axes[1])

        axes_list = np.arange(0, raw_img.ndim)
        (axes_list[axes[0]], axes_list[axes[1]]) = (axes_list[axes[1]],
                                                    axes_list[axes[0]])

        if self._rotate_k == 1:
            self.processed_image = np.transpose(np.flip(raw_img, axes[1]), axes_list)
        else:
            # k == 3
            self.processed_image = np.flip(np.transpose(raw_img, axes_list), axes[1])
