from django.urls import re_path
from .views_serializers import *

urlpatterns = [
    re_path(r'^other-list/$', OtherList.as_view(), name=OtherList.name),
    re_path(r'^othermain-list/$', OtherMainList.as_view(), name=OtherMainList.name),
    re_path(r'^other-added-list/$', OtherAddList.as_view(), name=OtherAddList.name),
    re_path(r'^other-list/(?P<pk>[0-9]+)$', OtherDetail.as_view(), name=OtherDetail.name),
    re_path(r'^othercategory-list/$', OtherCategoryList.as_view(), name=OtherCategoryList.name),
    re_path(r'^other-by-address-list/$', OtherByAddressList.as_view(), name=OtherByAddressList.name),
    re_path(r'^other-by-category-list/$', OtherByCategoryList.as_view(), name=OtherByCategoryList.name),
]








