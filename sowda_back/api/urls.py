from django.urls import re_path,path
from .views_serializers import *
from .token_views import *

urlpatterns = [
    re_path(r'^new/',index),

    re_path(r'^address-list/$', AddressList.as_view(), name=AddressList.name),
    re_path(r'^address-list/(?P<pk>[0-9]+)$', AddressDetail.as_view(), name=AddressDetail.name),

    re_path(r'^token-login/$', login_token),
    re_path(r'^token-test/$', test_token),
    re_path(r'^token-sign/$', sign_token),

    re_path(r'^own-list/$', OwnList.as_view(), name=OwnList.name),
    re_path(r'^own-list/(?P<pk>[0-9]+)$', OwnDetail.as_view(), name=OwnDetail.name),
    
    re_path(r'^topmain-list/$', TopProductsList.as_view(), name=TopProductsList.name),
    re_path(r'^top-list/(?P<pk>[0-9]+)$', TopProductsDetail.as_view(), name=TopProductsDetail.name),

    
    re_path(r'^favorite-list/$', OwnList.as_view(), name=OwnList.name),
    re_path(r'^favorite-list/(?P<pk>[0-9]+)$', OwnDetail.as_view(), name=OwnDetail.name),

    re_path(r'^logist-list/$', LogistList.as_view(), name=LogistList.name),
    re_path(r'^logistmain-list/$', LogistMainList.as_view(), name=LogistMainList.name),
    re_path(r'^logist-list/(?P<pk>[0-9]+)$', LogistDetail.as_view(), name=LogistDetail.name),
    re_path(r'^logistcategory-list/$', LogistCategoryList.as_view(), name=LogistCategoryList.name),
    re_path(r'^logist-by-address-list/$', LogistByAddressList.as_view(), name=LogistByAddressList.name),
    re_path(r'^logist-by-category-list/$', LogistByCategoryList.as_view(), name=LogistByCategoryList.name),

    re_path(r'^elin-list/$', ElinList.as_view(), name=ElinList.name),  
    re_path(r'^elinmain-list/$', ElinMainList.as_view(), name=ElinMainList.name),  
    re_path(r'^elin-list/(?P<pk>[0-9]+)$', ElinDetail.as_view(), name=ElinDetail.name),
    re_path(r'^elincategory-list/$', ElinCategoryList.as_view(), name=ElinCategoryList.name),
    re_path(r'^elin-by-address-list/$', ElinByAddressList.as_view(), name=ElinByAddressList.name),
    re_path(r'^elin-by-category-list/$', ElinByCategoryList.as_view(), name=ElinByCategoryList.name),


    re_path(r'^other-list/$', OtherList.as_view(), name=OtherList.name),
    re_path(r'^othermain-list/$', OtherMainList.as_view(), name=OtherMainList.name),
    re_path(r'^other-list/(?P<pk>[0-9]+)$', OtherDetail.as_view(), name=OtherDetail.name),
    re_path(r'^othercategory-list/$', OtherCategoryList.as_view(), name=OtherCategoryList.name),
    re_path(r'^other-by-address-list/$', OtherByAddressList.as_view(), name=OtherByAddressList.name),
    re_path(r'^other-by-category-list/$', OtherByCategoryList.as_view(), name=OtherByCategoryList.name),

    
    re_path(r'^car-list/$', CarList.as_view(), name=CarList.name),
    re_path(r'^carmain-list/$', CarMainList.as_view(), name=CarMainList.name),
    re_path(r'^car-list/(?P<pk>[0-9]+)$', CarDetail.as_view(), name=CarDetail.name),
    re_path(r'^carcategory-list/$', CarCategoryList.as_view(), name=CarCategoryList.name),
    re_path(r'^car-by-address-list/$', CarByAddressList.as_view(), name=CarByAddressList.name),
    re_path(r'^car-by-category-list/$', CarByCategoryList.as_view(), name=CarByCategoryList.name),


    re_path(r'^service-list/$', ServiceList.as_view(), name=ServiceList.name),
    re_path(r'^servicemain-list/$', ServiceMainList.as_view(), name=ServiceMainList.name),
    re_path(r'^service-list/(?P<pk>[0-9]+)$', ServiceDetail.as_view(), name=ServiceDetail.name),
    re_path(r'^servicecategory-list/$', ServiceCategoryList.as_view(), name=ServiceCategoryList.name),
    re_path(r'^service-by-address-list/$', ServiceByAddressList.as_view(), name=ServiceByAddressList.name),
    re_path(r'^service-by-category-list/$', ServiceByCategoryList.as_view(), name=ServiceByCategoryList.name),

    re_path(r'^news-list/$', NewsList.as_view(), name=NewsList.name),
    re_path(r'^news-list/(?P<pk>[0-9]+)$', NewsDetail.as_view(), name=NewsDetail.name),
    re_path(r'^newscategory-list/$', NewsCategoryList.as_view(), name=NewsCategoryList.name),
    re_path(r'^news-by-category-list/$', NewsByCategoryList.as_view(), name=NewsByCategoryList.name),

    re_path(r'^carousel-list/$', CarouselList.as_view(), name=CarouselList.name),
    re_path(r'^carousel-list/(?P<pk>[0-9]+)$', CarouselDetail.as_view(), name=CarouselDetail.name),

    # path("<phone>/", getPhoneNumberRegistered.as_view(), name="OTP Gen"),
    # path("time_based/<phone>/", getPhoneNumberRegistered_TimeBased.as_view(), name="OTP Gen Time Based"),

    re_path(r'^$', ApiRoot.as_view(), name=ApiRoot.name)
]







