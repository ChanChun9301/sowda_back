from django.db import models
from api.models import Address

class CarCategory(models.Model):
    name = models.CharField(null=True, max_length=100)

    class Meta:
        verbose_name = ("Awtoulag kategoriýa")
        verbose_name_plural = ("Awtoulag kategoriýalar")

    def __str__(self):
        return self.name

def image_add_car(self,filename):
    return f'awtoulaglar/{self.created}-{self.name}/{filename}'

class Car(models.Model):
    name = models.CharField(null=True, max_length=100)
    address = models.ForeignKey(Address,on_delete=models.CASCADE)
    author = models.CharField(max_length=8,null=True)
    category = models.ForeignKey(CarCategory,on_delete=models.CASCADE)
    phone = models.CharField(null=True, max_length=8)
    img1 = models.ImageField(upload_to=image_add_car,null=True)
    img2 = models.ImageField(upload_to=image_add_car,null=True)
    img3 = models.ImageField(upload_to=image_add_car,null=True)
    img4 = models.ImageField(upload_to=image_add_car,null=True)
    img5 = models.ImageField(upload_to=image_add_car,null=True)
    text = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True)
    checked = models.BooleanField(default=False)
    price = models.CharField(null=True, max_length=100)
    
    class Meta:
        verbose_name = ("Awotulag")
        verbose_name_plural = ("Awtoulaglar")

    def __str__(self):
        return self.name