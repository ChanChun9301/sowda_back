from rest_framework import generics,filters
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.reverse import reverse
from car.views_serializers import *
from service.views_serializers import *
from logist.views_serializers import *
from other.views_serializers import *
from elin.views_serializers import *
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

class UserLoginAPIView(APIView):
    def post(self, request, *args, **kargs):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            response = {
                "username": {
                    "detail": "User Doesnot exist!"
                }
            }
            if User.objects.filter(username=request.data['username']).exists():
                user = User.objects.get(username=request.data['username'])
                token, created = Token.objects.get_or_create(user=user)
                response = {
                    'success': True,
                    'token': token.key
                }
                return Response(response, status=status.HTTP_200_OK)
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args):
        token = Token.objects.get(user=request.user)
        token.delete()
        return Response({"success": True, "detail": "Logged out!"}, status=status.HTTP_200_OK)

class UserPost(generics.ListCreateAPIView):
    queryset = UserProd.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['author']
    name = 'user'

    def get_queryset(self):
        queryset = super().get_queryset()
        author = self.request.query_params.get('author')

        # if checked:
        #     checked = bool(checked) 
        #     queryset = queryset.get(checked=checked)
        # else:
        #     queryset= {'token':False}

        return queryset

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProd.objects.all()
    serializer_class = UserSerializer
    name = 'userprod-detail'

class AddressDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    name = 'address-detail'

class AddressList(generics.ListAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    name = 'address-list'
#----------------------------
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
    name = 'Seýir'

    def get(self, request, *args, **kwargs):
        return Response({
            'user': reverse(UserPost.name, request=request),
            'top': reverse(TopProductsList.name, request=request),
            'address': reverse(AddressList.name, request=request),

            'logist': reverse(LogistMainList.name, request=request),
            'logist-gosulan': reverse(LogistAddList.name, request=request),
            'logist-gosmak': reverse(LogistList.name, request=request),
            'logist - category': reverse(LogistCategoryList.name, request=request),
            'logist - by_category': reverse(LogistByCategoryList.name, request=request),
            'logist - by_address': reverse(LogistByAddressList.name, request=request),

            'elin': reverse(ElinMainList.name, request=request),
            'elin-gosulan': reverse(ElinAddList.name, request=request),
            'elin-gosmak': reverse(ElinList.name, request=request),
            'elin - category': reverse(ElinCategoryList.name, request=request),
            'elin - by_category': reverse(ElinByCategoryList.name, request=request),
            'elin - by_address': reverse(ElinByAddressList.name, request=request),

            'beyleki': reverse(OtherMainList.name, request=request),
            'beyleki-gosulan': reverse(OtherAddList.name, request=request),
            'beyleki-gosmak': reverse(OtherList.name, request=request),
            'beyleki - category': reverse(OtherCategoryList.name, request=request),
            'beyleki - by_category': reverse(OtherByCategoryList.name, request=request),
            'beyleki - by_address': reverse(OtherByAddressList.name, request=request),

            'hyzmat': reverse(ServiceMainList.name, request=request),
            'hyzmat-gosulan': reverse(ServiceAddList.name, request=request),
            'hyzmat-gosmak': reverse(ServiceList.name, request=request),
            'hyzmat - category': reverse(ServiceCategoryList.name, request=request),
            'hyzmat - by_category': reverse(ServiceByCategoryList.name, request=request),
            'hyzmat - by_address': reverse(ServiceByAddressList.name, request=request),

            'awtoulag': reverse(CarMainList.name, request=request),
            'awtoulag-gosulan': reverse(CarAddList.name, request=request),
            'awtoulag-gosmak': reverse(CarList.name, request=request),
            'awtoulag - category': reverse(CarCategoryList.name, request=request),
            'awtoulag - by_category': reverse(CarByCategoryList.name, request=request),
            'awtoulag - by_address': reverse(CarByAddressList.name, request=request),

            'habarlar': reverse(NewsList.name, request=request),
            'habarlar - category': reverse(NewsCategoryList.name, request=request),
            'habarlar - by_category': reverse(NewsByCategoryList.name, request=request),

            'carousel_surat': reverse(CarouselList.name, request=request),


            })
