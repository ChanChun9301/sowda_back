from rest_framework import generics,filters,status
from .models import *
from .serializers import *
import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.reverse import reverse
from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from django.shortcuts import render

def index(requests):
    datas = Car.objects.all()
    return render(requests,'index.html',{'datas':datas})

class Login(APIView):
    def get(self,request,format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

class LogistFilter(django_filters.FilterSet):
    is_checked = django_filters.BooleanFilter()  # boolean

    class Meta:
        model = Logist
        fields = ['checked']


class AddressDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    name = 'address-detail'

class AddressList(generics.ListAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    name = 'address-list'

#----------------------------------
class OwnList(generics.ListCreateAPIView):
    filter_backends = [
        DjangoFilterBackend,
    ]
    # filterset_class = LogistFilter
    queryset = AddedModel.objects.all()
    serializer_class =AddedProductsSerializer
    filter_backends = [filters.SearchFilter]
    filterset_fields = ['checked']
    search_fields = ['author']
    ordering_fields = ['created']
    name = 'own-list'
    

class OwnDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AddedModel.objects.all()
    serializer_class = AddedProductsSerializer
    name = 'own-detail'

#----------------------------
class LogistMainList(generics.ListAPIView):
    filterset_class = LogistFilter
    queryset = Logist.objects.all()
    serializer_class = LogistSerializer
    filter_backends = [filters.SearchFilter]
    filterset_fields = ['checked']
    search_fields = ['name']
    ordering_fields = ['created']
    name = 'logistmain-list'

    def get_queryset(self):
        queryset = super().get_queryset()
        checked = self.request.query_params.get('checked')

        if checked is not None:
            checked = bool(checked) 
            queryset = queryset.filter(checked=checked)

        return queryset

class LogistList(generics.ListCreateAPIView):
    queryset = Logist.objects.all()
    serializer_class = LogistSerializer
    permission_classes = [IsAdminUser]
    name = 'logist-list'

class LogistDetail(generics.RetrieveAPIView):
    queryset = Logist.objects.all()
    serializer_class = LogistDetailSerializer
    name = 'logist-detail'

class LogistCategoryList(generics.ListAPIView):
    queryset = LogistCategory.objects.all()
    serializer_class = LogistCategorySerializer
    name = 'logistcategory-list'

class LogistByCategoryList(generics.ListAPIView):
    category=LogistCategorySerializer
    queryset = Logist.objects.all()
    serializer_class = LogistSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['category__name']
    name = 'logist_by_category-list'

    def get_queryset(self):
        queryset = super().get_queryset()
        checked = self.request.query_params.get('checked')

        if checked is not None:
            checked = bool(checked) 
            queryset = queryset.filter(checked=checked)

        return queryset

class LogistByAddressList(generics.ListAPIView):
    address=AddressSerializer
    queryset = Logist.objects.all()
    serializer_class = LogistSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['address__name']
    name = 'logist_by_address-list'

    def get_queryset(self):
        queryset = super().get_queryset()
        checked = self.request.query_params.get('checked')

        if checked is not None:
            checked = bool(checked) 
            queryset = queryset.filter(checked=checked)

        return queryset
#------------------------------------

class ElinMainList(generics.ListAPIView):
    queryset = Elin.objects.all()
    serializer_class = ElinSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    name = 'elinmain-list'

    def get_queryset(self):
        queryset = super().get_queryset()
        checked = self.request.query_params.get('checked')

        if checked is not None:
            checked = bool(checked) 
            queryset = queryset.filter(checked=checked)

        return queryset

class ElinList(generics.ListCreateAPIView):
    queryset = Elin.objects.all()
    serializer_class = ElinSerializer
    permission_classes = [IsAdminUser]
    name = 'elin-list'

class ElinDetail(generics.RetrieveAPIView):
    queryset = Elin.objects.all()
    serializer_class = ElinDetailSerializer
    name = 'elin-detail'

class ElinCategoryList(generics.ListAPIView):
    queryset = ElinCategory.objects.all()
    serializer_class = ElinCategorySerializer
    name = 'elincategory-list'

class ElinByCategoryList(generics.ListAPIView):
    category=ElinCategorySerializer
    queryset = Elin.objects.all()
    serializer_class = ElinSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['category__name']
    name = 'elin_by_category-list'

    def get_queryset(self):
        queryset = super().get_queryset()
        checked = self.request.query_params.get('checked')

        if checked is not None:
            checked = bool(checked) 
            queryset = queryset.filter(checked=checked)

        return queryset

class ElinByAddressList(generics.ListAPIView):
    address=AddressSerializer
    queryset = Elin.objects.all()
    serializer_class = ElinSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['address__name']
    name = 'elin_by_address-list'

    def get_queryset(self):
        queryset = super().get_queryset()
        checked = self.request.query_params.get('checked')

        if checked is not None:
            checked = bool(checked) 
            queryset = queryset.filter(checked=checked)

        return queryset

#------------------------------------
class OtherMainList(generics.ListAPIView):
    queryset = Other.objects.all()
    serializer_class = OtherSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    name = 'other-list'

    def get_queryset(self):
        queryset = super().get_queryset()
        checked = self.request.query_params.get('checked')

        if checked is not None:
            checked = bool(checked) 
            queryset = queryset.filter(checked=checked)

        return queryset

class OtherList(generics.ListCreateAPIView):
    queryset = Other.objects.all()
    serializer_class = OtherSerializer
    permission_classes=[IsAdminUser]
    name = 'other-list'

class OtherDetail(generics.RetrieveAPIView):
    queryset = Other.objects.all()
    serializer_class = OtherDetailSerializer
    name = 'other-detail'

class OtherCategoryList(generics.ListAPIView):
    queryset = OtherCategory.objects.all()
    serializer_class = OtherCategorySerializer
    name = 'othercategory-list'

class OtherByCategoryList(generics.ListAPIView):
    category=OtherCategorySerializer
    queryset = Other.objects.all()
    serializer_class = OtherSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['category__name']
    name = 'other_by_category-list'

    def get_queryset(self):
        queryset = super().get_queryset()
        checked = self.request.query_params.get('checked')

        if checked is not None:
            checked = bool(checked) 
            queryset = queryset.filter(checked=checked)

        return queryset

class OtherByAddressList(generics.ListAPIView):
    address=AddressSerializer
    queryset = Other.objects.all()
    serializer_class = OtherSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['address__name']
    name = 'other_by_address-list'

    def get_queryset(self):
        queryset = super().get_queryset()
        checked = self.request.query_params.get('checked')

        if checked is not None:
            checked = bool(checked) 
            queryset = queryset.filter(checked=checked)

        return queryset

#------------------------------------

class CarMainList(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    name = 'carmain-list'

    def get_queryset(self):
        queryset = super().get_queryset()
        checked = self.request.query_params.get('checked')

        if checked is not None:
            checked = bool(checked) 
            queryset = queryset.filter(checked=checked)

        return queryset

class CarList(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes=[IsAdminUser]
    name = 'car-list'

class CarDetail(generics.RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarDetailSerializer
    name = 'car-detail'

class CarCategoryList(generics.ListAPIView):
    queryset = CarCategory.objects.all()
    serializer_class = CarCategorySerializer
    name = 'carcategory-list'

class CarByCategoryList(generics.ListAPIView):
    category=CarCategorySerializer
    queryset = Car.objects.all()
    serializer_class = CarListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['category__name']
    name = 'car_by_category-list'

    def get_queryset(self):
        queryset = super().get_queryset()
        checked = self.request.query_params.get('checked')

        if checked is not None:
            checked = bool(checked) 
            queryset = queryset.filter(checked=checked)

        return queryset

class CarByAddressList(generics.ListAPIView):
    address=AddressSerializer
    queryset = Car.objects.all()
    serializer_class = CarListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['address__name']
    name = 'car_by_address-list'

    def get_queryset(self):
        queryset = super().get_queryset()
        checked = self.request.query_params.get('checked')

        if checked is not None:
            checked = bool(checked) 
            queryset = queryset.filter(checked=checked)

        return queryset

#------------------------------------

class NewsList(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    name = 'news-list'

    def get_queryset(self):
        queryset = super().get_queryset()
        checked = self.request.query_params.get('checked')

        if checked is not None:
            checked = bool(checked) 
            queryset = queryset.filter(checked=checked)

        return queryset

class NewsDetail(generics.RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    name = 'news-detail'

class NewsCategoryList(generics.ListAPIView):
    queryset = NewsCategory.objects.all()
    serializer_class = NewsCategorySerializer
    name = 'newscategory-list'

class NewsByCategoryList(generics.ListAPIView):
    category=NewsCategorySerializer
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['category__name']
    name = 'news_by_category-list'

    def get_queryset(self):
        queryset = super().get_queryset()
        checked = self.request.query_params.get('checked')

        if checked is not None:
            checked = bool(checked) 
            queryset = queryset.filter(checked=checked)

        return queryset

#------------------------------------
class ServiceMainList(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    name = 'servicemain-list'

    def get_queryset(self):
        queryset = super().get_queryset()
        checked = self.request.query_params.get('checked')

        if checked is not None:
            checked = bool(checked) 
            queryset = queryset.filter(checked=checked)

        return queryset

class ServiceList(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    name = 'service-list'
    permission_classes=[IsAdminUser]

class ServiceDetail(generics.RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceDetailSerializer
    name = 'service-detail'

class ServiceCategoryList(generics.ListAPIView):
    queryset = ServiceCategory.objects.all()
    serializer_class = ServiceCategorySerializer
    name = 'servicecategory-list'

class ServiceByCategoryList(generics.ListAPIView):
    category=ServiceCategorySerializer
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['category__name']
    name = 'service_by_category-list'

    def get_queryset(self):
        queryset = super().get_queryset()
        checked = self.request.query_params.get('checked')

        if checked is not None:
            checked = bool(checked) 
            queryset = queryset.filter(checked=checked)

        return queryset

class ServiceByAddressList(generics.ListAPIView):
    address=AddressSerializer
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['address__name']
    name = 'service_by_address-list'

    def get_queryset(self):
        queryset = super().get_queryset()
        checked = self.request.query_params.get('checked')

        if checked is not None:
            checked = bool(checked) 
            queryset = queryset.filter(checked=checked)

        return queryset

#------------------------------------

class TopProductsList(generics.ListAPIView):
    queryset = TopProducts.objects.all()
    serializer_class = TopProductsSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    name = 'top-list'

    def get_queryset(self):
        queryset = super().get_queryset()
        checked = self.request.query_params.get('checked')

        if checked is not None:
            checked = bool(checked) 
            queryset = queryset.filter(checked=checked)

        return queryset

class TopProductsDetail(generics.RetrieveAPIView):
    queryset = TopProducts.objects.all()
    serializer_class =TopProductDetailSerializer
    name = 'top-detail'

#------------------------------------


class CarouselList(generics.ListAPIView):
    queryset = CarouselImage.objects.all()
    serializer_class = CarouselSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'address']
    name = 'carousel-list'

class CarouselDetail(generics.RetrieveAPIView):
    queryset = CarouselImage.objects.all()
    serializer_class = CarouselSerializer
    name = 'carousel-detail'

class ApiRoot(generics.GenericAPIView):
    name = 'Seyir'

    def get(self, request, *args, **kwargs):
        return Response({
            'top': reverse(TopProductsList.name, request=request),
            'address': reverse(AddressList.name, request=request),
            'gosulan': reverse(OwnList.name, request=request),
            'favorite': reverse(OwnList.name, request=request),
            'logist': reverse(LogistMainList.name, request=request),
            'logist-gosmak': reverse(LogistList.name, request=request),
            'logist - category': reverse(LogistCategoryList.name, request=request),
            'logist - by_category': reverse(LogistByCategoryList.name, request=request),
            'logist - by_address': reverse(LogistByAddressList.name, request=request),

            'elinler': reverse(ElinMainList.name, request=request),
            'elinler-gosmak': reverse(ElinList.name, request=request),
            'elinler - category': reverse(ElinCategoryList.name, request=request),
            'elinler - by_category': reverse(ElinByCategoryList.name, request=request),
            'elinler - by_address': reverse(ElinByAddressList.name, request=request),

            'beylekiler': reverse(OtherMainList.name, request=request),
            'beylekiler-gosmak': reverse(OtherList.name, request=request),
            'beylekiler - category': reverse(OtherCategoryList.name, request=request),
            'beylekiler - by_category': reverse(OtherByCategoryList.name, request=request),
            'beylekiler - by_address': reverse(OtherByAddressList.name, request=request),

            'hyzmatlar': reverse(ServiceMainList.name, request=request),
            'hyzmatlar-gosmak': reverse(ServiceList.name, request=request),
            'hyzmatlar - category': reverse(ServiceCategoryList.name, request=request),
            'hyzmatlar - by_category': reverse(ServiceByCategoryList.name, request=request),
            'hyzmatlar - by_address': reverse(ServiceByAddressList.name, request=request),

            'awtoulaglar': reverse(CarMainList.name, request=request),
            'awtoulaglar-gosmak': reverse(CarList.name, request=request),
            'awtoulaglar - category': reverse(CarCategoryList.name, request=request),
            'awtoulaglar - by_category': reverse(CarByCategoryList.name, request=request),
            'awtoulaglar - by_address': reverse(CarByAddressList.name, request=request),

            'habarlar': reverse(NewsList.name, request=request),
            'habarlar - category': reverse(NewsCategoryList.name, request=request),
            'habarlar - by_category': reverse(NewsByCategoryList.name, request=request),

            'carousel_surat': reverse(CarouselList.name, request=request),


            })
