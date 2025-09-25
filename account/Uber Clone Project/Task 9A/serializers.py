from rest_framework import serializers
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import Ride, RideFeedback


class RideFeedbackSerializer(serializers.ModelSerializer):
    rating = serializers.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    comment = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = RideFeedback
        fields = ['ride', 'rating', 'comment', 'is_driver']

        # ride field will be set in the view, not directly from request body
        extra_kwargs = {
            'ride': {'read_only': True},
            'is_driver': {'read_only': True},
        }

    def validate(self, data):
        """Custom validation for feedback rules."""
        user = self.context['request'].user
        ride = self.context.get('ride')  # ride is passed from view

        if not ride:
            raise serializers.ValidationError("Ride not found.")

        # Ensure user belongs to the ride
        if ride.rider != user and ride.driver != user:
            raise serializers.ValidationError("You are not part of this ride.")

        # Ensure ride is completed
        if ride.status != "COMPLETED":
            raise serializers.ValidationError("Ride is not completed yet.")

        # Ensure user hasn’t already submitted feedback
        is_driver = (ride.driver == user)
        if RideFeedback.objects.filter(ride=ride, is_driver=is_driver).exists():
            raise serializers.ValidationError("Feedback already submitted.")

        data['ride'] = ride
        data['is_driver'] = is_driver
        return data
