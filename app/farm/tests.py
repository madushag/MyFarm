from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.models import User
from django.test import TestCase, Client, RequestFactory

from .models import Farm
from .views import add, details, delete, index

valid_form_data = {
    "name": "Test Farm",
    "description": "Test Description",
    "phone_no": "123-456-7890"
}

update_form_data = {
    "name": "Test Farm 2",
    "description": "Test Description",
    "phone_no": "123-456-7890"
}


class TestFarmView(TestCase):

    def test_index(self):
        response = self.client.get('/farm/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'farm/index.html')

    def test_add(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', email='test@user.com', password='testpassword')
        request = self.factory.post('/farm/add/', valid_form_data)
        request.user = self.user

        response = add(request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/farm/')

    def test_details(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', email='test@user.com', password='testpassword')
        request = self.factory.post('/farm/add/', valid_form_data)
        request.user = self.user
        add(request)

        request = self.factory.get('/farm/1/details')
        request.user = self.user
        response = details(request, 1)
        self.assertContains(response, 'Test Farm')

    def test_details_invalid_user(self):
        self.factory = RequestFactory()
        request = self.factory.post('/farm/add/', valid_form_data)
        request.user = User.objects.create_user(username='testuser', email='test@user.com', password='testpassword')
        add(request)

        request = self.factory.get('/farm/1/details')
        request.user = User.objects.create_user(username='anothertestuser', email='test@user.com',
                                                password='testpassword')
        response = details(request, 1)
        self.assertContains(response, 'You do not have permission to view this farm.')

    def test_details_invalid_farm_id(self):
        self.factory = RequestFactory()
        request = self.factory.post('/farm/add/', valid_form_data)
        request.user = User.objects.create_user(username='testuser', email='test@user.com', password='testpassword')
        add(request)

        request = self.factory.get('/farm/2/details')
        request.user = authenticate(username='testuser', password='testpassword')
        response = details(request, 2)
        self.assertContains(response, 'Invalid farm ID')

    def test_details_update(self):
        self.factory = RequestFactory()
        request = self.factory.post('/farm/add/', valid_form_data)
        request.user = User.objects.create_user(username='testuser', email='test@user.com', password='testpassword')
        add(request)

        request = self.factory.post('/farm/1/details', update_form_data)
        request.user = authenticate(username='testuser', password='testpassword')
        response = details(request, 1)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/farm/')

        request = self.factory.get('/farm/1/details')
        request.user = authenticate(username='testuser', password='testpassword')
        response = details(request, 1)
        self.assertContains(response, 'Test Farm 2')

    def test_details_update_invalid_user(self):
        self.factory = RequestFactory()
        request = self.factory.post('/farm/add/', valid_form_data)
        request.user = User.objects.create_user(username='testuser', email='test@user.com', password='testpassword')
        add(request)

        request = self.factory.post('/farm/1/details', update_form_data)
        request.user = User.objects.create_user(username='anothertestuser', email='test@user.com',
                                                password='testpassword')
        response = details(request, 1)
        self.assertContains(response, 'You do not have permission to update this farm.')

    def test_delete_invalid_user(self):
        self.factory = RequestFactory()
        request = self.factory.post('/farm/add/', valid_form_data)
        request.user = User.objects.create_user(username='testuser', email='test@user.com', password='testpassword')
        add(request)

        request = self.factory.post('/farm/1/delete')
        request.user = User.objects.create_user(username='anothertestuser', email='test@user.com',
                                                password='testpassword')
        response = delete(request, 1)
        self.assertContains(response, 'You do not have permission to delete this farm.')

    def test_delete_invalid_farm_id(self):
        self.factory = RequestFactory()
        request = self.factory.post('/farm/add/', valid_form_data)
        request.user = User.objects.create_user(username='testuser', email='test@user.com', password='testpassword')
        add(request)

        request = self.factory.post('/farm/2/delete')
        request.user = authenticate(username='testuser', password='testpassword')
        response = delete(request, 2)
        self.assertContains(response, 'Invalid farm ID')

    def test_delete(self):
        self.factory = RequestFactory()
        request = self.factory.post('/farm/add/', valid_form_data)
        request.user = User.objects.create_user(username='testuser', email='test@user.com', password='testpassword')
        add(request)

        request = self.factory.post('/farm/1/delete')
        request.user = authenticate(username='testuser', password='testpassword')
        response = delete(request, 1)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/farm/')

        request = self.factory.get('/farm/')
        request.user = authenticate(username='testuser', password='testpassword')
        response = index(request)
        self.assertContains(response, 'No farms are available.')

    def test_farm_model(self):
        farm = Farm(name='Test Farm', description='Test Description', phone_no='1234567890')
        self.assertEqual(farm.name, 'Test Farm')
