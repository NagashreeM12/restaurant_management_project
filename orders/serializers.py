# orders/serializers.py
# orders/serializers.py
from rest_framework import serializers
from .models import Order

class OrderStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'status']

    def validate_status(self, value):
        """Ensure the provided status is one of the allowed choices."""
        allowed_statuses = [choice[0] for choice in Order.STATUS_CHOICES]
        if value not in allowed_statuses:
            raise serializers.ValidationError(f"'{value}' is not a valid status. Allowed: {allowed_statuses}")
        return value
