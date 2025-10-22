# urls.py
# home/urls.py
from django.urls import path
from .views import UserReviewCreateView, MenuItemReviewListView

urlpatterns = [
    path('reviews/create/', UserReviewCreateView.as_view(), name='create-review'),
    path('reviews/menu-item/<int:menu_item_id>/', MenuItemReviewListView.as_view(), name='menu-item-reviews'),
]
