from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .serializers import UserProfileUpdateSerializer

class UserProfileUpdateView(generics.UpdateAPIView):
    """
    API endpoint that allows a logged-in user to update their profile.
    """
    serializer_class = UserProfileUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # Always return the currently logged-in user
        return self.request.user
