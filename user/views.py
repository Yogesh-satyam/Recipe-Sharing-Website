from django.forms import ValidationError
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from .validate import MinimumLengthValidator, NumberValidator, UppercaseValidator

def signup(request):
    if request.method=='POST':
        form = request.POST
        first_name=form['first-name']
        last_name=form['last-name']
        username=form['username']
        email=form['email']
        password=request.POST['password']
        cnf_password=form['cnf-password']

        if(password==cnf_password):
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email has been alreay used')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username already taken')
                return redirect('signup')
            else:
                validators = [MinimumLengthValidator, NumberValidator, UppercaseValidator]     
                try:
                    for validator in validators:
                        validator().validate(password)
                except ValidationError as e:
                    messages.info(request, str(e))
                    return redirect('signup')
                user=User.objects.create_user(username=username,email=email,password=password,first_name=first_name,last_name=last_name)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'Password did not match')
            return redirect('signup')
    else:   
        return render(request,'user/signup.html')

def login(request):
    return redirect('/')
    
def index(request):
    return redirect('/')
        
    

# Create your views here.
