from rest_framework import generics,filters,pagination
from .models import *
from .serializers import *
from api.serializers import *

class MyPagination(pagination.PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 1000
#------------------------------------
class OtherMainList(generics.ListAPIView):
    queryset = Other.objects.all()
    serializer_class = OtherSerializer
    pagination_class = MyPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    name = 'othermain-list'

    def get_queryset(self):
        queryset = super().get_queryset()
        checked = self.request.query_params.get('checked')

        if checked is not None:
            checked = bool(checked) 
            queryset = queryset.filter(checked=checked)

        return queryset

class OtherAddList(generics.ListAPIView):
    queryset = Other.objects.all()
    serializer_class = OtherListSerializer
    pagination_class = MyPagination
    search_fields = ['author']
    name = 'other-added-list'

    def get_queryset(self):
        queryset = super().get_queryset()
        author = self.request.query_params.get('author')

        if author:
            author = str(author) 
            queryset = queryset.filter(author=author)
        else:
            queryset=[]

        return queryset

class OtherList(generics.ListCreateAPIView):
    queryset = Other.objects.all()
    pagination_class = MyPagination
    serializer_class = OtherSerializer
    name = 'other-list'

class OtherDetail(generics.RetrieveDestroyAPIView):
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
    pagination_class = MyPagination
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
    pagination_class = MyPagination
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
