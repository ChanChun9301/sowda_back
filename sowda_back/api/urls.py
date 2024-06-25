from django.urls import re_path
from .views_serializers import *

urlpatterns = [
    re_path(r'^address-list/$', AddressList.as_view(), name=AddressList.name),
    re_path(r'^address-list/(?P<pk>[0-9]+)$', AddressDetail.as_view(), name=AddressDetail.name),

    re_path(r'^topmain-list/$', TopProductsList.as_view(), name=TopProductsList.name),
    re_path(r'^top-list/(?P<pk>[0-9]+)$', TopProductsDetail.as_view(), name=TopProductsDetail.name),

    re_path(r'^news-list/$', NewsList.as_view(), name=NewsList.name),
    re_path(r'^news-list/(?P<pk>[0-9]+)$', NewsDetail.as_view(), name=NewsDetail.name),
    re_path(r'^newscategory-list/$', NewsCategoryList.as_view(), name=NewsCategoryList.name),
    re_path(r'^news-by-category-list/$', NewsByCategoryList.as_view(), name=NewsByCategoryList.name),

    re_path(r'^carousel-list/$', CarouselList.as_view(), name=CarouselList.name),
    re_path(r'^carousel-list/(?P<pk>[0-9]+)$', CarouselDetail.as_view(), name=CarouselDetail.name),

    re_path(r'^$', ApiRoot.as_view(), name=ApiRoot.name)
]








