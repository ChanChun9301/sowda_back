from rest_framework import serializers
from .models import *

class CarCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CarCategory
        fields = ('pk', 'name')

class CarDetailSerializer(serializers.ModelSerializer):
    category = serializers.CharField()
    address = serializers.CharField()
    class Meta:
        model = Car
        fields = ('pk', 'name', 'address','text','category','phone','price','created','img1','img2','img3','img4','img5','checked')

class CarListSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name')
    address_name = serializers.CharField(source='address.name')
    class Meta:
        model = Car
        fields = ('pk', 'name', 'text','phone','price','created','img1','checked','address_name','category_name')

class CarSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.id')
    address = serializers.CharField(source='address.id')
    def create(self, validated_data):
        address_data = validated_data.pop('address')
        category_data = validated_data.pop('category')

        category_id = category_data['id']
        address_id = address_data['id']
        category = CarCategory.objects.get(id=int(category_id))
        address = Address.objects.get(id=int(address_id))
        car = Car.objects.create(category=category,address=address,**validated_data)

        return car
        
    class Meta:
        model = Car
        fields = ('pk', 'name', 'address','author','text','phone','price','created','img1','img2','img3','img4','img5','category')