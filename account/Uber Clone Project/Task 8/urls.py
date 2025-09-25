from django.urls import path
from .views import RiderHistoryView, DriverHistoryView

urlpatterns = [
    path("api/rider/history/", RiderHistoryView.as_view(), name="rider-history"),
    path("api/driver/history/", DriverHistoryView.as_view(), name="driver-history"),
]
