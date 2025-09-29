from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
import logging

# Get Django's logger
logger = logging.getLogger(__name__)

def send_order_confirmation_email(order_id, customer_email, customer_name, total_price):
    """
    Sends an order confirmation email to the customer.

    Args:
        order_id (int): The ID of the order.
        customer_email (str): The customer's email address.
        customer_name (str): The name of the customer.
        total_price (Decimal/float): The total price of the order.

    Returns:
        bool: True if email sent successfully, False otherwise.
    """

    subject = f"Order Confirmation - Order #{order_id}"
    message = (
        f"Hello {customer_name},\n\n"
        f"Thank you for your purchase!\n"
        f"Your order with ID #{order_id} has been successfully placed.\n"
        f"Total Amount: ₹{total_price}\n\n"
        f"You will receive another email once your order is shipped.\n\n"
        f"Best regards,\n"
        f"Our Store Team"
    )

    try:
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,  # from email (set in settings.py)
            [customer_email],            # recipient list
            fail_silently=False,         # raise error if sending fails
        )
        logger.info(f"Order confirmation email sent to {customer_email} for order {order_id}.")
        return True

    except BadHeaderError:
        logger.error("Invalid header found while sending email.")
        return False
    except Exception as e:
        logger.error(f"Error sending order confirmation email: {e}")
        return False
