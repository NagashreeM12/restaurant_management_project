from django.db import models

class RestaurantAddress(models.Model):
    name=models.CharField(max_length=150,default="My Restaurant")
    address=models.TextField()
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zipcode=models.CharField(max_length=100)
    def __str__(self):
        return  f"{self.street},{self.city},{self.state}-{self.zipcode}"