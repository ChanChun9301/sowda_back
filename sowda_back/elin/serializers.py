from django.conf import settings
import os
from rest_framework import serializers
from .models import *

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageElin
        fields = ['img']

class ElinCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ElinCategory
        fields = ('pk', 'name')

class ElinDetailSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name')
    address_name = serializers.CharField(source='address.name')
    images = serializers.StringRelatedField(many=True)

    
    class Meta:
        model = Elin
        fields = ('pk', 'name', 'address_name','text','category_name','phone','price','created','img','images','checked')

class ElinListSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name')
    address_name = serializers.CharField(source='address.name')

    class Meta:
        model = Elin
        fields = ('pk', 'name','text','phone','price','created','img','checked','author','category_name','address_name')

class ElinSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.id')
    address = serializers.CharField(source='address.id')
    images = serializers.ListField(child=serializers.ImageField(), write_only=True)

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        category_data = validated_data.pop('category')
        images_data = validated_data.pop('images')
        category = ElinCategory.objects.get(id=int(category_data['id']))
        address = Address.objects.get(id=int( address_data['id']))
        elin = Elin.objects.create(category=category,address=address,**validated_data)
        
        for image in images_data:
            ImageElin.objects.create(elin=elin, img=image)


        return elin

    class Meta:
        model = Elin
        fields = ('pk', 'name', 'address','text','phone','price','created','img','checked','category','author','images')