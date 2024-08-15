from django.db import models
from api.models import Address
from django.conf import settings

class ServiceCategory(models.Model):
    name = models.CharField(null=True, max_length=100)

    class Meta:
        verbose_name = ("Hyzmat kategoriýa")
        verbose_name_plural = ("Hyzmat kategoriýalar")

    def __str__(self):
        return self.name

def image_add_hyzmat(self,filename):
    return f'hyzmatlar/{self.created}-{self.name}/{filename}'

class Service(models.Model):
    name = models.CharField(null=True, max_length=100)
    address = models.ForeignKey(Address,on_delete=models.CASCADE)
    category = models.ForeignKey(ServiceCategory,on_delete=models.CASCADE)
    author = models.CharField(max_length=8,null=True)
    phone = models.IntegerField(null=True)
    img = models.ImageField(upload_to=image_add_hyzmat,null=True)
    text = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True)
    checked = models.BooleanField(default=False)
    price = models.DecimalField(null=True,  max_digits=10,decimal_places=2,)
    
    class Meta:
        ordering= ['-created','checked']
        verbose_name = ("Hyzmatlar")
        verbose_name_plural = ("Hyzmatlar")

    def __str__(self):
        return self.name

class ImageService(models.Model):
    service = models.ForeignKey(Service,on_delete=models.CASCADE,verbose_name='Haryt',null=True,related_name='images')
    img = models.ImageField(upload_to=image_add_hyzmat,null=True,verbose_name='Surat')
    created = models.DateField(auto_now_add=True,verbose_name='Döredilen wagty',null=True)

    class Meta:
        ordering= ['created']
        verbose_name = ("Hyzmat surat")
        verbose_name_plural = ("Hyzmat suratlar")

    def __str__(self):
        return f'{settings.HOSTNAME}{self.img.url}'