from django.urls import path
from .views import userprofile
from phome import views as home_views
urlpatterns = [
    path('', home_views.index, name='index'),
    path("userprofile/", userprofile, name="userprofile"),
    
]