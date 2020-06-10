# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/6
# @Author  : Yingke Ding
# @File    : gray_scale.py
# @Software: PyCharm
import cv2
import numpy as np


def get_gray_scale_image(img_path, gray_scale):
    img = cv2.imread(img_path)
    h, w, c = img.shape

    if c != 3:
        raise Exception("ALREADY GRAYED")

    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # TODO
    scaled_pixels = []
    for index, row_pixels in enumerate(gray_img):
        scaled_row_pixels = [int(pixel * gray_scale / 255) for pixel in row_pixels]
        scaled_pixels.append(scaled_row_pixels)

    scaled_gray_img = np.array(scaled_pixels, dtype=np.uint8)

    return scaled_gray_img


if __name__ == '__main__':
    result = get_gray_scale_image("./images/IMG_0185.JPG", 128)

    cv2.imshow("Image", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
