from django.db import models
from django.contrib.auth.models import AbstractUser
from tinymce.models import HTMLField

class UserProd(AbstractUser):
    author = models.CharField(max_length=23,null=True)
    
    class Meta:
        verbose_name = ("Ulanyjy")
        verbose_name_plural = ("Ulanyjylar")

class CarouselImage(models.Model):
    name = models.CharField(max_length=150)
    img = models.ImageField(upload_to='carousel',null=True)

    def __str__(self):
        return self.name

class Address(models.Model):
    name = models.CharField(null=True, max_length=100)
    def __str__(self):
        return self.name

def image_add_top(self,filename):
    return f'top_product/{self.name}/{filename}'

class TopProducts(models.Model):
    name = models.CharField(null=True, max_length=100)
    category = models.CharField(null=True, max_length=100)
    author = models.CharField(max_length=255,null=True)
    address = models.ForeignKey(Address,on_delete=models.CASCADE)
    phone = models.CharField(null=True, max_length=100)
    img1 = models.ImageField(upload_to=image_add_top,null=True,default='/static/')
    img2 = models.ImageField(upload_to=image_add_top,null=True)
    img3 = models.ImageField(upload_to=image_add_top,null=True)
    img4 = models.ImageField(upload_to=image_add_top,null=True)
    img5 = models.ImageField(upload_to=image_add_top,null=True)
    text = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True)
    checked = models.BooleanField(default=False)
    price = models.CharField(null=True, max_length=100)
    
    class Meta:
        verbose_name = ("Saýlanan")
        verbose_name_plural = ("Saýlananlar")

    def __str__(self):
        return self.name

class NewsCategory(models.Model):
    name = models.CharField(null=True, max_length=100)

    class Meta:
        verbose_name = ("Habar kategoriýa")
        verbose_name_plural = ("Habar kategoriýalar")

    def __str__(self):
        return self.name

def image_add_habar(self,filename):
    return f'habarlar/{self.name}/{filename}'

class News(models.Model):
    name = models.CharField(null=True, max_length=100)
    author = models.CharField(max_length=150,null=True)
    category = models.ForeignKey(NewsCategory,on_delete=models.CASCADE)
    img = models.ImageField(upload_to=image_add_habar,null=True)
    text = HTMLField()
    created = models.DateField(auto_now_add=True)
    checked = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = ("Habar")
        verbose_name_plural = ("Habarlar")

    def __str__(self):
        return self.name