from django.urls import path
from .views import register_rider, register_driver

urlpatterns = [
    path('api/register/rider/', register_rider, name='register-rider'),
    path('api/register/driver/', register_driver, name='register-driver'),
]
