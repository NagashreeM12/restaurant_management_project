from django.urls import path
from .views import *
from django.contrib import admin
from myapp import views
from myapp import homepage

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('admin/',admin.site.urls),

]