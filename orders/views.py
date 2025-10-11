# orders/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from .models import Coupon
from .serializers import CouponSerializer

class CouponValidationView(APIView):
    def post(self, request):
        code = request.data.get('code')

        if not code:
            return Response({'error': 'Coupon code is required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            coupon = Coupon.objects.get(code=code)
        except Coupon.DoesNotExist:
            return Response({'error': 'Invalid coupon code.'}, status=status.HTTP_400_BAD_REQUEST)

        # Validate coupon status and date range
        today = timezone.now().date()
        if not coupon.is_active:
            return Response({'error': 'This coupon is not active.'}, status=status.HTTP_400_BAD_REQUEST)
        if today < coupon.valid_from or today > coupon.valid_until:
            return Response({'error': 'This coupon is expired or not yet valid.'}, status=status.HTTP_400_BAD_REQUEST)

        # If valid, return success response
        return Response({
            'success': True,
            'code': coupon.code,
            'discount_percentage': coupon.discount_percentage
        }, status=status.HTTP_200_OK)

