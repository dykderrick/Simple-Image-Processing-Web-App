# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/6
# @Author  : Yingke Ding
# @File    : laplacian_derivative.py
# @Software: PyCharm
import cv2

from Processing_App.processing_scripts.image import Image


class LaplacianImage(Image):
    def __init__(self, image_path):
        super().__init__(image_path, "LAPLACIAN")

        self.set_laplacian_image()

    def set_laplacian_image(self):
        img = cv2.imread(self._image_path)

        self.processed_image = cv2.Laplacian(img, cv2.CV_64F)  # TODO needs to be modified
