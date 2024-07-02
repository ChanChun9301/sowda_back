from rest_framework import generics,filters,status
from .models import *
from .serializers import *
from api.serializers import *

class LogistMainList(generics.ListAPIView):
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

class LogistAddList(generics.ListAPIView):
    queryset = Logist.objects.all()
    serializer_class = LogistSerializer
    search_fields = ['author']
    name = 'logist-added-list'

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

class LogistList(generics.ListCreateAPIView):
    queryset = Logist.objects.all()
    serializer_class = LogistSerializer
    name = 'logist-list'

class LogistDetail(generics.RetrieveDestroyAPIView):
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