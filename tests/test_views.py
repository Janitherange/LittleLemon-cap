from django.test import TestCase, RequestFactory
from restaurant.models import MenuItem
from restaurant.views import MenuItemsView
from restaurant.serializers import MenuItemSerializer

mocks = [
    {
        'title': 'Tacos',
        'price': 22.99,
        'inventory': 6,
    },
    {
        'title': 'Pizza',
        'price': 17.99,
        'inventory': 9,
    },
    {
        'title': 'Pizza',
        'price': 15.99,
        'inventory': 5,
    },
]


class MenuViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

        for mock in mocks:
            MenuItem.objects.create(
                title=mock.title,
                price=mock.price,
                inventory=mock.inventory
            )

    def test_getall(self):
        menuitems = MenuItem.objects.all()
        serialized_menuitems = MenuItemSerializer(menuitems, many=True)
        request = self.factory.get('restaurant/menu/')
        response = MenuItemsView.as_view()(request)

        self.assertEqual(response.data, serialized_menuitems.data)
