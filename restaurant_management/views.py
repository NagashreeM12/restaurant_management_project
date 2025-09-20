# users/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from utils.validation_utils import is_valid_email

class EmailCheckView(APIView):
    def post(self, request):
        email = request.data.get("email")
        if not email:
            return Response({"error": "Email is required"}, status=400)

        if is_valid_email(email):
            return Response({"message": "Valid email"}, status=200)
        else:
            return Response({"error": "Invalid email address"}, status=400)
