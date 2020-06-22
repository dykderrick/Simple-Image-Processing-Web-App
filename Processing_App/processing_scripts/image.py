# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/22
# @Author  : Yingke Ding
# @File    : image.py
# @Software: PyCharm
import os

import cv2

from Simple_Image_Processing_Web_App import settings


class Image:
    def __init__(self, image_path, process_type):
        self._image_path = image_path
        self._image_file_name = os.path.splitext(image_path)[0].split("/")[-1]
        self._image_file_type = os.path.splitext(image_path)[-1]  # include "."  e.g. "IMG.jpeg" -> ".jpeg"
        self.processed_image = None
        self.process_type = process_type

    def _process(self):
        pass

    def save_processed_image(self):
        save_path = settings.MEDIA_ROOT + "/user_upload_images/" + self._image_file_name + "_" + self.process_type + self._image_file_type

        cv2.imwrite(save_path, self.processed_image)

        return os.path.exists(save_path), save_path
