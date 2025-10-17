# home/serializers.py
from rest_framework import serializers
from .models import ContactFormSubmission

class ContactFormSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactFormSubmission
        fields = ['id', 'name', 'email', 'message', 'created_at']
