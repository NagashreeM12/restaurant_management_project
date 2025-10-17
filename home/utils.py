# home/utils.py
from django.core.mail import send_mail, BadHeaderError
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.conf import settings

def send_custom_email(to_email, subject, message):
    """
    Utility function to send an email.
    Args:
        to_email (str): Recipient's email address
        subject (str): Subject line
        message (str): Body of the email
    """
    try:
        # Validate email
        validate_email(to_email)

        # Send email
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[to_email],
            fail_silently=False,
        )
        return {"success": True, "message": "Email sent successfully."}

    except ValidationError:
        return {"success": False, "error": "Invalid email address."}

    except BadHeaderError:
        return {"success": False, "error": "Invalid header found."}

    except Exception as e:
        return {"success": False, "error": str(e)}
