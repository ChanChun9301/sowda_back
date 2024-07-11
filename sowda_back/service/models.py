from django.db import models
from api.models import Address

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
    phone = models.CharField(null=True, max_length=8)
    img1 = models.ImageField(upload_to=image_add_hyzmat,null=True)
    img2 = models.ImageField(upload_to=image_add_hyzmat,null=True)
    img3 = models.ImageField(upload_to=image_add_hyzmat,null=True)
    img4 = models.ImageField(upload_to=image_add_hyzmat,null=True)
    img5 = models.ImageField(upload_to=image_add_hyzmat,null=True)
    text = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True)
    checked = models.BooleanField(default=False)
    price = models.CharField(null=True, max_length=100)
    
    class Meta:
        verbose_name = ("Hyzmatlar")
        verbose_name_plural = ("Hyzmatlar")

    def __str__(self):
        return self.name