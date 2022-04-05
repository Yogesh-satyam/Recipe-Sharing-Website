
from operator import index
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path
from .views import login, signup
from django.contrib.auth.views import LoginView,LogoutView
from phome import views as home_views
from userprofile import views as userprofile_views
urlpatterns = [
    path('', home_views.index, name='index'),
    path("signup/", signup, name="signup"),
    path("login/", login,name="login"),
     
]