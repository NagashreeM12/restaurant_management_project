from django.shortcuts import render
from .models import RestaurantAddress
def homepage(request):
    address=RestaurantAddress.objects.first() # Fetch first address
    return render(request,"home/homepage.html",{"address":address})
    


