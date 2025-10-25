# home/utils.py
import re

def is_valid_email(email):
    """
    Validates an email address using a regular expression.

    Args:
        email (str): Email address to validate.

    Returns:
        bool: True if email is valid, False otherwise.
    """
    if not isinstance(email, str):
        return False

    # Basic regex pattern for validating emails
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))
