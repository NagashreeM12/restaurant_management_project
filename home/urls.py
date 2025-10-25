from django.urls import path
from .views import OrderStatusAPIView

urlpatterns = [
    path('api/orders/<str:unique_id>/status/', OrderStatusAPIView.as_view(), name='order-status'),
]
