from django.test import TestCase, RequestFactory, Client
from .models import Produce
from django.contrib.auth.models import User
from farm.views import add, details, delete, index
from farm.models import Farm
from produce.views import add as produce_add, list_produce as list_produce, edit as produce_edit

valid_form_data = {
    "name": "Carrots",
    "description": "test description",
    "price": "1.00",
    "min_quantity": "10",
    "is_organic": False,
    "farm": "Test Farm"
}

valid_farm_data = {
    "name": "Test Farm",
    "description": "Test Description",
    "phone_no": "123-456-7890",
    "location_state": "MA",
    "city": "Boston"
}
c = Client()


class TestProduceView(TestCase):

    def test_list_produce_of_invalid_farm(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', email='test@user.com', password='testpassword')

        invalid_farm_id = "1"
        request_path = f"produce/{invalid_farm_id}/list"
        request = self.factory.get(request_path)
        request.user = self.user
        response = list_produce(request, invalid_farm_id)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Invalid farm ID')

    def test_add_produce_to_invalid_farm(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', email='test@user.com', password='testpassword')

        # create test produce
        invalid_farm_id = "1"
        request = self.factory.post('/produce/add', {
            "name": "Item 1",
            "description": "Test Description",
            "price": "1.00",
            "min_quantity": "10",
            "is_organic": False,
            "farm": invalid_farm_id
        })
        request.user = self.user
        response = produce_add(request, invalid_farm_id)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Invalid farm ID')

    def test_farmer_view_of_produce(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', email='test@user.com', password='testpassword')

        # create test farm
        request = self.factory.post('/farm/add/', valid_farm_data)
        request.user = self.user
        add(request)

        # create test produce
        farm_id = Farm.objects.first().id
        request = self.factory.post('/produce/add', {
            "name": "CARROTS",
            "description": "test description",
            "price": "1.00",
            "min_quantity": "10",
            "is_organic": False,
            "farm": farm_id
        })
        request.user = self.user
        produce_add(request, farm_id)

        request_path = f"produce/{farm_id}/list"
        request = self.factory.get(request_path)
        request.user = self.user
        response = list_produce(request, farm_id)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Produce Available At Farm - Test Farm')
        self.assertContains(response, 'CARROTS')

    def test_farmer_view_unauthenticated(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', email='test@user.com', password='testpassword')

        # create test farm
        request = self.factory.post('/farm/add/', valid_farm_data)
        request.user = self.user
        add(request)

        # create test produce
        farm_id = Farm.objects.first().id
        request = self.factory.post('/produce/add', {
            "name": "Carrots",
            "description": "test description",
            "price": "1.00",
            "min_quantity": "10",
            "is_organic": False,
            "farm": farm_id
        })
        request.user = self.user
        produce_add(request, farm_id)

        response = c.get(f"/produce/{farm_id}/list")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, f'/register/login/?next=/produce/{farm_id}/list')


    def test_form_input(self):
        response = self.client.post('/produce/add', valid_form_data)
        self.assertEqual(response.status_code, 302)

    def test_invalid_produce_id(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', email='test@user.com', password='testpassword')

        invalid_produce_id = "1"
        request_path = f"produce/{invalid_produce_id}/edit"
        request = self.factory.get(request_path)
        request.user = self.user
        response = produce_edit(request, invalid_produce_id)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Invalid produce ID')

    def test_invalid_price_qty_values_shows_error_message(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', email='test@user.com', password='testpassword')

        # create test farm
        request = self.factory.post('/farm/add/', valid_farm_data)
        request.user = self.user
        add(request)

        # create test produce
        farm_id = Farm.objects.first().id
        request = self.factory.post('/produce/add', {
            "name": "Item 1",
            "description": "Test Description",
            "price": "-1",
            "min_quantity": "-10",
            "is_organic": False,
            "farm": farm_id
        })
        request.user = self.user
        response = produce_add(request, farm_id)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'PRICE - Ensure this value is greater than or equal to 0.0.')
        self.assertContains(response, 'MIN. QTY - Ensure this value is greater than or equal to 0.0.')