from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return HttpResponse("""
    <html>
    <head>
    <title>My Restaurant App </title>
    </head>
    <body style="font-family:Arial,sans-serif;background-color:#f4f4f4;margin:0;padding:0;">
    <div style="max-width:800px;margin:50px auto;background_color:white;padding:40px;border-radius:8px;bpx-shadow:0 0 10px rgba(0,0,0,1);">
    <h1 style="color:#333;text-align:center;">Welcome to the Restaurant Manager System </h1>
    <p style="text-align:center;font-size:18px;color:#555;">
    Use the navigation menu to register restaurants,add menu items and manage your system
    </p>
    <p style="text-align:center;margin-top:30px;">
    <a href="/admin/"style="text-decoration:none;padding:10px 20px;background-color:#4CAF50;color:white;border-radius:4px;">Go to Admin Panel </a>
    </p>
    </div>
    </body>
    </html>
    """)

# Create your views here.
def home(request):
    context={
        'restaurant_name':'Delightful Bites'
        
    }
    return render(request,'home.html',context)
def contact(request):
    return render(request,'contact.html')