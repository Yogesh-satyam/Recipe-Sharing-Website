from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .forms import SignUp
from django.contrib.auth.models import User
from django.contrib import messages

def signup(request):
    if request.method=='POST':
        form = SignUp(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            name=form.cleaned_data.get('name').split(' ')
           
            us=User.objects.get(username=username)
            us.email=username
            us.first_name=name[0]
            us.last_name=name[0]
            us.save()
            messages.success(request,'Account is created successfully')
            return redirect('login')
    else:
        form=SignUp()
    return render(request,'user/signup.html',{'form':form})

def login(request):
    return render(request,'userprofile/Profile.html')
    
        
    

# Create your views here.
