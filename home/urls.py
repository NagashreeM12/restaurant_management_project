from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuCategoryViewSet

router = DefaultRouter()
router.register(r'menu-categories', MenuCategoryViewSet, basename='menu-category')

urlpatterns = [
    path('api/', include(router.urls)),
]
