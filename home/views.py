from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the data (save/send email etc.)
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            return HttpResponse("Thank you! Your message has been received.")
    else:
        form = ContactForm()

    return render(request, 'home/contact.html', {'form': form})



