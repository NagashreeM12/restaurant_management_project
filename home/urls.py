# urls.py
# urls.py
from django.urls import path
from .views import TableDetailView

urlpatterns = [
    # existing URLs...
    path('api/tables/<int:pk>/', TableDetailView.as_view(), name='table-detail'),
]


