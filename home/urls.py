from django.urls import path
from myapp import views
from myapp import homepage

urlpatterns = [
    path('',views.home_view,name='home'),
    path('about/',views.about_view,name='about'),

]