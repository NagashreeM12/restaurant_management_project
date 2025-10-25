# home/serializersfrom rest_framework import serializers
from rest_framework import serializers
from .models import OpeningHour

class OpeningHourSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpeningHour
        fields = ['day', 'open_time', 'close_time']
