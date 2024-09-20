from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from api.models import Address

class LogistCategory(models.Model):
    name = models.CharField(null=True, max_length=100)

    class Meta:
        verbose_name = ("Logistika kategoriýa")
        verbose_name_plural = ("Logistika kategoriýalar")

    def __str__(self):
        return self.name

def image_add_logist(self,filename):
    return f'logistika/{self.created}-{self.name}/{filename}'

def images_add_logist(self,filename):
    return f'logistika/{self.created}-{self.logist.name}/{filename}'

class Logist(models.Model):
    name = models.CharField(null=True, max_length=100)
    category = models.ForeignKey(LogistCategory,on_delete=models.CASCADE)
    author = models.CharField(max_length=8,null=True)
    where = models.CharField(max_length=20,null=True)
    nirden = models.CharField(max_length=20,null=True)
    last_date = models.DateField(null=True)
    bring = models.BooleanField(default=False)
    vip = models.BooleanField(default=False)
    address = models.ForeignKey(Address,on_delete=models.CASCADE)
    phone = models.IntegerField(null=True)
    img = models.ImageField(upload_to=image_add_logist,null=True)
    text = RichTextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    checked = models.BooleanField(default=False)
    price = models.DecimalField(null=True,  max_digits=10,decimal_places=2,)
    
    class Meta:
        ordering= ['checked','-created',]
        verbose_name = ("Logistika")
        verbose_name_plural = ("Logistikalar")

    def __str__(self):
        return self.name

class ImageLogist(models.Model):
    logist = models.ForeignKey(Logist,on_delete=models.CASCADE,verbose_name='Haryt',null=True,related_name='images')
    img = models.ImageField(upload_to=images_add_logist,null=True,verbose_name='Surat')
    created = models.DateTimeField(auto_now_add=True,verbose_name='Döredilen wagty',null=True)

    class Meta:
        ordering= ['-created']
        verbose_name = ("Logistika surat")
        verbose_name_plural = ("Logistika suratlar")

    def __str__(self):
        return f'{settings.HOSTNAME}{self.img.url}'
