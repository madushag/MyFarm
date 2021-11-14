from django.http import request
from django.test import TestCase, Client
from authenticate.forms import SignUpForm
from homepage.views import homepage
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.models import User

valid_form_data = {
  "username": "username",
  "email": "user@name.com",
  "password1": "password123!!!",
  "password2": "password123!!!"
}

missing_field_form_data = {
  "username": "username",
  "password1": "password123!!!",
  "password2": "password123!!!"
}

missing_field_form_data = {
  "username": "username",
  "password1": "password123!!!",
  "password2": "password123!!!"
}

invalid_field_form_data = {
  "username":" ",
  "email": "user@name.com",
  "password1": "password123!!!",
  "password2": "password123!!!"
}

diff_password_form_data = {
  "username":"username",
  "email": "user@name.com",
  "password1": "password123!!!",
  "password2": "password456!!!"
}

c = Client()

class TestSignUpView(TestCase):

    # Is the appropriate template rendered with a GET request
    def test_register_get_request(self):
       # Issue a GET request.
       response = self.client.get('/register/')
       self.assertEqual(response.status_code, 200)

    # Test POST with correct data succeeds
    def test_register_post_request(self):
        response = self.client.post('/register/',valid_form_data)
        self.assertEqual(response.status_code, 302)
        # self.assertTemplateUsed(response,'homepage/homepage.html')

    # Test response code POST with incorrect data
    # (Test invalid data types)
    def test_register_invalid_input_1(self):
        response = self.client.post('/register/',invalid_field_form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'authenticate/authenticate.html')

    # Test response code POST with incorrect data
    # (Required fields missing)
    def test_register_invalid_input_2(self):
        response = self.client.post('/register/',missing_field_form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'authenticate/authenticate.html')

    # Test response code POST with incorrect data
    # (Test existing username)
    def test_register_invalid_input_3(self):
        User = get_user_model()
        User.objects.create_user('username', 'user@name.com', 'password123!!!')
        response = self.client.post('/register/',valid_form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'authenticate/authenticate.html')

    # Test response code POST with incorrect data
    # (Passwords different)
    def test_register_invalid_input_4(self):
        User = get_user_model()
        response = self.client.post('/register/',diff_password_form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'authenticate/authenticate.html')


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
        
class LogoutTest(TestCase):

    def test_logout_view_redirects_to_homepage(self):
        response = c.get('/register/logout')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/')

        

