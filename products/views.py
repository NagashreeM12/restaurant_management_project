from django.shortcuts import render
from .models import MenuItem
def menu_view(request):
    #Fetch all menu items from DB
    items=MenuItem.objects.all()
    return render(request,'products/menu.html',{'items':items})
