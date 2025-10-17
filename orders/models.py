# home/models.py
# orders/models.py
from django.db import models
from decimal import Decimal
from home.models import MenuItem  # Import your MenuItem model

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def calculate_total(self):
        """
        Calculate the total cost of this order based on all related order items.
        """
        total = Decimal('0.00')
        for item in self.items.all():  # 'items' is the related_name in OrderItem
            total += item.price * item.quantity
        return total

    def __str__(self):
        return f"Order #{self.id} by {self.customer_name}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2)  # Store price at time of order

    def __str__(self):
        return f"{self.menu_item.name} x {self.quantity}"
