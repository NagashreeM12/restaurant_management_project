from django.db import models
from django.contrib.auth.models import User
from products.models import Menu
# Create your models here.
class Order(models.Model):
    STATUS_CHOICES=[
        ('PENDING','Pending'),
        ('CONFIRMED','Confirmed'),
        ('CANCELLED','Cancelled'),
        ('DELIVERED','Delivered'),
    ]
    customer=models.ForeignKey(User,on_delete=models.CASCADE)#Link to User
    order_items=models.ManyToManyField(Menu,through='OrderItem')
    total_amount=models.DecimalField(max_digits=8,decimal_places=2)
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default='PENDING')
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Order {self.id} by {self.customer.username}-{self.status}"
#Intermediate table for order items
class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    menu_item=models.ForeignKey(Menu,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    def __str__(self):
        return f"{self.quantity} x {self.menu_item.name}"