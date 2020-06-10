# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/6
# @Author  : Yingke Ding
# @File    : laplacian_derivative.py
# @Software: PyCharm
import cv2


def get_laplacian_image(img_path):
    img = cv2.imread(img_path)

    laplacian = cv2.Laplacian(img, cv2.CV_64F)  # TODO needs to be modified

    return laplacian


if __name__ == '__main__':
    result = get_laplacian_image("./images/IMG_0185.JPG")

    cv2.imshow("Image", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
