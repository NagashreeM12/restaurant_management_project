from django.urls import path
from .views import add_to_cart, cart_count

urlpatterns = [
    path('add_to_cart/<int:item_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart_count, name='cart_count'),
]

