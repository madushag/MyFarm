from django.test import TestCase, Client
from django.contrib.auth import get_user_model


c = Client()

class LoginTest(TestCase):
    def test_can_access_page(self):
        response = c.get('/register/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'authenticate/login.html')

    def test_authenticate_user(self):
        User = get_user_model()
        user = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')
        