from django.db import models
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

class Logist(models.Model):
    name = models.CharField(null=True, max_length=100)
    category = models.ForeignKey(LogistCategory,on_delete=models.CASCADE)
    author = models.CharField(max_length=255,null=True)
    where = models.CharField(max_length=255,null=True)
    nirden = models.CharField(max_length=255,null=True)
    last_date = models.DateField(null=True)
    bring = models.BooleanField(default=False)
    vip = models.BooleanField(default=False)
    address = models.ForeignKey(Address,on_delete=models.CASCADE)
    phone = models.CharField(null=True, max_length=100)
    img1 = models.ImageField(upload_to=image_add_logist,null=True)
    img2 = models.ImageField(upload_to=image_add_logist,null=True)
    img3 = models.ImageField(upload_to=image_add_logist,null=True)
    img4 = models.ImageField(upload_to=image_add_logist,null=True)
    img5 = models.ImageField(upload_to=image_add_logist,null=True)
    text = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True)
    checked = models.BooleanField(default=False)
    price = models.CharField(null=True, max_length=100)
    
    class Meta:
        verbose_name = ("Logistika")
        verbose_name_plural = ("Logistikalar")

    def __str__(self):
        return self.name