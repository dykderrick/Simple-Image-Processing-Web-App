# -*- coding: utf-8 -*-
# @Time    : 2020/6/10 8:21 下午
# @Author  : Yingke Ding
# @FileName: padding.py
# @Software: PyCharm
import os

import cv2
import numpy as np

from Simple_Image_Processing_Web_App import settings


class ImagePadding:
    def __init__(self, image_path, pad_w=700, pad_h=520):
        if pad_w < 500 or pad_h < 500:
            raise Exception("PAD ERROR")

        self._pad_w = pad_w
        self._pad_h = pad_h
        self._background_color_decimal = (32, 32, 32)  # background color
        self._image_file_name = os.path.splitext(image_path)[0].split("/")[-1]
        self._image_file_type = os.path.splitext(image_path)[-1]  # include "."  e.g. "IMG.jpeg" -> ".jpeg"

        self._image_path = image_path
        self._cv2_image = cv2.imread(image_path)
        self._cv2_padded_image = self._pad_image()

    def _pad_image(self):
        # Resize to under (500, 500)
        while self._cv2_image.shape[0] > 500 or self._cv2_image.shape[1] > 500:
            self._cv2_image = cv2.resize(src=self._cv2_image, dsize=None, fx=0.8, fy=0.8, interpolation=cv2.INTER_AREA)

        # Get (resized) shape
        ht, wd, cc = self._cv2_image.shape

        # compute center offset
        xx = (self._pad_w - wd) // 2
        yy = (self._pad_h - ht) // 2

        # Pad background color into result
        result = np.full((self._pad_h, self._pad_w, cc), self._background_color_decimal, dtype=np.uint8)

        # copy img image into center of result image
        result[yy:yy + ht, xx:xx + wd] = self._cv2_image

        return result

    def save_padded_image(self):
        save_path = settings.MEDIA_ROOT + "/user_upload_images/" + self._image_file_name + "_PADDED" + self._image_file_type

        if not os.path.exists(save_path):
            cv2.imwrite(save_path, self._cv2_padded_image)

        padded_url = "/images/user_upload_images/" + self._image_file_name + "_PADDED" + self._image_file_type
        return os.path.exists(save_path), padded_url
