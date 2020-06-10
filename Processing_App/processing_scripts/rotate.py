# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/6
# @Author  : Yingke Ding
# @File    : rotate.py
# @Software: PyCharm
import cv2
import numpy as np


def rotate(image_path, k=1, axes=(0, 1)):
    # TODO need to be modified
    """
    :param image_path:
    :param k: Number of times the array is rotated by 90 degrees.
    :param axes: The array is rotated in the plane defined by the axes.
    :return:
    """
    raw_img = cv2.imread(image_path)

    axes = tuple(axes)
    if len(axes) != 2:
        raise ValueError("len(axes) must be 2.")

    if axes[0] == axes[1] or np.abs(axes[0] - axes[1]) == raw_img.ndim:
        raise ValueError("Axes must be different.")

    if (axes[0] >= raw_img.ndim or axes[0] < -raw_img.ndim
            or axes[1] >= raw_img.ndim or axes[1] < -raw_img.ndim):
        raise ValueError("Axes={} out of range for array of ndim={}."
                         .format(axes, raw_img.ndim))

    k %= 4

    if k == 0:
        return raw_img[:]
    if k == 2:
        return np.flip(np.flip(raw_img, axes[0]), axes[1])

    axes_list = np.arange(0, raw_img.ndim)
    (axes_list[axes[0]], axes_list[axes[1]]) = (axes_list[axes[1]],
                                                axes_list[axes[0]])

    if k == 1:
        return np.transpose(np.flip(raw_img, axes[1]), axes_list)
    else:
        # k == 3
        return np.flip(np.transpose(raw_img, axes_list), axes[1])


if __name__ == '__main__':
    path = "./images/IMG_0185.JPG"
    result = rotate(path, k=2)
    cv2.imshow("Image", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
