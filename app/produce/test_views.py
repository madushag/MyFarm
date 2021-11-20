from django.test import TestCase
from .models import Produce


class TestIndexView(TestCase):

    # This test cannot be completed until the CRUD views for produce are implemented
    def test_index(self):
        response = self.client.get('/produce')
        self.assertEqual(response.status_code, 404)
        # self.assertTemplateUsed(response, 'produce/index.html')
