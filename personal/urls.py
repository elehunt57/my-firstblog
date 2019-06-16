from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    path('homepage/', views.homepage, name='homepage'),
]