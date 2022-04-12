from django.shortcuts import render
from .models import Cuisines_category
def index(request):
    Cuisines_categories=Cuisines_category.objects.all()
    return render(request,'main/index.html',{'cuisines_categories':Cuisines_categories})
    
def aboutus(request):
    return render(request,'aboutus/aboutus.html')

