# orders/views.py
from .utils import send_order_confirmation_email

# After saving order
send_order_confirmation_email(
    order_id=order.order_id,
    customer_email=order.customer.email,
    customer_name=order.customer.username,
    total_price=order.total_price,
)


