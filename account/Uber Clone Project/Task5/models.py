# models.py

from django.db import models
from django.contrib.auth.models import User


class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    current_latitude = models.FloatField(null=True, blank=True)
    current_longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.user.username


class Ride(models.Model):
    STATUS_CHOICES = [
        ('REQUESTED', 'Requested'),
        ('ONGOING', 'Ongoing'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]

    rider = models.ForeignKey(User, on_delete=models.CASCADE, related_name="rides")
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, blank=True, related_name="rides")

    pickup_address = models.CharField(max_length=255)
    dropoff_address = models.CharField(max_length=255)
    pickup_lat = models.FloatField()
    pickup_lng = models.FloatField()
    drop_lat = models.FloatField()
    drop_lng = models.FloatField()

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="REQUESTED")
    requested_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Ride {self.id} - {self.status}"
