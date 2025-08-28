from django.urls import path
from .import views
#from myapp import homepage

urlpatterns = [
    path("",views.homepage,name="homepage"),
]
