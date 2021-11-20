from django.test import TestCase
from .models import Produce


class TestProduceModel(TestCase):

    def test_str_method(self):
        produce = Produce(name='Apple', price=1.00, min_quantity=10, is_organic=True)
        self.assertEqual(str(produce), produce.name)
