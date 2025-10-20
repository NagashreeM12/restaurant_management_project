# home/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import MenuItem
from .serializers import MenuItemSerializer

@api_view(['GET'])
def daily_specials(request):
    """Retrieve all menu items marked as daily specials."""
    specials = MenuItem.objects.filter(is_daily_special=True)
    serializer = MenuItemSerializer(specials, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

