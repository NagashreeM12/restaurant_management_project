import string
import secrets
from .models import Coupon  # Assuming you have a Coupon model

def generate_coupon_code(length=10):
    """
    Generate a unique alphanumeric coupon code.
    Ensures the generated code does not already exist in the database.
    """
    characters = string.ascii_uppercase + string.digits  # A-Z, 0-9

    while True:
        code = ''.join(secrets.choice(characters) for _ in range(length))
        if not Coupon.objects.filter(code=code).exists():
            return code
