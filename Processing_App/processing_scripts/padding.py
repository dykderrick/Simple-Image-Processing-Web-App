# -*- coding: utf-8 -*-
# @Time    : 2020/6/10 8:21 下午
# @Author  : Yingke Ding
# @FileName: padding.py
# @Software: PyCharm
import os

import cv2
import numpy as np

from Processing_App.processing_scripts.image import Image
from Simple_Image_Processing_Web_App import settings


class PaddedImage(Image):
    """
    This class inherits from Image.
    Will pad background color to every image for the app.
    """

    def __init__(self, image_path, pad_w=700, pad_h=520):
        """
        Pad size will be 720 by 520 by default.
        :param image_path:
        :param pad_w: width of padded image
        :param pad_h: height of padded image
        """

        # cannot be less than (500, 500)
        if pad_w < 500 or pad_h < 500:
            raise Exception("PAD ERROR")

        super().__init__(image_path, "PADDED")
        self._pad_w = pad_w
        self._pad_h = pad_h
        self._background_color_decimal = (32, 32, 32)  # background color in decimal

        self._process()

    def _process(self):
        """
        Overwritten method.
        :return:
        """
        img = cv2.imread(self._image_path)

        # Resize to under (500, 500)
        while img.shape[0] > 500 or img.shape[1] > 500:
            img = cv2.resize(src=img, dsize=None, fx=0.8, fy=0.8, interpolation=cv2.INTER_AREA)

        # Get (resized) shape
        ht, wd, cc = img.shape

        # compute center offset
        xx = (self._pad_w - wd) // 2
        yy = (self._pad_h - ht) // 2

        # Pad background color into result
        self.processed_image = np.full((self._pad_h, self._pad_w, cc), self._background_color_decimal, dtype=np.uint8)

        # copy img image into center of result image
        self.processed_image[yy:yy + ht, xx:xx + wd] = img

    def save_processed_image(self):
        """
        Overwritten method.
        Will return a url other than absolute path because of rendering to html.
        :return:
        """
        save_path = \
            settings.MEDIA_ROOT + "/user_upload_images/" + self._image_file_name + "_PADDED" + self._image_file_type

        cv2.imwrite(save_path, self.processed_image)

        padded_url = "/images/user_upload_images/" + self._image_file_name + "_PADDED" + self._image_file_type

        return os.path.exists(save_path), padded_url
