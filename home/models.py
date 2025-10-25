# models.py
# models.py
# home/models.py
from django.db import models
from datetime import datetime, timedelta

class Reservation(models.Model):
    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=255)
    reservation_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    party_size = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.customer_name} at {self.restaurant.name} on {self.reservation_date}"
