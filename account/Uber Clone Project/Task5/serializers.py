# serializers.py

from rest_framework import serializers
from .models import Ride


class RideRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = [
            "pickup_address", "dropoff_address",
            "pickup_lat", "pickup_lng",
            "drop_lat", "drop_lng"
        ]


class RideDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = "__all__"
