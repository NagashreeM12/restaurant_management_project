from rest_framework import generics, status
from rest_framework.response import Response
from .models import MenuItem
from .serializers import MenuItemAvailabilitySerializer

class MenuItemAvailabilityUpdateAPIView(generics.UpdateAPIView):
    """
    API endpoint to update availability of a menu item.
    """
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemAvailabilitySerializer
    lookup_field = 'id'

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
