from rest_framework import serializers
from .models import *

class CarouselSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarouselImage
        fields = ('pk', 'name', 'img')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProd
        fields = ('author')

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
class TopProductDetailSerializer(serializers.ModelSerializer):
    address = serializers.CharField(source='address.name')
    class Meta:
        model = TopProducts
        fields = ('pk', 'name', 'address','text','category','phone','price','created','img1','img2','img3','img4','img5','checked')

class TopProductsSerializer(serializers.ModelSerializer):
    address_name = serializers.CharField(source='address.name')
    class Meta:
        model = TopProducts
        fields = ('pk', 'name', 'address_name','text','phone','price','created','img1','checked')

class NewsSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name')
    class Meta:
        model = News
        fields = ('pk', 'name','img', 'author','text','category','created' ,'checked')
