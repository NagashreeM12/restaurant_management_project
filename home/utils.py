# home/utils.py
def calculate_discount(original_price, discount_percentage):
    """
    Calculates the discounted price for a menu item.

    Args:
        original_price (float or int): Original price of the item.
        discount_percentage (float or int): Discount percentage (0-100).

    Returns:
        float: Discounted price, rounded to 2 decimal places.
               Returns original_price if inputs are invalid.
    """
    try:
        if original_price < 0 or discount_percentage < 0 or discount_percentage > 100:
            return original_price  # Invalid input, return original price

        discount_amount = (discount_percentage / 100) * original_price
        discounted_price = original_price - discount_amount
