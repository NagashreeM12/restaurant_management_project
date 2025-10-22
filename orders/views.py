from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Order

@api_view(['GET'])
def order_status_view(request, order_id):
    """
    Retrieve the current status of an order given its ID.
    """
    try:
        order = Order.objects.get(id=order_id)
        return Response({
            "order_id": order.id,
            "status": order.status
        }, status=status.HTTP_200_OK)
    except Order.DoesNotExist:
        return Response({
            "error": f"Order with ID {order_id} not found."
        }, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({
            "error": f"An unexpected error occurred: {str(e)}"
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
