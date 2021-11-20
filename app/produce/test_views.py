from django.test import TestCase
from .models import Produce


valid_form_data = {
  "name": "Item 1",
  "price": "1.00",
  "min_quantity": "10",
  "is_organic": False,
  "farm": "my first farm"
}


class TestIndexView(TestCase):

    # This test cannot be completed until the CRUD views for produce are implemented
    def test_index(self):
        response = self.client.get('/produce')
        self.assertEqual(response.status_code, 404)
        # self.assertTemplateUsed(response, 'produce/index.html')

    # This test cannot be completed until the CRUD views for produce are implemented
    def test_customer(self):
        response = self.client.get('/produce')
        self.assertEqual(response.status_code, 404)
        # self.assertTemplateUsed(response, 'produce/index.html')

    # Test response code POST with incorrect data
    # (Passwords different)
    def test_form_input(self):
        response = self.client.post('/produce/add',valid_form_data)
        self.assertEqual(response.status_code, 302)
        # self.assertTemplateUsed(response,'authenticate/authenticate.html')
