from django.contrib import admin
from .models import UserReview, MenuItem, MenuCategory

admin.site.register(UserReview)
admin.site.register(MenuItem)
admin.site.register(MenuCategory)
