from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Ride(models.Model):
    STATUS_CHOICES = [
        ('REQUESTED', 'Requested'),
        ('ONGOING', 'Ongoing'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]

    rider = models.ForeignKey(User, on_delete=models.CASCADE, related_name="rides_as_rider")
    driver = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="rides_as_driver")
    pickup = models.CharField(max_length=255)
    drop = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="REQUESTED")
    requested_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pickup} → {self.drop} ({self.status})"


class RideFeedback(models.Model):
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE, related_name="feedbacks")
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(blank=True)
    is_driver = models.BooleanField()  # True = driver submitted, False = rider submitted
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('ride', 'is_driver')  # One feedback per user-role per ride

    def __str__(self):
        role = "Driver" if self.is_driver else "Rider"
        return f"{role} feedback for Ride {self.ride.id}"
