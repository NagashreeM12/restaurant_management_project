# urls.py
from django.urls import path
from .views import AvailableTablesAPIView

urlpatterns = [
    # other API routes...
    path('api/tables/available/', AvailableTablesAPIView.as_view(), name='available_tables_api'),
]
