from rest_framework import generics
from .models import MenuItem
from .serializers import MenuItemSerializer

class FeaturedMenuItemList(generics.ListAPIView):
    queryset = MenuItem.objects.filter(is_featured=True)
    serializer_class = MenuItemSerializer

