from django.urls import path
from .views import FeaturedMenuItemList

urlpatterns = [
    path('featured-menu/', FeaturedMenuItemList.as_view(), name='featured-menu'),
]
