#home/forms.py
from django.shortcuts import render,redirect
from.forms import ContactForm
def contact_view(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save() #save to database
            return redirect('contact') #redirect after success
        else:
            form=ContactForm()
        return render(request,'home/contact.html',{'form':form})