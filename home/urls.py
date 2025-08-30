# urls.py
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),  # Your homepage
    path('about_us/', views.about_us, name='about_us'),  # Add About Us page
]



