# models.py
# models.py
# home/models.py
from django.db import models

class MenuCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

