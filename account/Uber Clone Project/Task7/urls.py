# urls.py

from django.urls import path
from .views import CompleteRideView, CancelRideView

urlpatterns = [
    path('ride/complete/<int:ride_id>/', CompleteRideView.as_view(), name='complete-ride'),
    path('ride/cancel/<int:ride_id>/', CancelRideView.as_view(), name='cancel-ride'),
]
