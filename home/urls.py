from django.urls import path
from .views import MenuItemSearchAPIView

urlpatterns = [
    path('api/menu-items/search/', MenuItemSearchAPIView.as_view(), name='menuitem-search'),
]
