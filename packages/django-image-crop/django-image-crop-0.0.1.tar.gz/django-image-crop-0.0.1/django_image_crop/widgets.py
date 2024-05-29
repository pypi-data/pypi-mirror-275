# -*- coding: UTF-8 -*-
"""
@Project  : admin_ckeditor
@File     : widgets.py
@IDE      : PyCharm
@Author   : Tan Jianbin
@Email    : bj.t@foxmail.com
@Date     : 2024/5/23 8:56
@Function :
"""
from django.template import loader
from django.forms import ClearableFileInput
from django.utils.safestring import mark_safe


class ImageCroppingInput(ClearableFileInput):
    template_name = "image_cropping.html"

    class Media:
        css = {
            "all": [
                "css/bootstrap.min.css",
                "css/cropper.min.css",
                "css/image_cropping.css",
            ]
        }

        js = [
            "js/bootstrap.min.js",
            "js/cropper.min.js",
            "js/jquery-3.7.1.min.js",
        ]

    def render(self, name, value, attrs=None, renderer=None):
        context = self.get_context(name, value, attrs)
        template = loader.get_template(self.template_name).render(context)
        return mark_safe(template)
