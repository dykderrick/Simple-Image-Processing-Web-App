# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/6
# @Author  : Yingke Ding
# @File    : histogram_equalization.py
# @Software: PyCharm
import cv2
import numpy as np


def get_histogram_equalization_image(img_path):
    img = cv2.imread(img_path)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    pixel_count = [0 for i in range(256)]

    for row_pixels in gray_img:
        for pixel in row_pixels:
            pixel_count[pixel] += 1

    cumulative_histogram = [0 for i in range(256)]
    for i in range(1, 256):
        cumulative_histogram[i] = cumulative_histogram[i - 1] + pixel_count[i]

    lookup_table = [int(element * 255 / (gray_img.shape[0] * gray_img.shape[1])) for element in cumulative_histogram]

    equalized_pixels = []
    for index, row_pixels in enumerate(gray_img):
        equalized_row_pixels = [lookup_table[pixel] for pixel in row_pixels]
        equalized_pixels.append(equalized_row_pixels)

    equalized_img = np.array(equalized_pixels, dtype=np.uint8)

    return equalized_img


if __name__ == '__main__':
    result = get_histogram_equalization_image("./images/IMG_0185.JPG")

    cv2.imshow("Image", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
