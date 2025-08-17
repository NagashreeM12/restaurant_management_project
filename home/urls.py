from django.urls import path
from myapp import views
#from myapp import homepage

urlpatterns = [
    path("",views.home,name="home"),
]
