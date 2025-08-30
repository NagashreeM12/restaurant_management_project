# views.py
# views.py
from django.shortcuts import render

# views.py
from django.shortcuts import render
from .models import Restaurant

def homepage(request):
    # Fetch the restaurant object (assuming only one restaurant exists)
    restaurant = Restaurant.objects.first()
    
    # Pass the restaurant logo and phone number to the template
    return render(request, 'index.html', {'restaurant': restaurant, 'phone_number': restaurant.phone_number})








