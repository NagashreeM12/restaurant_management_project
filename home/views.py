# views.py
# views.py
from django.shortcuts import render

def about_us(request):
    # You can pass any dynamic content you want, like restaurant history, mission, etc.
    context = {
        'history': "Our restaurant was founded in 2000 with a mission to provide high-quality food.",
        'mission': "Our mission is to bring the finest dining experience with top-notch customer service.",
        'values': "We value sustainability, quality, and customer satisfaction.",
    }
    return render(request, 'about_us.html', context)







