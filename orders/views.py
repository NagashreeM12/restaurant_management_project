# orders/views.py
# orders/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Order
from .serializers import OrderSerializer

class CancelOrderView(APIView):
    """
    API endpoint to cancel an order by ID.
    """

    def delete(self, request, order_id):
        try:
            order = Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            return Response({"error": "Order not found."}, status=status.HTTP_404_NOT_FOUND)

        if order.status in ['Completed', 'Cancelled']:
            return Response({"message": f"Cannot cancel a {order.status.lower()} order."},
                            status=status.HTTP_400_BAD_REQUEST)

        # Update status
        order.status = 'Cancelled'
        order.save()

        serializer = OrderSerializer(order)
        return Response({"message": "Order cancelled successfully.", "order": serializer.data},
                        status=status.HTTP_200_OK)
