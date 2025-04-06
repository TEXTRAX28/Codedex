import unittest
from test_class import CoffeeMenu

class TestCoffeeMenu(unittest.TestCase):
    def setUp(self):
        self.coffee_menu = CoffeeMenu()

    def test_get_price_existing_item(self):
        get_price = self.coffee_menu.get_price
        self.assertEqual(get_price('espresso'), 2.5)
        self.assertEqual(get_price('latte'), 2.75)
        self.assertEqual(get_price('cappuccino'), 3.20)
        self.assertEqual(get_price('americano'), 2.70)
        self.assertNotEqual(get_price('americano'), 3.00)

    def test_get_price_non_existing_item(self):
        get_price = self.coffee_menu.get_price
        self.assertNotEqual(get_price('mocha'), 3.00)

    def test_add_item(self):
        self.coffee_menu.add_item('mocha', 3.00)
        self.assertEqual(self.coffee_menu.get_price('mocha'), 3.00)
