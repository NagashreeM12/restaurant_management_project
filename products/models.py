from django.db import models
class Menu(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    price=models.DecimalField(max_digits=6,decimal_place=2)
    def __str__(self):
        return self.name
class Order(models.Model):
    customer_name=models.CharField(max_length=100)
    dish=models.ForeignKey(Menu,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Order by {self.customer_name}-{self.dish.name}"