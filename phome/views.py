from xml.dom import INVALID_MODIFICATION_ERR
from django.shortcuts import render, HttpResponse
from .models import Cuisines_category
def index(request):

    cuisines_category1=Cuisines_category()
    cuisines_category1.id=0
    cuisines_category1.name='North Indian'
    cuisines_category1.desp='Spciy foods with great taste of North India'

    cuisines_category2=Cuisines_category()
    cuisines_category2.id=1
    cuisines_category2.name='South Indian'
    cuisines_category2.desp='Taditional and Healthy with great taste of South India'

    cuisines_category3=Cuisines_category()
    cuisines_category3.id=2
    cuisines_category3.name='Chinese'
    cuisines_category3.desp='First prefered light meal of every Indian'

    cuisines_category4=Cuisines_category()
    cuisines_category4.id=3
    cuisines_category4.name='Thai'
    cuisines_category4.desp='Famous recipies that comes all the way from Thailand'

    cuisines_category5=Cuisines_category()
    cuisines_category5.id=4
    cuisines_category5.name='American'
    cuisines_category5.desp='All famous burgers, pizzas and so on recipies are here'

    # cuisines_category1=Cuisines_category()
    # cuisines_category1.id=0
    # cuisines_category1.name='North Indian'
    # cuisines_category1.desp='Spciy foods with great taste of North India'

    # cuisines_category1=Cuisines_category()
    # cuisines_category1.id=0
    # cuisines_category1.name='North Indian'
    # cuisines_category1.desp='Spciy foods with great taste of North India'

    # cuisines_category1=Cuisines_category()
    # cuisines_category1.id=0
    # cuisines_category1.name='North Indian'
    # cuisines_category1.desp='Spciy foods with great taste of North India'

    # cuisines_category1=Cuisines_category()
    # cuisines_category1.id=0
    # cuisines_category1.name='North Indian'
    # cuisines_category1.desp='Spciy foods with great taste of North India'

    Cuisines_categories=[cuisines_category1,cuisines_category2,cuisines_category3,cuisines_category4,cuisines_category5]
    
    return render(request,'main/index.html',{'cuisines_categories':Cuisines_categories})


