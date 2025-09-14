from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Rider, Driver


# Rider Serializer
class RiderRegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Rider
        fields = ['username', 'email', 'password', 'phone_number', 'preferred_payment_method', 'default_pickup_location']

    def create(self, validated_data):
        username = validated_data.pop('username')
        email = validated_data.pop('email')
        password = validated_data.pop('password')

        user = User.objects.create_user(username=username, email=email, password=password)
        rider = Rider.objects.create(user=user, **validated_data)
        return rider


# Driver Serializer
class DriverRegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Driver
        fields = [
            'username', 'email', 'password',
            'phone_number', 'driver_license_number',
            'vehicle_make', 'vehicle_model', 'license_plate',
            'availability_status'
        ]

    def create(self, validated_data):
        username = validated_data.pop('username')
        email = validated_data.pop('email')
        password = validated_data.pop('password')

        user = User.objects.create_user(username=username, email=email, password=password)
        driver = Driver.objects.create(user=user, **validated_data)
        return driver
