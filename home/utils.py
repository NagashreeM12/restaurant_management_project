# home/utils.py
def calculate_order_total(order_items):
    """
    Calculates the total price of an order.

    Args:
        order_items (list of dict): Each dict should have 'quantity' and 'price' keys.
            Example: [{'quantity': 2, 'price': 150.0}, {'quantity': 1, 'price': 200.0}]

    Returns:
        float: Total cost of the order. Returns 0.0 if order_items is empty.
    """
    if not order_items:
        return 0.0

    total = 0.0
    for item in order_items:
        qty = item.get('quantity', 0)
        price = item.get('price', 0.0)
        total += qty * price
    return total
