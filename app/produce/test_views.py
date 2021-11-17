from django.test import TestCase
from .models import Produce


class TestIndexView(TestCase):

    def test_index_view_200(self):
        response = self.client.get('/produce')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'produce/index.html')