# menu/urls.py
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import MenuItemSearchViewSet

router = DefaultRouter()
router.register(r'menu/search', MenuItemSearchViewSet, basename='menu-search')

urlpatterns = router.urls
