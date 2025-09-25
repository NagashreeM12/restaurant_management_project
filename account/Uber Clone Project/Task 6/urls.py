# urls.py

from django.urls import path
from .views import UpdateDriverLocationView, TrackDriverLocationView

urlpatterns = [
    path('ride/update-location/', UpdateDriverLocationView.as_view(), name='update-driver-location'),
    path('ride/track/<int:ride_id>/', TrackDriverLocationView.as_view(), name='track-driver-location'),
]
