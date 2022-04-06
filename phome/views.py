from xml.dom import INVALID_MODIFICATION_ERR
from django.shortcuts import render, HttpResponse
from .models import Cuisines_category
def index(request):

    cuisines_category1=Cuisines_category()
    cuisines_category1.id=0
    cuisines_category1.name='North Indian'
    cuisines_category1.desp='Spciy foods with great taste of North India'
    cuisines_category1.path='main/img/american1.jpg'

    cuisines_category2=Cuisines_category()
    cuisines_category2.id=1
    cuisines_category2.name='South Indian'
    cuisines_category2.desp='Taditional and Healthy with great taste of South India'
    cuisines_category2.path=''

    cuisines_category3=Cuisines_category()
    cuisines_category3.id=2
    cuisines_category3.name='Chinese'
    cuisines_category3.desp='First prefered light meal of every Indian'
    cuisines_category3.path=''

    cuisines_category4=Cuisines_category()
    cuisines_category4.id=3
    cuisines_category4.name='Thai'
    cuisines_category4.desp='Famous recipies that comes all the way from Thailand'
    cuisines_category4.path=''

    cuisines_category5=Cuisines_category()
    cuisines_category5.id=4
    cuisines_category5.name='American'
    cuisines_category5.desp='All famous burgers, pizzas and so on recipies are here'
    cuisines_category5.path=''

    cuisines_category6=Cuisines_category()
    cuisines_category6.id=5
    cuisines_category6.name='French'
    cuisines_category6.desp="French food boasts a rich and sweeping culinary history that includes rustic home cooking, elaborate court-dining masterpieces, and avant garde Parisian haute cuisine. Here some of our favorite French recipes, from Normandy to the Côte d’Azur (and everywhere in between)."
    cuisines_category6.path=''

    cuisines_category7=Cuisines_category()
    cuisines_category7.id=6
    cuisines_category7.name='Mexican'
    cuisines_category7.desp="Mexican Recipes- Feisty, vibrant and mysterious - these words define the land of Mexico. Mexico's cuisine has been blessed with numerous influences, ranging from the early civilization of the Aztecs and Mayas to modern European."
    cuisines_category7.path=''

    cuisines_category8=Cuisines_category()
    cuisines_category8.id=7    
    cuisines_category8.name='Italian'
    cuisines_category8.desp='Here Are Our 15 best Italian recipes, ranging from Focaccia bread to a luscious tiramisu and more. Buon appetito!'
    cuisines_category8.path=''

    cuisines_category9=Cuisines_category()
    cuisines_category9.id=8
    cuisines_category9.name='Barbeque'
    cuisines_category9.desp="Barbecue is probably the world's oldest cooking method. We've rounded up our 13 best barbecue recipes that you can try at home on a bonfire night with family and friends."
    cuisines_category9.path=''

    cuisines_category10=Cuisines_category()
    cuisines_category10.id=9
    cuisines_category10.name='Japanese'
    cuisines_category10.desp='The traditional cuisine of Japan (Japanese: washoku) is based on rice with miso soup and other dishes; there is an emphasis on seasonal ingredients. Side dishes often consist of fish, pickled vegetables, and vegetables cooked in broth. Seafood is common, often grilled, but also served raw as sashimi or in sushi.'
    cuisines_category10.path=''

    Cuisines_categories=[cuisines_category1,cuisines_category2,cuisines_category3,cuisines_category4,cuisines_category5,cuisines_category6,cuisines_category7,cuisines_category8,cuisines_category9,cuisines_category10]
    
    return render(request,'main/index.html',{'cuisines_categories':Cuisines_categories})


