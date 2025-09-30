from django.db import models


class ActiveOrderManager(models.Manager):
    def get_active_orders(self):
        """
        Return only orders with status 'pending' or 'processing'.
        """
        return self.filter(status__in=['pending', 'processing'])



