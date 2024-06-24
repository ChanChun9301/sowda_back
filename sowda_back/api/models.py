from django.db import models
from django.contrib.auth.models import AbstractUser
from tinymce.models import HTMLField

# class phoneModel(models.Model):
#     Mobile = models.IntegerField(blank=False)
#     isVerified = models.BooleanField(blank=False, default=False)
#     counter = models.IntegerField(default=0, blank=False)   # For HOTP Verification

#     def __str__(self):
#         return str(self.Mobile)

class UserProd(AbstractUser):
    author = models.CharField(max_length=23,null=True)
    

    class Meta:
        verbose_name = ("Ulanyjy")
        verbose_name_plural = ("Ulanyjylar")

    # def __str__(self):
    #     return self.author

class CarouselImage(models.Model):
    name = models.CharField(max_length=150)
    img = models.ImageField(upload_to='carousel',null=True)

    def __str__(self):
        return self.name

class Address(models.Model):
    name = models.CharField(null=True, max_length=100)
    def __str__(self):
        return self.name

class LogistCategory(models.Model):
    name = models.CharField(null=True, max_length=100)

    class Meta:
        verbose_name = ("Logistika kategoriýa")
        verbose_name_plural = ("Logistika kategoriýalar")

    def __str__(self):
        return self.name

def image_add(self):
    return f'gosulan_bildiris/{self}'

class AddedModel(models.Model):
    name = models.CharField(null=True, max_length=100)
    author = models.CharField(max_length=255,null=True)
    category = models.ForeignKey(LogistCategory,on_delete=models.CASCADE)
    address = models.ForeignKey(Address,on_delete=models.CASCADE)
    phone = models.CharField(null=True, max_length=100)
    img1 = models.ImageField(upload_to=image_add,null=True)
    img2 = models.ImageField(upload_to=image_add,null=True)
    img3 = models.ImageField(upload_to=image_add,null=True)
    img4 = models.ImageField(upload_to=image_add,null=True)
    img5 = models.ImageField(upload_to=image_add,null=True)
    text = models.TextField(blank=True)
    text = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True)
    checked = models.BooleanField(default=False)
    price = models.CharField(null=True, max_length=100)
    

    class Meta:
        verbose_name = ("Gosulan")
        verbose_name_plural = ("Gosulanlar")

    def __str__(self):
        return self.name


class TopProducts(models.Model):
    name = models.CharField(null=True, max_length=100)
    category = models.CharField(null=True, max_length=100)
    author = models.CharField(max_length=255,null=True)
    address = models.ForeignKey(Address,on_delete=models.CASCADE)
    phone = models.CharField(null=True, max_length=100)
    img1 = models.ImageField(upload_to='saýlanan',null=True,default='/static/')
    img2 = models.ImageField(upload_to='saýlanan',null=True)
    img3 = models.ImageField(upload_to='saýlanan',null=True)
    img4 = models.ImageField(upload_to='saýlanan',null=True)
    img5 = models.ImageField(upload_to='saýlanan',null=True)
    text = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True)
    checked = models.BooleanField(default=False)
    price = models.CharField(null=True, max_length=100)
    

    class Meta:
        verbose_name = ("Saýlanan")
        verbose_name_plural = ("Saýlananlar")

    def __str__(self):
        return self.name

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
    img1 = models.ImageField(upload_to='logistika',null=True)
    img2 = models.ImageField(upload_to='logistika',null=True)
    img3 = models.ImageField(upload_to='logistika',null=True)
    img4 = models.ImageField(upload_to='logistika',null=True)
    img5 = models.ImageField(upload_to='logistika',null=True)
    text = HTMLField()
    created = models.DateField(auto_now_add=True)
    checked = models.BooleanField(default=False)
    price = models.CharField(null=True, max_length=100)
    

    class Meta:
        verbose_name = ("Logistika")
        verbose_name_plural = ("Logistikalar")

    def __str__(self):
        return self.name



class ElinCategory(models.Model):
    name = models.CharField(null=True, max_length=100)

    class Meta:
        verbose_name = ("Elin kategoriýa")
        verbose_name_plural = ("Elin kategoriýalar")
        
    def __str__(self):
        return self.name

def image_add(self):
    return f'gosulan_bildiris/{self}'


class Elin(models.Model):
    name = models.CharField(null=True, max_length=100)
    address = models.ForeignKey(Address,on_delete=models.CASCADE)
    category = models.ForeignKey(ElinCategory,on_delete=models.CASCADE)
    author = models.CharField(max_length=255,null=True)
    phone = models.CharField(null=True, max_length=100)
    img1 = models.ImageField(upload_to='elin',null=True)
    img2 = models.ImageField(upload_to='elin',null=True)
    img3 = models.ImageField(upload_to='elin',null=True)
    img4 = models.ImageField(upload_to='elin',null=True)
    img5 = models.ImageField(upload_to='elin',null=True)
    text = HTMLField()
    created = models.DateField(auto_now_add=True)
    checked = models.BooleanField(default=False)
    price = models.CharField(null=True, max_length=100)
    

    class Meta:
        verbose_name = ("Elin")
        verbose_name_plural = ("Elin")

    def __str__(self):
        return self.name

