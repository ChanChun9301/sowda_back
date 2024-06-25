from django.urls import re_path
from .views_serializers import *

urlpatterns = [
    re_path(r'^elin-list/$', ElinList.as_view(), name=ElinList.name),  
    re_path(r'^elinmain-list/$', ElinMainList.as_view(), name=ElinMainList.name),  
    re_path(r'^elin-added-list/$', ElinAddList.as_view(), name=ElinAddList.name),  
    re_path(r'^elin-list/(?P<pk>[0-9]+)$', ElinDetail.as_view(), name=ElinDetail.name),
    re_path(r'^elincategory-list/$', ElinCategoryList.as_view(), name=ElinCategoryList.name),
    re_path(r'^elin-by-address-list/$', ElinByAddressList.as_view(), name=ElinByAddressList.name),
    re_path(r'^elin-by-category-list/$', ElinByCategoryList.as_view(), name=ElinByCategoryList.name),
]








