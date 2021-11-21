from django.contrib.auth.models import User
from django.test import TestCase, Client, RequestFactory
from farm.views import add, details, delete, index
from produce.views import add as produce_add
from farm.models import Farm

c = Client()

class TestHomepageViews(TestCase):

  def test_homepage_route_results_in_200(self):
    response = c.get('/')
    self.assertEqual(response.status_code, 200)

  def test_customer_view_of_produce(self):
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
        "name": "Item 1",
        "price": "1.00",
        "min_quantity": "10",
        "is_organic": False,
        "farm": farm_id
    })
    request.user = self.user
    produce_add(request)

    response = c.get('/')
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'produce/customer_view.html')
    self.assertContains(response, 'List of Produce')
    self.assertContains(response, 'Item 1')
    self.assertContains(response, 'Test Farm')
