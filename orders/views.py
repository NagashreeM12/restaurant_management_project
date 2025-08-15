from django.shortcuts import render

# Create your views here.
def home(request):
    #Render the homepage template that shows the prominent logo
    return render(request,"home/homepage.html")
