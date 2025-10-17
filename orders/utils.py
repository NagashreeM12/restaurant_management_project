from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Order
from home.utils import send_custom_email  # Import the utility

class CancelOrderView(APIView):
    def delete(self, request, order_id):
        try:
            order = Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            return Response({"error": "Order not found."}, status=status.HTTP_404_NOT_FOUND)

        if order.status in ['Completed', 'Cancelled']:
            return Response({"message": f"Cannot cancel a {order.status.lower()} order."},
                            status=status.HTTP_400_BAD_REQUEST)

        order.status = 'Cancelled'
        order.save()

        # Send notification email
        email_response = send_custom_email(
            to_email="customer@example.com",
            subject=f"Order #{order.id} Cancelled",
            message=f"Dear {order.customer_name}, your order #{order.id} has been cancelled successfully."
        )

        return Response({
            "message": "Order cancelled successfully.",
            "email_status": email_response
        }, status=status.HTTP_200_OK)
