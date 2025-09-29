# orders/urls.py
from django.urls import path
from .views import OrderRetrieveView

urlpatterns = [
    path("<int:order_id>/", OrderRetrieveView.as_view(), name="order-retrieve"),
]
