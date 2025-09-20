# menu/views.py
# menu/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import MenuItem
from .serializers import MenuItemSerializer

class MenuItemsByCategoryView(APIView):
    def get(self, request):
        category_name = request.query_params.get('category', None)

        if not category_name:
            return Response({"error": "Category parameter is required"}, status=400)

        items = MenuItem.objects.filter(category__category_name__iexact=category_name)
        serializer = MenuItemSerializer(items, many=True)
        return Response(serializer.data)

