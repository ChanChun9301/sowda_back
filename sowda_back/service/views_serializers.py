from rest_framework import generics,filters,pagination
from .models import *
from .serializers import *
from api.serializers import *

class MyPagination(pagination.PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 1000

class ServiceMainList(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    filter_backends = [filters.SearchFilter]
    pagination_class = MyPagination
    search_fields = ['name']
    name = 'servicemain-list'

    def get_queryset(self):
        queryset = super().get_queryset()
        checked = self.request.query_params.get('checked')

        if checked is not None:
            checked = bool(checked) 
            queryset = queryset.filter(checked=checked)

        return queryset

class ServiceAddList(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceListSerializer
    filter_backends = [filters.SearchFilter]
    pagination_class = MyPagination
    search_fields = ['author']
    name = 'service-added-list'

    def get_queryset(self):
        queryset = super().get_queryset()
        author = self.request.query_params.get('author')

        print(author)
        if author:
            author = str(author) 
            queryset = queryset.filter(author=author)
        else:
            queryset=[]

        return queryset

class ServiceList(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    pagination_class = MyPagination
    name = 'service-list'

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
    pagination_class = MyPagination
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
    pagination_class = MyPagination
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