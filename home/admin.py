from django.contrib import admin
from .models import Restaurant

class RestaurantAdmin(admin.ModelAdmin):
    # ✅ Show important fields in list view
    list_display = ('name', 'address', 'phone_number', 'email', 'is_active')

    # ✅ Enable search by name and address
    search_fields = ('name', 'address')

    # ✅ Filter by active status (only if field exists in model)
    list_filter = ('is_active',)

# ✅ Register with Admin site
admin.site.register(Restaurant, RestaurantAdmin)
