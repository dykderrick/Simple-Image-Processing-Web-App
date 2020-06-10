# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/6
# @Author  : Yingke Ding
# @File    : smoothing.py
# @Software: PyCharm
import cv2
import numpy as np


def get_smooth_image(img_path):
    img = cv2.imread(img_path)

    kernel = np.ones((5, 5), np.float32) / 25

    smoothed_img = cv2.filter2D(img, -1, kernel)  # TODO needs to be refactored

    return smoothed_img


if __name__ == '__main__':
    result = get_smooth_image("./images/IMG_0185.JPG")

    cv2.imshow("Image", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
