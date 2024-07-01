from django.db import models
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

class Other(models.Model):
    name = models.CharField(null=True, max_length=100)
    address = models.ForeignKey(Address,on_delete=models.CASCADE)
    category = models.ForeignKey(OtherCategory,on_delete=models.CASCADE)
    author = models.CharField(max_length=255,null=True)
    phone = models.CharField(null=True, max_length=100)
    img1 = models.ImageField(upload_to=image_add_beyleki,null=True)
    img2 = models.ImageField(upload_to=image_add_beyleki,null=True)
    img3 = models.ImageField(upload_to=image_add_beyleki,null=True)
    img4 = models.ImageField(upload_to=image_add_beyleki,null=True)
    img5 = models.ImageField(upload_to=image_add_beyleki,null=True)
    text =models.TextField(blank=True)
    created = models.DateField(auto_now_add=True)
    checked = models.BooleanField(default=False)
    price = models.CharField(null=True, max_length=100)
    
    class Meta:
        verbose_name = ("Beylekiler")
        verbose_name_plural = ("Beylekiler")

    def __str__(self):
        return self.name