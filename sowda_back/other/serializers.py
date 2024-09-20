from rest_framework import serializers
from django.conf import settings
import os
from .models import *

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageOther
        fields = ['img']

class OtherCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherCategory
        fields = ('pk', 'name')

class OtherDetailSerializer(serializers.ModelSerializer):
    category = serializers.CharField()
    address = serializers.CharField()
    images = serializers.StringRelatedField(many=True)

    class Meta:
        model = Other
        fields = ('pk', 'name', 'address','text','category','phone','price','created','img','images','checked')

class OtherListSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name')
    address_name = serializers.CharField(source='address.name')
    class Meta:
        model = Other
        fields = ('pk', 'name', 'text','phone','price','created','img','checked','address_name','category_name')

class OtherSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.id')
    address = serializers.CharField(source='address.id')
    images = serializers.ListField(child=serializers.ImageField(), write_only=True)

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        category_data = validated_data.pop('category')
        images_data = validated_data.pop('images')
        category = OtherCategory.objects.get(id=int(category_data['id']))
        address = Address.objects.get(id=int( address_data['id']))
        other = Other.objects.create(category=category,address=address,**validated_data)
        for image in images_data:
            ImageOther.objects.create(other=other, img=image)
        
        return other

    class Meta:
        model = Other
        fields = ('pk', 'name', 'address','text','phone','price','created','img','checked','category','author','images')