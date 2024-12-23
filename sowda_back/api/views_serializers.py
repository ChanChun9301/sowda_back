from rest_framework import generics,filters,status,pagination
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
from rest_framework_simplejwt.tokens import RefreshToken

class UserPost(generics.ListCreateAPIView):
    queryset = UserProd.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['author']
    name = 'userprod-list'

class UserCreate(APIView):
    name = 'userprod-list'
    template_name = 'auth/login.html'
    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        if UserProd.objects.filter(author=data.get('author')).exists():
            return Response({'error': 'Ulanyjy bir eyyam bar.'},status=status.HTTP_201_CREATED)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLogout(APIView):
    name = 'user-logout'

    def post(self, request):
        data = request.data
        # serializer = UserSerializer(data=data)
        print('>>>?????'+str(data))
        try:
            checked = UserProd.objects.filter(author=data.get('author')).exists()
            user = UserProd.objects.get(author=data.get('author'))
            print('>>>>>>'+str(user.checked)) 
            if checked:
                user.checked = False
                user.save()
                return Response({'success': 'Ulanyjy ulgamdan cykdy.'},status=status.HTTP_200_OK)
        except:
            return Response({'error': 'Ulgamdan cykmak yerine yetmedi.'},status=status.HTTP_400_BAD_REQUEST)

class UserProdDetailView(APIView):
    
    def get(self, request):
        author = request.GET.get('author')
        try:
            check = UserProd.objects.get(author=author)
            if UserProd.objects.filter(author=author).exists():
                if (UserProd.objects.filter(checked=True)):
                    return Response({'token': check.checked})
            return Response({'token': check.checked})
        except UserProd.DoesNotExist:
            return Response({'token': False})

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
    pagination_class = MyPagination
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
    pagination_class = MyPagination
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
class ImageList(generics.ListAPIView):
    queryset = ImageTop.objects.all()
    serializer_class = ImageSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'top']
    name = 'imagetop-list'

class ImageDetail(generics.RetrieveAPIView):
    queryset = ImageTop.objects.all()
    serializer_class = ImageSerializer
    name = 'imagetop-detail'


class TopProductsList(generics.ListAPIView):
    queryset = TopProducts.objects.all()
    serializer_class = TopProductsSerializer
    filter_backends = [filters.SearchFilter]
    pagination_class = MyPagination
    search_fields = ['name']
    name = 'topmain-list'

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
    name = 'topmain-detail'

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
            'imagetop': reverse(ImageList.name, request=request),
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
