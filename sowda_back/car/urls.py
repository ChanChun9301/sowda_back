from django.urls import re_path
from .views_serializers import *

urlpatterns = [
    re_path(r'^car-list/$', CarList.as_view(), name=CarList.name),
    re_path(r'^carmain-list/$', CarMainList.as_view(), name=CarMainList.name),
    re_path(r'^car-added-list/$', CarAddList.as_view(), name=CarAddList.name),
    re_path(r'^car-list/(?P<pk>[0-9]+)$', CarDetail.as_view(), name=CarDetail.name),
    re_path(r'^carcategory-list/$', CarCategoryList.as_view(), name=CarCategoryList.name),
    re_path(r'^car-by-address-list/$', CarByAddressList.as_view(), name=CarByAddressList.name),
    re_path(r'^car-by-category-list/$', CarByCategoryList.as_view(), name=CarByCategoryList.name),
]








