# menu/urls.py
# menu/urls.py
from django.urls import path
from .views import MenuItemViewSet

menu_item_update = MenuItemViewSet.as_view({'put': 'update'})

urlpatterns = [
    path('menu-items/<int:pk>/update/', menu_item_update, name='menu-item-update'),
]

