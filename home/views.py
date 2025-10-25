from rest_framework import generics
from .models import MenuCategory
from .serializers import MenuCategorySerializer

class MenuCategoryListAPIView(generics.ListAPIView):
    """
    GET API endpoint to list all menu categories.
    """
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer
