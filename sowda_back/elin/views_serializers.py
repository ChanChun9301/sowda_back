from rest_framework import generics,filters
from .models import *
from .serializers import *
from api.serializers import *


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

class ElinAddList(generics.ListAPIView):
    queryset = Elin.objects.all()
    serializer_class = ElinSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['author']
    name = 'elin-added-list'

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
    
class ElinList(generics.ListCreateAPIView):
    queryset = Elin.objects.all()
    serializer_class = ElinSerializer
    name = 'elin-list'

class ElinDetail(generics.RetrieveDestroyAPIView):
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
