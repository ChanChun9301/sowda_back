from rest_framework import serializers
from .models import *

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageService
        fields = ['img']

class ServiceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = ('pk', 'name')

class ServiceDetailSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name')
    address_name = serializers.CharField(source='address.name')
    images = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = Service
        fields = ('pk', 'name', 'address_name','text','category_name','phone','price','created','img','images','checked')

class ServiceSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.id')
    address = serializers.CharField(source='address.id')
    images = serializers.ListField(child=serializers.ImageField(), write_only=True)

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        category_data = validated_data.pop('category')
        images_data = validated_data.pop('images')
        category_id = category_data['id']
        address_id = address_data['id']
        category = ServiceCategory.objects.get(id=int(category_id))
        address = Address.objects.get(id=int(address_id))
        service = Service.objects.create(category=category,address=address,**validated_data)
        for image in images_data:
            ImageService.objects.create(service=service, img=image)
        return service

    class Meta:
        model = Service
        fields = ('pk', 'name', 'address','author','text','phone','price','created','img','checked','category','images')
