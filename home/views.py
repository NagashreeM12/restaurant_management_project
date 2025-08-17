from django.shortcuts import render
def home(request):
    #For now we just render the template;no search logic yet
    return render(request,"home/home.html")

