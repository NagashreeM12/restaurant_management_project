import logging
from django.core.exceptions import ObjectDoesNotExist
from .models import Order

# Configure logger
logger = logging.getLogger(__name__)

def update_order_status(order_id, new_status):
    """
    Reusable function to update the status of an order.
    Args:
        order_id (int): ID of the order to update
        new_status (str): New status to set (e.g., 'pending', 'processing', 'completed')
    Returns:
        str: Success or error message
    """
    try:
        order = Order.objects.get(id=order_id)
        old_status = order.status
        order.status = new_status
        order.save()

        logger.info(f"Order #{order_id} status updated from '{old_status}' to '{new_status}'.")
        return f"Order #{order_id} status successfully updated to '{new_status}'."

    except ObjectDoesNotExist:
        logger.error(f"Order with ID {order_id} not found.")
        return f"Error: Order with ID {order_id} not found."

    except Exception as e:
        logger.error(f"Unexpected error updating order #{order_id}: {e}")
        return f"Error updating order #{order_id}: {e}"

