# views.py

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Driver, Ride
from .serializers import DriverLocationUpdateSerializer, DriverLocationSerializer


class UpdateDriverLocationView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            driver = get_object_or_404(Driver, user=request.user)
        except:
            return Response({"error": "Only drivers can update location"}, status=status.HTTP_403_FORBIDDEN)

        serializer = DriverLocationUpdateSerializer(driver, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Location updated successfully"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TrackDriverLocationView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, ride_id):
        ride = get_object_or_404(Ride, id=ride_id)

        # Security check → Only rider of this ride (or driver/admin) can view
        if ride.rider != request.user and ride.driver.user != request.user:
            return Response({"error": "Not authorized"}, status=status.HTTP_403_FORBIDDEN)

        # Ensure ride is ongoing
        if ride.status != "ONGOING":
            return Response({"error": "Ride not active"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = DriverLocationSerializer(ride.driver)
        return Response(serializer.data)
