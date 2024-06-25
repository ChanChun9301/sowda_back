from django.db import models
from tinymce.models import HTMLField
from api.models import *

class ElinCategory(models.Model):
    name = models.CharField(null=True, max_length=100)

    class Meta:
        verbose_name = ("Elin kategoriýa")
        verbose_name_plural = ("Elin kategoriýalar")
        
    def __str__(self):
        return self.name

def image_add_elin(self,filename):
    return f'elin/{self.name}/{filename}'

class Elin(models.Model):
    name = models.CharField(null=True, max_length=100)
    address = models.ForeignKey(Address,on_delete=models.CASCADE)
    category = models.ForeignKey(ElinCategory,on_delete=models.CASCADE)
    author = models.CharField(max_length=255,null=True)
    phone = models.CharField(null=True, max_length=100)
    img1 = models.ImageField(upload_to=image_add_elin,null=True)
    img2 = models.ImageField(upload_to=image_add_elin,null=True)
    img3 = models.ImageField(upload_to=image_add_elin,null=True)
    img4 = models.ImageField(upload_to=image_add_elin,null=True)
    img5 = models.ImageField(upload_to=image_add_elin,null=True)
    text = HTMLField()
    created = models.DateField(auto_now_add=True)
    checked = models.BooleanField(default=False)
    price = models.CharField(null=True, max_length=100)
    
    class Meta:
        verbose_name = ("Elin")
        verbose_name_plural = ("Elin")

    def __str__(self):
        return self.name
