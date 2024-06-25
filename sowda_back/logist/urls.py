from django.urls import re_path
from .views_serializers import *

urlpatterns = [
    re_path(r'^logist-list/$', LogistList.as_view(), name=LogistList.name),
    re_path(r'^logistmain-list/$', LogistMainList.as_view(), name=LogistMainList.name),
    re_path(r'^logist-added-list/$', LogistAddList.as_view(), name=LogistAddList.name),
    re_path(r'^logist-list/(?P<pk>[0-9]+)$', LogistDetail.as_view(), name=LogistDetail.name),
    re_path(r'^logistcategory-list/$', LogistCategoryList.as_view(), name=LogistCategoryList.name),
    re_path(r'^logist-by-address-list/$', LogistByAddressList.as_view(), name=LogistByAddressList.name),
    re_path(r'^logist-by-category-list/$', LogistByCategoryList.as_view(), name=LogistByCategoryList.name),
]








