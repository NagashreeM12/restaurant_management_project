from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    # ✅ New field
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name