class OtherCategory(models.Model):
    name = models.CharField(null=True, max_length=100)

    class Meta:
        verbose_name = ("Beýleki kategoriýa")
        verbose_name_plural = ("Beýleki kategoriýalar")

    def __str__(self):
        return self.name

class Other(models.Model):
    name = models.CharField(null=True, max_length=100)
    address = models.ForeignKey(Address,on_delete=models.CASCADE)
    category = models.ForeignKey(OtherCategory,on_delete=models.CASCADE)
    author = models.CharField(max_length=255,null=True)
    phone = models.CharField(null=True, max_length=100)
    img1 = models.ImageField(upload_to='beylekiler',null=True)
    img2 = models.ImageField(upload_to='beylekiler',null=True)
    img3 = models.ImageField(upload_to='beylekiler',null=True)
    img4 = models.ImageField(upload_to='beylekiler',null=True)
    img5 = models.ImageField(upload_to='beylekiler',null=True)
    text = HTMLField()
    created = models.DateField(auto_now_add=True)
    checked = models.BooleanField(default=False)
    price = models.CharField(null=True, max_length=100)
    

    class Meta:
        verbose_name = ("Beylekiler")
        verbose_name_plural = ("Beylekiler")

    def __str__(self):
        return self.name

class ServiceCategory(models.Model):
    name = models.CharField(null=True, max_length=100)

    class Meta:
        verbose_name = ("Hyzmat kategoriýa")
        verbose_name_plural = ("Hyzmat kategoriýalar")

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(null=True, max_length=100)
    address = models.ForeignKey(Address,on_delete=models.CASCADE)
    category = models.ForeignKey(ServiceCategory,on_delete=models.CASCADE)
    author = models.CharField(max_length=255,null=True)
    phone = models.CharField(null=True, max_length=100)
    img1 = models.ImageField(upload_to='hyzmatlar',null=True)
    img2 = models.ImageField(upload_to='hyzmatlar',null=True)
    img3 = models.ImageField(upload_to='hyzmatlar',null=True)
    img4 = models.ImageField(upload_to='hyzmatlar',null=True)
    img5 = models.ImageField(upload_to='hyzmatlar',null=True)
    text = HTMLField()
    created = models.DateField(auto_now_add=True)
    checked = models.BooleanField(default=False)
    price = models.CharField(null=True, max_length=100)
    

    class Meta:
        verbose_name = ("Hyzmatlar")
        verbose_name_plural = ("Hyzmatlar")

    def __str__(self):
        return self.name




class CarCategory(models.Model):
    name = models.CharField(null=True, max_length=100)

    class Meta:
        verbose_name = ("Awtoulag kategoriýa")
        verbose_name_plural = ("Awtoulag kategoriýalar")

    def __str__(self):
        return self.name

class Car(models.Model):
    name = models.CharField(null=True, max_length=100)
    address = models.ForeignKey(Address,on_delete=models.CASCADE)
    author = models.CharField(max_length=255,null=True)
    category = models.ForeignKey(CarCategory,on_delete=models.CASCADE)
    phone = models.CharField(null=True, max_length=100)
    img1 = models.ImageField(upload_to='ulaglar',null=True)
    img2 = models.ImageField(upload_to='ulaglar',null=True)
    img3 = models.ImageField(upload_to='ulaglar',null=True)
    img4 = models.ImageField(upload_to='ulaglar',null=True)
    img5 = models.ImageField(upload_to='ulaglar',null=True)
    text = HTMLField()
    created = models.DateField(auto_now_add=True)
    checked = models.BooleanField(default=False)
    price = models.CharField(null=True, max_length=100)
    

    class Meta:
        verbose_name = ("Ulag")
        verbose_name_plural = ("Ulaglar")

    def __str__(self):
        return self.name




class NewsCategory(models.Model):
    name = models.CharField(null=True, max_length=100)

    class Meta:
        verbose_name = ("Habar kategoriýa")
        verbose_name_plural = ("Habar kategoriýalar")

    def __str__(self):
        return self.name

class News(models.Model):
    name = models.CharField(null=True, max_length=100)
    author = models.CharField(max_length=150,null=True)
    category = models.ForeignKey(NewsCategory,on_delete=models.CASCADE)
    img = models.ImageField(upload_to='habarlar',null=True)
    text = HTMLField()
    created = models.DateField(auto_now_add=True)
    checked = models.BooleanField(default=False)
    

    class Meta:
        verbose_name = ("Habar")
        verbose_name_plural = ("Habarlar")

    def __str__(self):
        return self.name

