# rides/models.py
from django.db import models
from django.contrib.auth.models import User

class Ride(models.Model):
    rider = models.ForeignKey(User, on_delete=models.CASCADE, related_name="rides")
    driver = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="drives")
    pickup_lat = models.FloatField()
    pickup_lon = models.FloatField()
    drop_lat = models.FloatField()
    drop_lon = models.FloatField()
    status = models.CharField(max_length=20, choices=[("REQUESTED", "Requested"),
                                                      ("ONGOING", "Ongoing"),
                                                      ("COMPLETED", "Completed")])
    fare = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
