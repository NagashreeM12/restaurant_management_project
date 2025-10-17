class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    unique_id = models.CharField(max_length=20, unique=True, blank=True)  # Add this field
    customer_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def save(self, *args, **kwargs):
        if not self.unique_id:
            from .utils import generate_unique_order_id
            self.unique_id = generate_unique_order_id(length=8)
        super().save(*args, **kwargs)

    def calculate_total(self):
        total = sum(item.price * item.quantity for item in self.items.all())
        return total

    def __str__(self):
        return f"Order {self.unique_id} ({self.status})"
