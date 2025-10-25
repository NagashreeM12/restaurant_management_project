# models.py
# models.py
# home/models.py
from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount_percentage = models.FloatField(default=0)  # discount in percent
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_final_price(self):
        """
        Calculates the final price after applying discount.
        Returns:
            float: discounted price rounded to 2 decimals
        """
        if self.discount_percentage < 0 or self.discount_percentage > 100:
            # Invalid discount, ignore it
            return float(self.price)
        discount_amount = (self.discount_percentage / 100) * float(self.price)
        final

