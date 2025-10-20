# models.py
# models.py
# home/models.py
from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_daily_special = models.BooleanField(default=False)  # NEW FIELD

    def __str__(self):
        return self.name
