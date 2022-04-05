from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class SignUp(UserCreationForm):
    name=forms.CharField( label =("Full name"))
    username=forms.EmailField(label=("email"))
    class Meta:
        model=User
        fields=('name','username','password1','password2')
