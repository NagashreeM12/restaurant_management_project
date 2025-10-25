# models.py
# models.py
# home/models.py
from django.db import models
from django.db.models import Count

class MenuItemManager(models.Manager):
    def get_top_selling_items(self, num_items=5):
        return (
            self.get_queryset()
            .annotate(order_count=Count('orderitem'))
            .order_by('-order_count')[:num_items]
        )
