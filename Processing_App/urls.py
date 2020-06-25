# -*- coding: utf-8 -*-
# @Time    : 2020/6/9 1:47 下午
# @Author  : Yingke Ding
# @FileName: urls.py
# @Software: PyCharm
from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'Processing_App'
urlpatterns = [
    path('', views.index, name='index'),
    path('equalized_image', views.equalized_image_index, name='index'),
    path('grayed_image', views.grayed_image_index, name='index'),
    path('laplacian_image', views.laplacian_image_index, name='index'),
    path('smoothed_image', views.smoothed_image_index, name='index'),

    # For resize function, only allow 0.01-0.99 (1 or 2 digit)
    url(r'^(?P<resize_input>\d+\.\d)/resized_image$', views.resized_image_index),
    url(r'^(?P<resize_input>\d+\.\d{2})/resized_image$', views.resized_image_index),

    # Matches url for image rotation function.
    # url(r'(?P<last_image_name>[\w\-]+)/(?P<last_image_type>\.[\w\-]+)/left90([^/]*)$', views.rotate90_image_index),
    url(r'(?P<last_image_name>[\w\-]+)/(?P<last_image_type>\.[\w\-]+)/(?P<rotate_type>[\w\-]+)([^/]*)$',
        views.rotate90_image_index),
]
