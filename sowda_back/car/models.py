from django.db import models
from api.models import Address
from django.conf import settings
from ckeditor.fields import RichTextField
import uuid
import os

class CarCategory(models.Model):
    name = models.CharField(null=True, max_length=100)

    class Meta:
        verbose_name = "Awtoulag kategoriýasy"
        verbose_name_plural = "Awtoulag kategoriýalar"

    def __str__(self):
        return self.name

def image_add_car(instance, filename):
    filename_base, filename_ext = os.path.splitext(filename)
    return f'awtoulaglar/{uuid.uuid4()}_{filename_base}{filename_ext}'

def images_add_car(instance, filename):
    filename_base, filename_ext = os.path.splitext(filename)
    return f'awtoulaglar/{uuid.uuid4()}_{filename_base}{filename_ext}'

class Car(models.Model):
    name = models.CharField(null=True, max_length=100)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(CarCategory, on_delete=models.CASCADE)
    phone = models.CharField(null=True, max_length=20)
    img = models.ImageField(upload_to=image_add_car, null=True)
    text = RichTextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    checked = models.BooleanField(default=False)
    price = models.DecimalField(null=True, max_digits=10, decimal_places=2)

    class Meta:
        ordering = ['-created', 'checked']
        verbose_name = "Awtoulag"
        verbose_name_plural = "Awtoulaglar"

    def __str__(self):
        return self.name or f"Awtoulag #{self.pk}"

class ImageCar(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='Haryt', null=True, related_name='images')
    img = models.ImageField(upload_to=images_add_car, null=True, verbose_name='Surat')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Döredilen wagty', null=True)

    class Meta:
        ordering = ['created']
        verbose_name = "Awtoulag suraty"
        verbose_name_plural = "Awtoulag suratlar"

    def __str__(self):
        return self.img.url if self.img else "Surat ýok"
