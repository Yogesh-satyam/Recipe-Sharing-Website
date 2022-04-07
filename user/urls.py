
from django.urls import path
from .views import login, signup
from phome import views as home_views

urlpatterns = [
    path('', home_views.index, name='index'),
    path("signup/", signup, name="signup"),
    path("login/", login,name="login"),
     
]