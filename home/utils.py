# home/utils.py
from home.models import MenuItem

def get_distinct_cuisines():
    """
    Returns a list of unique cuisine names across all MenuItem instances.
    
    Example:
        ['Italian', 'Indian', 'Mexican']
    """
    # Query related Cuisine names and get distinct values
    cuisines = MenuItem.objects.values_list('cuisine__name', flat=True).distinct()
    return list(cuisines)
