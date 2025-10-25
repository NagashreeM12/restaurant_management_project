# models.py
# models.py
# home/models.py
from django.db import models
import random

class DailySpecial(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    # ✅ Static method to get a random daily special
    @staticmethod
    def get_random_special():
        specials = DailySpecial.objects.filter(available=True)
        if not specials.exists():
            return None
        return specials.order_by('?').first()

from home.models import DailySpecial

special_of_the_day = DailySpecial.get_random_special()
if special_of_the_day:
    print(special_of_the_day.name)
else:
    print("No daily specials available today.")
