from rest_framework import serializers
from .models import *

class ElinCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ElinCategory
        fields = ('pk', 'name')

class ElinDetailSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name')
    address_name = serializers.CharField(source='address.name')
    class Meta:
        model = Elin
        fields = ('pk', 'name', 'address_name','text','category_name','phone','price','created','img1','img2','img3','img4','img5','checked')

class ElinSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.id')
    address = serializers.CharField(source='address.id')

    def create(self, validated_data):
        print(validated_data)
        address_data = validated_data.pop('address')
        category_data = validated_data.pop('category')
        category_id = category_data['id']
        address_id = address_data['id']
        category = ElinCategory.objects.get(id=int(category_id))
        address = Address.objects.get(id=int(address_id))
        elin = Elin.objects.create(category=category,address=address,**validated_data)
        
        return elin

    class Meta:
        model = Elin
        fields = ('pk', 'name', 'address','text','phone','price','created','img1','img2','img3','img4','img5','checked','category','author')