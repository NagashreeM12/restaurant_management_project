from decimal import Decimal
from django.db import models

# Try to import the discount utility; fallback to a no-op if not present.
try:
    from orders.utils import calculate_discount
except Exception:
    def calculate_discount(amount: Decimal, discount_percent: Decimal) -> Decimal:
        """
        Fallback: if the real utility isn't available, return amount unchanged.
        Keep signature compatible with (amount, discount_percent).
        """
        return amount


class Order(models.Model):
    # example fields (you might already have your own)
    order_id = models.CharField(max_length=50, unique=True)
    customer = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # attach custom manager if you have one already
    # objects = OrderManager()

    def _get_items_qs(self):
        """
        Return the related manager for order items.
        Tries common related_name possibilities.
        """
        # common related names for OrderItem -> Order FK: 'items', 'order_items', 'orderitem_set'
        for attr in ('items', 'order_items', 'orderitem_set'):
            if hasattr(self, attr):
                return getattr(self, attr).all()
        # If none exist, try to find any related objects automatically (best-effort fallback)
        # but return empty queryset-like list to avoid crashing
        return []

    def calculate_total(self) -> Decimal:
        """
        Calculate the total price of the order by summing each item's (price * quantity),
        applying item-level discount if available (using calculate_discount utility),
        otherwise applying order-level discount if present (attribute 'discount_percent').

        Returns:
            Decimal: total payable amount (rounded to 2 decimal places).
        """
        total = Decimal('0.00')

        items_qs = self._get_items_qs()

        for item in items_qs:
            # Determine unit price
            unit_price = None
            if hasattr(item, 'price') and item.price is not None:
                unit_price = item.price
            elif hasattr(item, 'menu_item') and getattr(item.menu_item, 'price', None) is not None:
                unit_price = item.menu_item.price

            if unit_price is None:
                # skip items with no price information
                continue

            # Ensure Decimal
            if not isinstance(unit_price, Decimal):
                unit_price = Decimal(str(unit_price))

            # Quantity (default 1)
            quantity = getattr(item, 'quantity', 1) or 1
            try:
                quantity = int(quantity)
            except Exception:
                quantity = 1

            line_total = unit_price * Decimal(quantity)

            # Prefer item-level discount if present
            discounted_amount = line_total
            item_discount = getattr(item, 'discount_percent', None)

            if item_discount is not None:
                try:
                    # coerce discount to Decimal
                    if not isinstance(item_discount, Decimal):
                        item_discount = Decimal(str(item_discount))
                    discounted_amount = calculate_discount(line_total, item_discount)
                except Exception:
                    # if discount util fails, fall back to line_total
                    discounted_amount = line_total
            else:
                # fallback to order-level discount if present
                order_discount = getattr(self, 'discount_percent', None)
                if order_discount is not None:
                    try:
                        if not isinstance(order_discount, Decimal):
                            order_discount = Decimal(str(order_discount))
                        discounted_amount = calculate_discount(line_total, order_discount)
                    except Exception:
                        discounted_amount = line_total

            # Add to total
            if not isinstance(discounted_amount, Decimal):
                discounted_amount = Decimal(str(discounted_amount))

            total += discounted_amount

        # Optionally round to 2 decimal places
        return total.quantize(Decimal('0.01'))
