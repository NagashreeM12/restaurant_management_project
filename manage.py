#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from django.db import models
class RestaurantLocation(models.Model):
    #Street address of the restaurant
    address=models.CharField(max_length=255)
    #City name
    city=models.CharField(max_length=100)
    #state name
    state=models.CharField(max_length=100)
    #Zip/postal code
    zipcode=models.CharField(max_length=20)
    def __str__(self):
        return f"{self.address},{self.city},{self.state}-{self.zipcode}"
