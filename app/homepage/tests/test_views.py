from django.test import TestCase, Client

c = Client()

class HomePageTestCase(TestCase):

  def test_homepage_route_results_in_200(self):
    response = c.get('/')
    self.assertEqual(response.status_code, 200)

