from django.urls import path
from .views import *
from django.contrib import admin
from myapp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('admin/',admin.site.urls),

]