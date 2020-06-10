# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/6
# @Author  : Yingke Ding
# @File    : resize.py
# @Software: PyCharm
import cv2


def resize(image_path, scale_percent=50):
    img = cv2.imread(image_path)

    # calculate the 50 percent of original dimensions
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)

    dsize = (width, height)

    return cv2.resize(img, dsize)


if __name__ == '__main__':
    result = resize("./images/IMG_0185.JPG", scale_percent=20)
    cv2.imshow("Image", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
