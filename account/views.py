from django.shortcuts import render
from django.conf import settings
def homepage(request):
    phone_number=getattr(settings,'RESTAURANGT_PHONE','N/A')
    return render(request,'home/index.html',{'phone_number':phone_number})
    path