from rest_framework import serializers
from .models import Ride

class RideHistorySerializer(serializers.ModelSerializer):
    rider = serializers.CharField(source="rider.username", read_only=True)
    driver = serializers.CharField(source="driver.username", read_only=True)

    class Meta:
        model = Ride
        fields = ["pickup", "drop", "status", "requested_at", "rider", "driver"]
