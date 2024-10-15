from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _


class UserProd(models.Model):
    author = models.CharField(max_length=255,null=True)
    checked = models.BooleanField(default=False,verbose_name='Barlandy')
    
    class Meta:
        verbose_name = ("Ulanyjy")
        verbose_name_plural = ("Ulanyjylar")


class CarouselImage(models.Model):
    name = models.CharField(max_length=150,verbose_name='Ady')
    img = models.ImageField(upload_to='carousel',null=True,verbose_name='Surat')

    class Meta:
        verbose_name = ("Banner surat")
        verbose_name_plural = ("Banner suratlar")

    def __str__(self):
        return self.name

class Address(models.Model):
    name = models.CharField(null=True, max_length=100,verbose_name='Salgy')

    def __str__(self):
        return self.name

def images_add_top(self,filename):
    return f'top_product/{self.created}-{self.top.name}/{filename}'

def image_add_top(self,filename):
    return f'top_product/{self.created}-{self.name}/{filename}'
class TopProducts(models.Model):
    name = models.CharField(null=True, max_length=100,verbose_name='Ady')
    category = models.CharField(null=True, max_length=100,verbose_name='Kategoriýa')
    author = models.CharField(max_length=255,null=True,verbose_name='Awtor')
    price = models.DecimalField(null=True, max_digits=10,decimal_places=2,verbose_name='Bahasy')
    address = models.ForeignKey(Address,on_delete=models.CASCADE,verbose_name='Salgy')
    text = RichTextField(null=True)
    phone = models.IntegerField(null=True, verbose_name='Telefon belgi')
    img = models.ImageField(upload_to=image_add_top,verbose_name='Surat',null=True,)
    created = models.DateTimeField(auto_now_add=True,verbose_name='Döredilen wagty')
    checked = models.BooleanField(default=False,verbose_name='Barlandy')
    
    class Meta:
        ordering= ['-created','checked']
        verbose_name = ("Saýlanan")
        verbose_name_plural = ("Saýlananlar")

    def __str__(self):
        return self.name

class ImageTop(models.Model):
    top = models.ForeignKey(TopProducts,on_delete=models.CASCADE,verbose_name='Haryt',null=True,related_name='images')
    img = models.ImageField(upload_to=images_add_top,null=True,verbose_name='Surat')
    created = models.DateTimeField(auto_now_add=True,verbose_name='Döredilen wagty',null=True)

    class Meta:
        verbose_name = ("Saýlanan surat")
        verbose_name_plural = ("Saýlanan suratlar")

    def __str__(self):
        return f'{settings.HOSTNAME}{self.img.url}'
    
class NewsCategory(models.Model):
    name = models.CharField(null=True, max_length=100,verbose_name='Habar kategoriýa')

    class Meta:
        verbose_name = ("Habar kategoriýa")
        verbose_name_plural = ("Habar kategoriýalar")

    def __str__(self):
        return self.name

def image_add_habar(self,filename):
    return f'habarlar/{self.created}-{self.name[:50]}/{filename}'

class News(models.Model):
    name = models.CharField(null=True, max_length=500,verbose_name='Ady')
    author = models.CharField(max_length=150,null=True,verbose_name='Awtor')
    category = models.ForeignKey(NewsCategory,on_delete=models.CASCADE,verbose_name='Kategoriýa')
    img = models.ImageField(upload_to=image_add_habar,null=True,verbose_name='Surat')
    text = RichTextField(null=True)
    created = models.DateTimeField(auto_now_add=True,verbose_name='Döredilen wagty')
    checked = models.BooleanField(default=False,verbose_name='Barlandy')
    
    class Meta:
        # app_label = 'Habarlar'
        ordering= ['-created','checked']
        verbose_name = ("Habar")
        verbose_name_plural = ("Habarlar")

    def __str__(self):
        return self.name