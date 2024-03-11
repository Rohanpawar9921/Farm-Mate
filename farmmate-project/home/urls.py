from . import views
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('login', views.LoginView.as_view(), name='login'),
]