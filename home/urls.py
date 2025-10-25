from django.urls import path
from .views import MenuItemAvailabilityUpdateAPIView

urlpatterns = [
    path('api/menu-items/<int:id>/availability/', MenuItemAvailabilityUpdateAPIView.as_view(), name='menuitem-availability-update'),
]
