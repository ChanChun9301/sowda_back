from rest_framework import generics,filters
from .models import *
from .serializers import *
from api.serializers import *


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

class ServiceAddList(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['author']
    name = 'service-added-list'

class ServiceList(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
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