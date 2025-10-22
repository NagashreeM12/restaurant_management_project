# models.py
# models.py
# home/models.py
from django.db import models
from django.contrib.auth.models import User  # Import the User model
from .models import MenuCategory  # (if you have MenuItem in same file, ignore this line)

# Assuming you already have a MenuItem model defined somewhere
# If not, replace 'MenuItem' with your actual menu item model name
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey('MenuCategory', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name


class UserReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField()
    comment = models.TextField()
    review_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.menu_item.name} ({self.rating}/5)"
