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

class LogistCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LogistCategory
        fields = ('pk', 'name')

class ElinCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ElinCategory
        fields = ('pk', 'name')

class CarCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CarCategory
        fields = ('pk', 'name')

class OtherCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherCategory
        fields = ('pk', 'name')

class ServiceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = ('pk', 'name')

class NewsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsCategory
        fields = ('pk', 'name')


#/////////////////////////////////////////////////////////////////////////
class AddedProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopProducts
        fields = ('pk', 'name', 'address','text','category','phone','price','created','img1','img2','img3','img4','img5','checked')
class AddedProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopProducts
        fields = ('pk', 'name', 'address','text','category','phone','price','created','img1','checked')


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
        fields = ('pk', 'name', 'address','text','phone','price','created','img1','img2','img3','img4','img5','checked','category')

class ServiceDetailSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name')
    address_name = serializers.CharField(source='address.name')
    class Meta:
        model = Service
        fields = ('pk', 'name', 'address_name','text','category_name','phone','price','created','img1','img2','img3','img4','img5','checked')

class ServiceSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.id')
    address = serializers.CharField(source='address.id')

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        category_data = validated_data.pop('category')

        category_id = category_data['id']
        address_id = address_data['id']
        category = ServiceCategory.objects.get(id=int(category_id))
        address = Address.objects.get(id=int(address_id))
        service = Service.objects.create(category=category,address=address,**validated_data)
        
        return service

    class Meta:
        model = Service
        fields = ('pk', 'name', 'address','author','text','phone','price','created','img1','img2','img3','img4','img5','checked','category')

class OtherDetailSerializer(serializers.ModelSerializer):
    category = serializers.CharField()
    address = serializers.CharField()
    class Meta:
        model = Other
        fields = ('pk', 'name', 'address_name','text','category_name','phone','price','created','img1','img2','img3','img4','img5','checked')

class OtherListSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name')
    address_name = serializers.CharField(source='address.name')
    class Meta:
        model = Other
        fields = ('pk', 'name', 'text','phone','price','created','img1','checked','address_name','category_name')

class OtherSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.id')
    address = serializers.CharField(source='address.id')

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        category_data = validated_data.pop('category')

        category_id = category_data['id']
        address_id = address_data['id']
        category = OtherCategory.objects.get(id=int(category_id))
        address = Address.objects.get(id=int(address_id))
        other = Other.objects.create(category=category,address=address,**validated_data)
        
        return other

    class Meta:
        model = Other
        fields = ('pk', 'name', 'address','text','phone','price','created','img1','img2','img3','img4','img5','checked','category')


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

    


class NewsSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name')
    class Meta:
        model = News
        fields = ('pk', 'name','img', 'author','text','category','created' ,'checked')
