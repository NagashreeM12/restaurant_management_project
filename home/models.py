# models.py
# models.py
# home/models.py
class Ingredient(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    ingredients = models.ManyToManyField(Ingredient, related_name='menu_items')

    def __str__(self):
        return self.name
