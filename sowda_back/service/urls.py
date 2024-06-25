from django.urls import re_path
from .views_serializers import *

urlpatterns = [
    re_path(r'^service-list/$', ServiceList.as_view(), name=ServiceList.name),
    re_path(r'^servicemain-list/$', ServiceMainList.as_view(), name=ServiceMainList.name),
    re_path(r'^service-added-list/$', ServiceAddList.as_view(), name=ServiceAddList.name),
    re_path(r'^service-list/(?P<pk>[0-9]+)$', ServiceDetail.as_view(), name=ServiceDetail.name),
    re_path(r'^servicecategory-list/$', ServiceCategoryList.as_view(), name=ServiceCategoryList.name),
    re_path(r'^service-by-address-list/$', ServiceByAddressList.as_view(), name=ServiceByAddressList.name),
    re_path(r'^service-by-category-list/$', ServiceByCategoryList.as_view(), name=ServiceByCategoryList.name),
]








