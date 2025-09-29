# orders/views.py
from rest_framework import generics
from .models import Order
from .serializers import OrderSerializer

class OrderRetrieveView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = "order_id"  # use order_id instead of pk

