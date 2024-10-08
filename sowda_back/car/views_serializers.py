from rest_framework import generics,filters, pagination
from .models import *
from .serializers import *
from api.serializers import *

class MyPagination(pagination.PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 1000

class CarMainList(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarListSerializer
    filter_backends = [filters.SearchFilter]
    pagination_class = MyPagination
    search_fields = ['name']
    name = 'carmain-list'

    def get_queryset(self):
        queryset = super().get_queryset()
        checked = self.request.query_params.get('checked')

        if checked is not None:
            checked = bool(checked) 
            queryset = queryset.filter(checked=checked)

        return queryset

class CarAddList(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarListSerializer
    filter_backends = [filters.SearchFilter]
    pagination_class = MyPagination
    search_fields = ['author']
    name = 'car-added-list'

    def get_queryset(self):
        queryset = super().get_queryset()
        author = self.request.query_params.get('author')

        if author:
            author = str(author) 
            queryset = queryset.filter(author=author)
        else:
            queryset=[]

        return queryset

class CarList(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    pagination_class = MyPagination
    serializer_class = CarSerializer
    name = 'car-list'

class CarDetail(generics.RetrieveDestroyAPIView):
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
    pagination_class = MyPagination
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
    pagination_class = MyPagination
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
