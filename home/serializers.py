# home/serializersfrom rest_framework import serializers
from rest_framework import serializers
from .models import MenuItem

class MenuItemAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'is_available']
