from django.urls import path
from .views import OpeningHoursListAPIView

urlpatterns = [
    path('api/opening-hours/', OpeningHoursListAPIView.as_view(), name='opening-hours-list'),
]
