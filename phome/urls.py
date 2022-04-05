from django.contrib import admin
from django.urls import path
from phome import views

urlpatterns = [
    path("",views.index,name='phome')
]