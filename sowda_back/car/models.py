from django.db import models
from api.models import Address
from django.conf import settings
from ckeditor.fields import RichTextField

class CarCategory(models.Model):
    name = models.CharField(null=True, max_length=100)

    class Meta:
        verbose_name = ("Awtoulag kategoriýa")
        verbose_name_plural = ("Awtoulag kategoriýalar")

    def __str__(self):
        return self.name

def image_add_car(self,filename):
    return f'awtoulaglar/{self.created}-{self.name}/{filename}'
def images_add_car(self,filename):
    return f'awtoulaglar/{self.created}-{self.car.name}/{filename}'
class Car(models.Model):
    name = models.CharField(null=True, max_length=100)
    address = models.ForeignKey(Address,on_delete=models.CASCADE)
    author = models.CharField(max_length=8,null=True)
    category = models.ForeignKey(CarCategory,on_delete=models.CASCADE)
    phone = models.IntegerField(null=True,)
    img = models.ImageField(upload_to=image_add_car,null=True)
    text = RichTextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    checked = models.BooleanField(default=False)
    price = models.DecimalField(null=True,  max_digits=10,decimal_places=2,)
    
    class Meta:
        ordering= ['-created','checked']
        verbose_name = ("Awotulag")
        verbose_name_plural = ("Awtoulaglar")

    def __str__(self):
        return self.name


class ImageCar(models.Model):
    car = models.ForeignKey(Car,on_delete=models.CASCADE,verbose_name='Haryt',null=True,related_name='images')
    img = models.ImageField(upload_to=images_add_car,null=True,verbose_name='Surat')
    created = models.DateTimeField(auto_now_add=True,verbose_name='Döredilen wagty',null=True)

    class Meta:
        ordering= ['created']
        verbose_name = ("Awtoulag surat")
        verbose_name_plural = ("Awtoulag suratlar")

    def __str__(self):
        return f'{settings.HOSTNAME}{self.img.url}'