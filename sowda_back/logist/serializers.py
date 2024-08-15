from rest_framework import serializers
from .models import *


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageLogist
        fields = ['img']

class LogistCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LogistCategory
        fields = ('pk', 'name')

class LogistDetailSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name')
    address = serializers.CharField(source='address.name')
    images = serializers.StringRelatedField(many=True)

    class Meta:
        model = Logist
        fields = ('pk', 'name', 'address','text','category','last_date','where','nirden','bring','vip','phone','price','url','created','img','checked','images')

class LogistListSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name')
    address_name = serializers.CharField(source='address.name')
    class Meta:
        model = Logist
        fields = ('pk', 'name', 'text','phone','price','created','last_date','where','nirden','bring','vip','img','checked','address_name','category_name')


class LogistSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.id')
    address = serializers.CharField(source='address.id')
    images = serializers.ListField(child=serializers.ImageField(), write_only=True)

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        category_data = validated_data.pop('category')
        category_id = category_data['id']
        address_id = address_data['id']
        images_data = validated_data.pop('images')
        category = LogistCategory.objects.get(id=int(category_id))
        address = Address.objects.get(id=int(address_id))
        logist = Logist.objects.create(category=category,address=address,**validated_data)
        for image in images_data:
            ImageLogist.objects.create(logist=logist, img=image)

        
        return logist

    class Meta:
        model = Logist
        fields = ('pk', 'name', 'author','address','text','phone','last_date','images',
                  'where','nirden','bring','vip','price','url','created','img','checked','category')