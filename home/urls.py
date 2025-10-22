# urls.py
# home/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuCategoryViewSet

router = DefaultRouter()
router.register(r'categories', MenuCategoryViewSet, basename='menu-category')

urlpatterns = [
    path('', include(router.urls)),
]
