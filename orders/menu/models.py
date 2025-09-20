# menu/models.py
# menu/models.py
from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.category_name


class MenuItem(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="menu_items")

    def __str__(self):
        return self.name
