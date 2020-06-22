# -*- coding: utf-8 -*-
# @Time    : 2020/6/9 1:47 下午
# @Author  : Yingke Ding
# @FileName: urls.py
# @Software: PyCharm
from django.urls import path

from . import views

app_name = 'Processing_App'
urlpatterns = [
    path('', views.index, name='index'),
    path('equalized_image', views.equalized_image_index, name='index'),
    path('grayed_image', views.grayed_image_index, name='index'),
]
