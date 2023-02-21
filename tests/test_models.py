from django.test import TestCase
from restaurant.models import MenuItem


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(
            title="Tacos",
            price=12.99,
            inventory=6
        )
        self.assertEqual(str(item), "Tacos : 12.99")