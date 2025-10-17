import secrets
import string
from .models import Order

def generate_unique_order_id(length=8):
    """
    Generates a unique alphanumeric order ID.
    Ensures that the generated ID does not already exist in the database.
    
    Args:
        length (int): Length of the generated ID (default is 8)
    
    Returns:
        str: A unique order ID
    """
    characters = string.ascii_uppercase + string.digits  # e.g., ABC123
    while True:
        order_id = ''.join(secrets.choice(characters) for _ in range(length))
        if not Order.objects.filter(unique_id=order_id).exists():
            return order_id

