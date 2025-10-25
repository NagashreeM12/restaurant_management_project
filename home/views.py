from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import MenuItem
from .serializers import MenuItemSearchSerializer

class MenuItemSearchAPIView(generics.ListAPIView):
    """
    GET API endpoint to search for menu items by name (case-insensitive).
    """
    serializer_class = MenuItemSearchSerializer

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        if query:
            return MenuItem.objects.filter(name__icontains=query)
        return MenuItem.objects.none()
