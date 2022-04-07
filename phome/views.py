from xml.dom import INVALID_MODIFICATION_ERR
from django.shortcuts import render, HttpResponse
from .models import Cuisines_category
def index(request):

    Cuisines_categories=Cuisines_category.objects.all()
    
    return render(request,'main/index.html',{'cuisines_categories':Cuisines_categories})


