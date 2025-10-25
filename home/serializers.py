# home/serializersfrom rest_framework import serializers
from rest_framework import serializers
from .models import MenuItem

class MenuItemSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'image']
