from django.contrib import admin
from .models import RestaurantAddress
# Register your models here.
class RestaurantAddressAdmin(admin.ModelAdmin):
    list_display=("street","city","state","zipcode")
