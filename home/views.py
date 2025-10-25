from rest_framework import generics
from .models import OpeningHour
from .serializers import OpeningHourSerializer

class OpeningHoursListAPIView(generics.ListAPIView):
    """
    GET API endpoint to retrieve restaurant opening hours.
    """
    queryset = OpeningHour.objects.all().order_by('day')
    serializer_class = OpeningHourSerializer
