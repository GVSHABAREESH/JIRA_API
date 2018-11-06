from django.conf.urls import include, url
from django.contrib import admin
from .viewsets import MyClassviewsets
from rest_framework import routers

route = routers.DefaultRouter()
route.register(r'hi',MyClassviewsets)

urlpatterns = [
    url(r'^',include(route.urls)),
]
