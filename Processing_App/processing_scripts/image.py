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
    """
    This class defines the general prototype for all image processing function.
    Other processedImage class inherits it to overwrite process method.
    """

    def __init__(self, image_path, process_type):
        """
        Initialization.
        :param image_path: the absolute path for any image file
        :param process_type: a string indicating what type of process (e.g. SMOOTHED, 90LEFT etc.)
        """
        self._image_path = image_path
        self._image_file_name = os.path.splitext(image_path)[0].split("/")[-1]
        self._image_file_type = os.path.splitext(image_path)[-1]  # include "."  e.g. "IMG.jpeg" -> ".jpeg"
        self.processed_image = None
        self.process_type = process_type

    def _process(self):
        """
        Actually it would be an abstract method if it were Java.
        Let subclasses to overwrite.
        :return:
        """
        pass

    def save_processed_image(self):
        """
        Every processed image has to be saved into MEDIA_ROOT.
        This method saves the processed image with a specific name containing process type.
        :return: (boolean, string) boolean indicating if the saving is successful, and string is the saved path.
        """
        save_path = settings.MEDIA_ROOT\
            + "/user_upload_images/" + self._image_file_name + "_" + self.process_type + self._image_file_type

        cv2.imwrite(save_path, self.processed_image)

        return os.path.exists(save_path), save_path
