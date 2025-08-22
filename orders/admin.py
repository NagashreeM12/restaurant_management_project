from django.contrib import admin
from .models import Order,OrderItem
# Register your models here.
class OrderItemInline(admin.TabularInline):
    model=OrderItem
    extra=1
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=('id','customer','total_amount','status','created_at')
    list_filter=('status','created_at')
    inlines=[OrderItemInline]
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display=('order','menu_item',''quantify')
