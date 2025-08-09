from django.urls import path
from myapp import views
#from myapp import homepage

urlpatterns = [
    path('menu/',views.menu_items_view, name='menu'),
    path('',home,name='home'),
    ]
