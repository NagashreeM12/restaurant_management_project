from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Order
from .serializers import OrderStatusUpdateSerializer

@api_view(['POST'])
def update_order_status(request):
    """
    API endpoint to update an order's status.
    Expected JSON:
    {
        "order_id": "ORD123",
        "status": "Delivered"
    }
    """
    serializer = OrderStatusUpdateSerializer(data=request.data)

    if serializer.is_valid():
        order_id = serializer.validated_data['order_id']
        new_status = serializer.validated_data['status']

        try:
            order = Order.objects.get(order_id=order_id)
        except Order.DoesNotExist:
            return Response(
                {"error": f"Order with ID '{order_id}' not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        # Update order status
        order.status = new_status
        order.save()

        return Response(
            {
                "message": "Order status updated successfully.",
                "order_id": order.order_id,
                "new_status": order.status,
            },
            status=status.HTTP_200_OK,
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
