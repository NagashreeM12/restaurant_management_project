from rest_framework import generics
from .models import Restaurant
from .serializers import RestaurantSerializer

class RestaurantInfoAPIView(generics.ListAPIView):
    """
    GET API endpoint to retrieve all restaurant information.
    """
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

