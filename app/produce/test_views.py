from django.test import TestCase, RequestFactory, Client
from .models import Produce
from django.contrib.auth.models import User
from farm.views import add, details, delete, index
from farm.models import Farm
from produce.views import add as produce_add, index as produce_index

valid_form_data = {
    "name": "CARROTS",
    "price": "1.00",
    "min_quantity": "10",
    "is_organic": False,
    "farm": "Test Farm"
}

c = Client()


class TestProduceView(TestCase):

    def test_farmer_view_of_produce(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', email='test@user.com', password='testpassword')

        # create test farm
        request = self.factory.post('/farm/add/', {
            "name": "Test Farm",
            "description": "Test Description",
            "phone_no": "123-456-7890"
        })
        request.user = self.user
        add(request)

        # create test produce
        farm_id = Farm.objects.first().id
        request = self.factory.post('/produce/add', {
            "name": "CARROTS",
            "price": "1.00",
            "min_quantity": "10",
            "is_organic": False,
            "farm": farm_id
        })
        request.user = self.user
        produce_add(request)

        request_path = f"produce/{farm_id}/list"
        request = self.factory.get(request_path)
        request.user = self.user
        response = produce_index(request, farm_id)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Produce Available At Farm - Test Farm')
        self.assertContains(response, 'CARROTS')

    def test_farmer_view_unauthenticated(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', email='test@user.com', password='testpassword')

        # create test farm
        request = self.factory.post('/farm/add/', {
            "name": "Test Farm",
            "description": "Test Description",
            "phone_no": "123-456-7890"
        })
        request.user = self.user
        add(request)

        # create test produce
        farm_id = Farm.objects.first().id
        request = self.factory.post('/produce/add', {
            "name": "CARROTS",
            "price": "1.00",
            "min_quantity": "10",
            "is_organic": False,
            "farm": farm_id
        })
        request.user = self.user
        produce_add(request)

        response = c.get(f"/produce/{farm_id}/list")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, f'/register/login/?next=/produce/{farm_id}/list')


    def test_form_input(self):
        response = self.client.post('/produce/add', valid_form_data)
        self.assertEqual(response.status_code, 302)
        # self.assertTemplateUsed(response,'authenticate/authenticate.html')
