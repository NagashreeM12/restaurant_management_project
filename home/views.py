from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Order
from .serializers import OrderStatusSerializer

class OrderStatusAPIView(generics.RetrieveAPIView):
    """
    GET API endpoint to retrieve the status of an order by unique_id.
    """
    serializer_class = OrderStatusSerializer
    lookup_field = 'unique_id'
    queryset = Order.objects.all()

    def get(self, request, *args, **kwargs):
        try:
            return self.retrieve(request, *args, **kwargs)
        except Order.DoesNotExist:
            return Response({"detail": "Order not found."}, status=status.HTTP_404_NOT_FOUND)
