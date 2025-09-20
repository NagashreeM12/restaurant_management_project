# menu/views.py
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from .models import MenuItem
from .serializers import MenuItemSerializer

class MenuItemPagination(PageNumberPagination):
    page_size = 10  # default items per page
    page_size_query_param = 'page_size'
    max_page_size = 50

class MenuItemSearchViewSet(viewsets.ViewSet):
    pagination_class = MenuItemPagination

    def list(self, request):
        query = request.query_params.get('q', '')  # search query
        items = MenuItem.objects.filter(name__icontains=query)

        # Apply pagination
        paginator = self.pagination_class()
        page = paginator.paginate_queryset(items, request)
        serializer = MenuItemSerializer(page, many=True)

        return paginator.get_paginated_response(serializer.data)
