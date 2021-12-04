from django.contrib.auth.models import User
from django.test import TestCase, Client, RequestFactory
from farm.views import add, details, delete, index
from produce.views import add as produce_add
from farm.models import Farm

from produce.models import Produce

c = Client()

class TestHomepageViews(TestCase):

  @classmethod
  def setUpTestData(cls):
    user = User.objects.create_user(username='testuser', email='test@user.com', password='testpassword')
    farm = Farm.objects.create(name="Test Farm", description="Test Description", phone_no="123-456-7890", farmer=user)
    Produce.objects.create(name="CARROTS", price=1.0, min_quantity=10, is_organic=False, farm=farm)
    Produce.objects.create(name="KALE", price=1.0, min_quantity=10, is_organic=False, farm=farm)

  def test_homepage_route_results_in_200(self):
    response = c.get('/')
    self.assertEqual(response.status_code, 200)

  def test_customer_view_of_produce(self):
    response = c.get('/')
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'produce/customer_view.html')
    self.assertContains(response, 'List of Produce')
    self.assertContains(response, '>CARROTS')
    self.assertContains(response, 'Test Farm')
    self.assertContains(response, '10.0 lbs.')

  def test_customer_view_of_produce_filtered_returns_200(self):
    response = c.get('/?produce=KALE')
    self.assertEqual(response.status_code, 200)

  def test_customer_view_of_produce_filtered_contains_query_term(self):
    response = c.get('/?produce=KALE')
    self.assertContains(response, ">KALE")

  def test_customer_view_of_produce_filtered_only_contains_query_term(self):
    response = c.get('/?produce=KALE')
    self.assertNotContains(response, ">CARROTS")

  def test_customer_view_of_produce_filtered_returns_correct_template(self):
    response = c.get('/?produce=KALE')
    self.assertTemplateUsed(response, 'produce/customer_view.html')

  def test_customer_view_of_produce_displays_produce_filter(self):
    response = c.get('/')
    self.assertContains(response, "Produce")

  def test_customer_view_of_produce_displays_mode_filter(self):
    response = c.get('/')
    self.assertContains(response, "Sale Type")
