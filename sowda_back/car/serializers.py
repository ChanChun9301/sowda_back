from rest_framework import serializers
from .models import *

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageCar
        fields = ['img']

class CarCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CarCategory
        fields = ('pk', 'name')

class CarDetailSerializer(serializers.ModelSerializer):
    category = serializers.CharField()
    address = serializers.CharField()
    images = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = Car
        fields = ('pk', 'name', 'address','text','category','phone','price','created','img','images')

class CarListSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name')
    address_name = serializers.CharField(source='address.name')
    class Meta:
        model = Car
        fields = ('pk', 'name', 'text','phone','price','created','img','checked','address_name','category_name')

class CarSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.id')
    address = serializers.CharField(source='address.id')
    images = serializers.ListField(child=serializers.ImageField(), write_only=True)
    def create(self, validated_data):
        address_data = validated_data.pop('address')
        category_data = validated_data.pop('category')
        images_data = validated_data.pop('images')
        category_id = category_data['id']
        address_id = address_data['id']
        category = CarCategory.objects.get(id=int(category_id))
        address = Address.objects.get(id=int(address_id))
        car = Car.objects.create(category=category,address=address,**validated_data)
        for image in images_data:
            ImageCar.objects.create(car=car, img=image)


        return car
        
    class Meta:
        model = Car
        fields = ('pk', 'name', 'address','author','text','phone','price','created','img','category','images')