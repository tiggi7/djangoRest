from django.conf.urls import url
from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.toy_list),
    re_path(r'^(?P<pk>[0-9]+)$', views.toy_detail),
]