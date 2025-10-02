# rides/views.py
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Ride
from .serializers import FareCalculationSerializer

class CalculateFareView(generics.UpdateAPIView):
    queryset = Ride.objects.all()
    serializer_class = FareCalculationSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        # Example: Surge multiplier based on peak hours
        context["surge_multiplier"] = 1.5 if self.request.query_params.get("peak") == "true" else 1.0
        return context
