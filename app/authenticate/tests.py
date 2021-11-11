from django.test import TestCase, Client
from django.contrib.auth import get_user_model, login


c = Client()

class LoginTest(TestCase):
    def test_can_access_register_page(self):
        response = c.get('/register/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'authenticate/authenticate.html')

    def test_can_access_login_page(self):
        response = c.get('/register/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'authenticate/login.html')

    def test_authenticate_user(self):
        User = get_user_model()
        User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')
        response = self.client.login(username='temporary', password='temporary')
        self.assertEqual(response, True)
    
    def test_fake_user_authentication(self):
        User = get_user_model()
        response = self.client.login(username='temporary', password='temporary')
        self.assertNotEqual(response, True)
        