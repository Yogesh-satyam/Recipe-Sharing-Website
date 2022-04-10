from django.urls import path
from phome import views

urlpatterns = [
    path('',views.index,name='index'),
    path("aboutus/", views.aboutus ,name="aboutus"),
]