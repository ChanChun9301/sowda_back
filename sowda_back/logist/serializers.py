from rest_framework import serializers
from .models import *


class LogistCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LogistCategory
        fields = ('pk', 'name')

class LogistDetailSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name')
    address = serializers.CharField(source='address.name')
    class Meta:
        model = Logist
        fields = ('pk', 'name', 'address','text','category','last_date','where','nirden','bring','vip','phone','price','url','created','img1','img2','img3','img4','img5','checked')

class LogistListSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name')
    address_name = serializers.CharField(source='address.name')
    class Meta:
        model = Logist
        fields = ('pk', 'name', 'text','phone','price','created','last_date','where','nirden','bring','vip','img1','checked','address_name','category_name')


class LogistSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.id')
    address = serializers.CharField(source='address.id')
    def create(self, validated_data):
        address_data = validated_data.pop('address')
        category_data = validated_data.pop('category')
        category_id = category_data['id']
        address_id = address_data['id']
        category = LogistCategory.objects.get(id=int(category_id))
        address = Address.objects.get(id=int(address_id))
        logist = Logist.objects.create(category=category,address=address,**validated_data)
        
        return logist

    class Meta:
        model = Logist
        fields = ('pk', 'name', 'address','text','phone','last_date','where','nirden','bring','vip','price','url','created','img1','img2','img3','img4','img5','checked','category')