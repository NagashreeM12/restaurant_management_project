# rides/serializers.py
from rest_framework import serializers
from .models import Ride
from .utils import calculate_distance
from decimal import Decimal

class FareCalculationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = ["id", "fare", "status"]

    def update(self, instance, validated_data):
        # Prevent fare calculation if ride not completed
        if instance.status != "COMPLETED":
            raise serializers.ValidationError("Fare can only be calculated for completed rides.")

        # Prevent re-calculation if fare already set
        if instance.fare is not None:
            raise serializers.ValidationError("Fare already calculated for this ride.")

        # Constants
        base_fare = Decimal("50.00")
        per_km_rate = Decimal("10.00")
        surge_multiplier = Decimal(str(self.context.get("surge_multiplier", 1.0)))

        # Distance in km
        distance = Decimal(str(calculate_distance(
            instance.pickup_lat, instance.pickup_lon,
            instance.drop_lat, instance.drop_lon
        ))).quantize(Decimal("0.01"))  # round to 2 decimal places

        # Fare calculation
        fare = base_fare + (distance * per_km_rate * surge_multiplier)

        # Save fare
        instance.fare = fare.quantize(Decimal("0.01"))
        instance.save()

        return instance
