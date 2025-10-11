# orders/utils.py

from datetime import date
from django.db.models import Sum
from .models import Order


def get_daily_sales_total(specific_date: date):
    """
    Calculate total sales for a given date.
    
    Args:
        specific_date (date): The date for which sales total is to be calculated.
    
    Returns:
        Decimal: Total sales amount for that date (0 if no orders found).
    """
    # Filter all orders whose created_at date matches the given date
    orders = Order.objects.filter(created_at__date=specific_date)

    # Aggregate the total sales using Sum
    total = orders.aggregate(total_sum=Sum('total_price'))['total_sum']

    # Return 0 if no orders found
    return total or 0
