from django.urls import path
from .views import profile
from phome import views as home_views
urlpatterns = [
    path('', home_views.index, name='index'),
    path("profile/", profile, name="profile"),
    
]