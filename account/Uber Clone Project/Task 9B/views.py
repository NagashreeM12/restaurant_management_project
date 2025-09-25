from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Ride, RideFeedback
from .serializers import RideFeedbackSerializer

class SubmitRideFeedbackView(APIView):
    """
    POST /api/ride/feedback/<ride_id>/
    Allows rider or driver to submit feedback after a ride is COMPLETED.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, ride_id):
        # Step 1: Validate ride exists
        ride = get_object_or_404(Ride, id=ride_id)

        # Step 2: Check if ride is completed
        if ride.status != "COMPLETED":
            return Response({"error": "Ride is not completed yet."}, status=status.HTTP_400_BAD_REQUEST)

        # Step 3: Check user is part of this ride
        user = request.user
        if user != ride.rider and user != ride.driver:
            return Response({"error": "You are not part of this ride."}, status=status.HTTP_403_FORBIDDEN)

        # Step 4: Determine if user is driver or rider
        is_driver = (user == ride.driver)

        # Step 5: Check if feedback already submitted
        if RideFeedback.objects.filter(ride=ride, is_driver=is_driver).exists():
            return Response({"error": "You have already submitted feedback for this ride."}, status=status.HTTP_400_BAD_REQUEST)

        # Step 6: Serialize and save feedback
        serializer = RideFeedbackSerializer(data=request.data, context={'request': request, 'ride': ride})
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Feedback submitted successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
