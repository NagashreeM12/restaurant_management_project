# orders/urls.py
# orders/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('<int:order_id>/update-status/', views.update_order_status, name='update-order-status'),
]
