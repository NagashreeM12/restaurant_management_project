# home/serializersfrom rest_framework import serializers
from rest_framework import serializers
from .models import Order

class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['unique_id', 'status']
