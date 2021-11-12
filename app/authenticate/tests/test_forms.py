from django.test import TestCase
from authenticate.forms import SignUpForm

valid_form_data = {
  "username": "username",
  "firstname": "user",
  "lastname": "name",
  "email": "user@name.com",
  "password1": "password123!!!",
  "password2": "password123!!!"
}


class TestTestsWork(TestCase):

  def test_true_is_true(self):
      self.assertEqual(True, True)


class TestSignUpForm(TestCase):

  def test_form_is_valid_with_correct_data(self):
    form = SignUpForm(valid_form_data)
    self.assertTrue(form.is_valid())
  
  def test_form_is_invalid_when_passwords_dont_match(self):
    form_data = {**valid_form_data, "password2": "aDifferentPassword"}
    form = SignUpForm(form_data)
    self.assertFalse(form.is_valid())

  def test_form_is_invalid_when_username_is_missing(self):
    form_data = {**valid_form_data, "username": None}
    form = SignUpForm(form_data)
    self.assertFalse(form.is_valid())

  def test_form_is_invalid_when_email_is_missing(self):
    form_data = {**valid_form_data, "email": None}
    form = SignUpForm(form_data)
    self.assertFalse(form.is_valid())

  def test_form_is_invalid_when_email_format_is_wrong(self):
    form_data = {**valid_form_data, "email": "This is not what an email looks like"}
    form = SignUpForm(form_data)
    self.assertFalse(form.is_valid())

