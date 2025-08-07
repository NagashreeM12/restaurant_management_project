from django.urls import path
from .views import *
from django.conf.urls import handler404

urlpatterns = [
    path('items/', ItemView.as_view(), name='item-list'),
]
#Link custom 404 handler
handler404='your-app-name.views'