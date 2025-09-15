from django.db import models
from home.models import MenuCategory   # if you use it
# Import OrderStatus
from .models import OrderStatus   # if in same app
# OR: from orders.models import OrderStatus (if OrderStatus is in same file, no need)

class Order(models.Model):
    # your existing fields here...
    customer_name = models.CharField(max_length=100)
    order_date = models.DateTimeField(auto_now_add=True)

    # New field for order status
    status = models.ForeignKey(
        "orders.OrderStatus",   # safer to use string reference
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="orders"
    )

    def __str__(self):
        return f"Order {self.id} - {self.customer_name}"
