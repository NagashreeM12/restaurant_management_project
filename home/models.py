# models.py
from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)  # Add phone number field

    def __str__(self):
        return self.name
