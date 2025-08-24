from django.urls import path
from .import views
from django.conf.urls import handler404

urlpatterns = [
    path('menu/', views.menu_view,name='menu'),#/menu page
]