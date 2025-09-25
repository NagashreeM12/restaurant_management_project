# views.py

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Ride, Driver
from .serializers import RideRequestSerializer, RideDetailSerializer


class RideRequestView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = RideRequestSerializer(data=request.data)
        if serializer.is_valid():
            ride = serializer.save(rider=request.user, status="REQUESTED")
            return Response(RideDetailSerializer(ride).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AvailableRidesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        rides = Ride.objects.filter(status="REQUESTED", driver__isnull=True)
        serializer = RideDetailSerializer(rides, many=True)
        return Response(serializer.data)


class AcceptRideView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, ride_id):
        ride = get_object_or_404(Ride, id=ride_id)

        # Ensure only drivers can accept
        driver = get_object_or_404(Driver, user=request.user)

        if ride.status != "REQUESTED" or ride.driver is not None:
            return Response({"error": "Ride already accepted."}, status=status.HTTP_400_BAD_REQUEST)

        ride.driver = driver
        ride.status = "ONGOING"
        ride.save()

        return Response({"message": "Ride accepted successfully.", "ride": RideDetailSerializer(ride).data})
