from django import forms
from django.db import models

from django_image_cropping.widgets import ImageCroppingInput


class ImageCroppingField(models.ImageField):

    def formfield(self, **kwargs):
        defaults = {
            'form_class': ImageCroppingFormField,
        }
        defaults.update(kwargs)
        return super(ImageCroppingField, self).formfield(**defaults)


class ImageCroppingFormField(forms.ImageField):
    def __init__(self, **kwargs):
        kwargs.update({'widget': ImageCroppingInput()})
        super(ImageCroppingFormField, self).__init__(**kwargs)
