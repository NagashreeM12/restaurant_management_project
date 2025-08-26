from django.urls import path
from .views import contact_view
#from myapp import homepage

urlpatterns = [
    path('contact/',contact_view,name='contact'),
]
