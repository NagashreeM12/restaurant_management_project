# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_count, name='cart_count'),  # Homepage with cart count
    path('add_to_cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),  # Add item to cart
]


