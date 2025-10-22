# home/views.py
from rest_framework import generics, permissions
from .models import UserReview
from .serializers import UserReviewSerializer

# Create a new review
class UserReviewCreateView(generics.CreateAPIView):
    queryset = UserReview.objects.all()
    serializer_class = UserReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# Retrieve reviews for a specific menu item
class MenuItemReviewListView(generics.ListAPIView):
    serializer_class = UserReviewSerializer

    def get_queryset(self):
        menu_item_id = self.kwargs.get('menu_item_id')
        return UserReview.objects.filter(menu_item_id=menu_item_id)
