# -*- coding: utf-8 -*-
# @Time    : 2020/6/8 4:20 下午
# @Author  : Yingke Ding
# @FileName: forms.py
# @Software: PyCharm
from django import forms
from .models import UserUploadPhoto


class ImageForm(forms.ModelForm):
    class Meta:
        model = UserUploadPhoto
        fields = ['image']
