# orders/models.py
from django.db import models

class OrderManager(models.Manager):
    """Custom manager for Order model."""

    def with_status(self, status):
        """
        Retrieve all orders with a specific status.
        Example usage: Order.objects.with_status('pending')
        """
        return self.filter(status=status)

    def pending(self):
        """Shortcut method to get all pending orders."""
        return self.filter(status='pending')

    def completed(self):
        """Shortcut method to get all completed orders."""
        return self.filter(status='completed')

    def cancelled(self):
        """Shortcut method to get all cancelled orders."""
        return self.filter(status='cancelled')


class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    order_id = models.CharField(max_length=20, unique=True)
    customer_name = models.CharField(max_length=100)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    # Attach the custom manager
    objects = OrderManager()

    def __str__(self):
        return f"{self.order_id} - {self.status}"
