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
        password=form['password']
        cnf_password=form['cnf-password']



        if(password==cnf_password):    
            validators = [MinimumLengthValidator, NumberValidator, UppercaseValidator]     
            try:
                for validator in validators:
                    validator(password)

            except ValidationError as e:
                messages.error(request, str(e))
                return redirect('user/signup.html')
          
    else:
        form=SignUp()
    return render(request,'user/signup.html')

def login(request):
    return redirect('/')
    
        
    

# Create your views here.
