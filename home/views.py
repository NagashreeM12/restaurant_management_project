from django.shortcuts import render
from .forms import ContactForm
def home_view(request):
    if request.method=="POST":
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()#save to database
            return redirect("home") #redirect to homepage after submission
        else:
            form=ContactForm()
        return render(request,"home/index.html",{"form":form})
    


