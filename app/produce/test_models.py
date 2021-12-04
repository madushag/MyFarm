from django.test import TestCase
from .models import Produce
from farm.models import Farm


class TestProduceModel(TestCase):

    def test_str_method(self):
        produce = Produce(name='Apple', price=1.00, min_quantity=10, is_organic=True)
        self.assertEqual(str(produce), produce.name)

    def test_get_distance(self):
        farm = Farm(name='Apple Farm', location_lat=42.4071855, location_lng=-71.013356)
        produce = Produce(name='Apple', price=1.00, min_quantity=10, is_organic=True, farm=farm)
        self.assertEqual(produce.get_distance(42.4068238, -71.0169325), 0.1846397184436176)
