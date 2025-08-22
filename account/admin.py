from django.contrib import admin
from .models import Menu,Order
# Register your models here.
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display=('name','description','price')
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=('customer_name','dish','quantity','created_at')
