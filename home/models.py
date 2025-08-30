# models.py
# models.py
from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    logo = models.ImageField(upload_to='restaurant_logos/', null=True, blank=True)  # Logo image field

    def __str__(self):
        return self.name

