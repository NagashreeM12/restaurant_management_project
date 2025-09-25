# urls.py

from django.urls import path
from .views import RideRequestView, AvailableRidesView, AcceptRideView

urlpatterns = [
    path('ride/request/', RideRequestView.as_view(), name='ride-request'),
    path('ride/available/', AvailableRidesView.as_view(), name='available-rides'),
    path('ride/accept/<int:ride_id>/', AcceptRideView.as_view(), name='accept-ride'),
]
