from django.shortcuts import render
from products.models import Menu #Import Menu model
def home(request):
    menu_items=Menu.objects.all() #Get all menu items from DB
    return render(request,'home/index.html',{'menu_items':menu_items})


