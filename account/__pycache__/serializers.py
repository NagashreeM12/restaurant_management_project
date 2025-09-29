from django.contrib.auth.models import User
from rest_framework import serializers

class UserProfileUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer to update user profile fields.
    Only allows updating selected fields like first_name, last_name, email.
    """

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]
        extra_kwargs = {
            "email": {"required": True}
        }
