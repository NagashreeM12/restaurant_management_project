# views.py

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Ride, Driver


class CompleteRideView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, ride_id):
        ride = get_object_or_404(Ride, id=ride_id)

        # Only the driver of this ride can complete
        if ride.driver.user != request.user:
            return Response({"error": "Only the assigned driver can complete this ride."},
                            status=status.HTTP_403_FORBIDDEN)

        # Ride must be ongoing
        if ride.status != "ONGOING":
            return Response({"error": "Only ongoing rides can be completed."},
                            status=status.HTTP_400_BAD_REQUEST)

        # Mark as completed
        ride.status = "COMPLETED"
        ride.save()
        return Response({"message": "Ride marked as completed."}, status=status.HTTP_200_OK)


class CancelRideView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, ride_id):
        ride = get_object_or_404(Ride, id=ride_id)

        # Only the rider who booked the ride can cancel
        if ride.rider != request.user:
            return Response({"error": "Only the rider who booked can cancel this ride."},
                            status=status.HTTP_403_FORBIDDEN)

        # Can only cancel if still requested
        if ride.status != "REQUESTED":
            return Response({"error": "Cannot cancel a ride that is already ongoing or completed."},
                            status=status.HTTP_400_BAD_REQUEST)

        # Mark as cancelled
        ride.status = "CANCELLED"
        ride.save()
        return Response({"message": "Ride cancelled successfully."}, status=status.HTTP_200_OK)
