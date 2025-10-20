from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Order
from .serializers import OrderStatusUpdateSerializer

@api_view(['PUT'])
def update_order_status(request, order_id):
    """
    API endpoint to update an existing order's status.
    URL: /orders/<order_id>/update-status/
    """
    try:
        order = Order.objects.get(id=order_id)
    except Order.DoesNotExist:
        return Response(
            {"error": f"Order with ID {order_id} not found."},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = OrderStatusUpdateSerializer(order, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {
                "message": "Order status updated successfully.",
                "order_id": order.id,
                "new_status": serializer.data['status']
            },
            status=status.HTTP_200_OK
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
