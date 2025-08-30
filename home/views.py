# views.py
from django.shortcuts import render
from .models import Restaurant

def homepage(request):
    # Fetch the restaurant object (assuming there's only one restaurant)
    restaurant = Restaurant.objects.first()
    
    # Pass the restaurant's phone number to the template
    return render(request, 'index.html', {'phone_number': restaurant.phone_number})






