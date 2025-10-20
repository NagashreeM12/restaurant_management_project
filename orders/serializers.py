# orders/serializers.py
# orders/serializers.py
from rest_framework import serializers
from .models import Order

class OrderStatusUpdateSerializer(serializers.Serializer):
    order_id = serializers.CharField(max_length=50)
    status = serializers.ChoiceField(choices=[choice[0] for choice in Order.STATUS_CHOICES])
