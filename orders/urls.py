# orders/urls.py
# orders/urls.py
from django.urls import path
from .views import CancelOrderView

urlpatterns = [
    path('orders/<int:order_id>/cancel/', CancelOrderView.as_view(), name='cancel-order'),
]
