
from django.urls import path
from .views import login, signup, logout
from phome import views as home_views

urlpatterns = [
    path('', home_views.index, name='index'),
    path("signup/", signup, name="signup"),
    path("login/", login ,name="login"),
    path("logout/", logout ,name="logout"),
    path("aboutus/", home_views.aboutus ,name="aboutus"),
     
]