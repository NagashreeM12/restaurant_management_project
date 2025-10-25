# models.py
# models.py
# home/models.py
from django.db import models

class OpeningHour(models.Model):
    DAYS_OF_WEEK = [
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Thu', 'Thursday'),
        ('Fri', 'Friday'),
        ('Sat', 'Saturday'),
        ('Sun', 'Sunday'),
    ]

    day = models.CharField(max_length=3, choices=DAYS_OF_WEEK, unique=True)
    open_time = models.TimeField()
    close_time = models.TimeField()

    def __str__(self):
        return f"{self.get_day_display()}: {self.open_time} - {self.close_time}"
