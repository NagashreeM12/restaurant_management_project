from rest_framework import generics, permissions
from .models import Ride
from .serializers import RideHistorySerializer

class RiderHistoryView(generics.ListAPIView):
    serializer_class = RideHistorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Ride.objects.filter(
            rider=self.request.user,
            status__in=["COMPLETED", "CANCELLED"]
        ).order_by("-requested_at")


class DriverHistoryView(generics.ListAPIView):
    serializer_class = RideHistorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Ride.objects.filter(
            driver=self.request.user,
            status__in=["COMPLETED", "CANCELLED"]
        ).order_by("-requested_at")
