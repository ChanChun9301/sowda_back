from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework import serializers
from .models import *
from .functions import user_created


class CarouselSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarouselImage
        fields = ('pk', 'name', 'img')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProd
        fields = ('pk','author','checked',)


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProd
        fields = ('author','username','password')

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('pk','url', 'name')

class NewsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsCategory
        fields = ('pk', 'name')


#/////////////////////////////////////////////////////////////////////////
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageTop
        fields = ['img__url']
        
class TopProductsSerializer(serializers.ModelSerializer):
    address_name = serializers.CharField(source='address.name')

    class Meta:
        model = TopProducts
        fields = ('pk', 'name', 'address_name','text','phone','price','created','img','checked')

class TopProductDetailSerializer(serializers.ModelSerializer):
    images = serializers.StringRelatedField(many=True)
    address = serializers.CharField(source='address.name')
    class Meta:
        model = TopProducts
        fields = ['pk', 'name', 'address','text','category','phone','price','created','img','checked','images']




class NewsSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name')
    class Meta:
        model = News
        fields = ('pk', 'name','img', 'author','text','category','created' ,'checked')
