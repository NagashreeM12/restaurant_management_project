from rest_framework import generics
from .models import MenuItem
from .serializers import IngredientSerializer

class MenuItemIngredientsList(generics.RetrieveAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = IngredientSerializer

    def get(self, request, *args, **kwargs):
        menu_item = self.get_object()
        ingredients = menu_item.ingredients.all()
        serializer = IngredientSerializer(ingredients, many=True)
        return Response(serializer.data)

