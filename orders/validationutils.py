# utils/validation_utils.py
from email_validator import validate_email, EmailNotValidError
import logging

logger = logging.getLogger(__name__)

def is_valid_email(email: str) -> bool:
    """
    Validate an email address.
    
    Args:
        email (str): The email address to validate.
    
    Returns:
        bool: True if email is valid, False otherwise.
    """
    try:
        # validate_email will raise an exception if invalid
        validate_email(email)
        return True
    except EmailNotValidError as e:
        logger.warning(f"Invalid email attempted: {email} | Reason: {e}")
        return False
