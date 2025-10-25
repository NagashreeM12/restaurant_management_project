from django.urls import path
from .views import RestaurantInfoAPIView

urlpatterns = [
    path('api/restaurant-info/', RestaurantInfoAPIView.as_view(), name='restaurant-info'),
]
