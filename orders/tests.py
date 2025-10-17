from django.test import TestCase

# Create your tests here.
# orders/tests.py
from django.test import TestCase
from home.models import MenuItem
from orders.models import Order, OrderItem
from decimal import Decimal

class OrderTotalTestCase(TestCase):
    def setUp(self):
        # Create sample menu items
        pizza = MenuItem.objects.create(name="Pizza", price=Decimal('200.00'))
        burger = MenuItem.objects.create(name="Burger", price=Decimal('100.00'))

        # Create order
        order = Order.objects.create(customer_name="Nagashree")

        # Add items to order
        OrderItem.objects.create(order=order, menu_item=pizza, quantity=2, price=pizza.price)
        OrderItem.objects.create(order=order, menu_item=burger, quantity=3, price=burger.price)

        self.order = order

    def test_calculate_total(self):
        total = self.order.calculate_total()
        expected_total = Decimal('200.00') * 2 + Decimal('100.00') * 3  # 700.00
        self.assertEqual(total, expected_total)
