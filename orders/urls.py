# orders/urls.py
# orders/urls.py
from django.urls import path
from .views import get_order_status

urlpatterns = [
    path('orders/<int:order_id>/status/', get_order_status, name='get-order-status'),
]
