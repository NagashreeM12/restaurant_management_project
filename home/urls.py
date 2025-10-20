# urls.py
# home/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('daily-specials/', views.daily_specials, name='daily-specials'),
]
