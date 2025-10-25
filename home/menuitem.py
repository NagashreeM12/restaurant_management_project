class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_featured = models.BooleanField(default=False)

    # ✅ Attach the custom manager here
    objects = MenuItemManager()

    def __str__(self):
        return self.name
