from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from api.models import *

class OtherCategory(models.Model):
    name = models.CharField(null=True, max_length=100)

    class Meta:
        verbose_name = ("Beýleki kategoriýa")
        verbose_name_plural = ("Beýleki kategoriýalar")

    def __str__(self):
        return self.name

def image_add_beyleki(self,filename):
    return f'beyleki/{self.created}-{self.name}/{filename}'

def images_add_beyleki(self,filename):
    return f'beyleki/{self.created}-{self.other.name}/{filename}'

class Other(models.Model):
    name = models.CharField(null=True, max_length=100)
    address = models.ForeignKey(Address,on_delete=models.CASCADE)
    category = models.ForeignKey(OtherCategory,on_delete=models.CASCADE)
    author = models.CharField(max_length=8,null=True)
    phone = models.IntegerField(null=True)
    img = models.ImageField(upload_to=image_add_beyleki,null=True)
    text =RichTextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    checked = models.BooleanField(default=False)
    price = models.DecimalField(null=True,  max_digits=10,decimal_places=2,)
    
    class Meta:
        ordering= ['-created','checked']
        verbose_name = ("Beylekiler")
        verbose_name_plural = ("Beylekiler")

    def __str__(self):
        return self.name

class ImageOther(models.Model):
    other = models.ForeignKey(Other,on_delete=models.CASCADE,verbose_name='Haryt',null=True,related_name='images')
    img = models.ImageField(upload_to=images_add_beyleki,null=True,verbose_name='Surat')
    created = models.DateTimeField(auto_now_add=True,verbose_name='Döredilen wagty',null=True)

    class Meta:
        ordering= ['created']
        verbose_name = ("Beyleki surat")
        verbose_name_plural = ("Beyleki suratlar")

    def __str__(self):
        return f'{settings.HOSTNAME}{self.img.url}'