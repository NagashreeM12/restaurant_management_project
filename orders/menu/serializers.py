# menu/serializers.py
# menu/serializers.py
from rest_framework import serializers
from .models import MenuItem

class MenuItemSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()  # shows category name instead of ID

    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'price', 'description', 'category']

