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
        farm = Farm.objects.create(name="Test POS",
                                   farm_name='Test Farm',
                                   description="Test Description",
                                   phone_no="123-456-7890",
                                   website_url="www.test.com",
                                   location_address="123 Test St",
                                   location_lat="42.4071855",
                                   location_lng="-71.013356",
                                   location_url="https://maps.google.com/?cid=4806452031478065970",
                                   farmer=user)
        farm2 = Farm.objects.create(name="Test POS2",
                                    farm_name='Test Farm',
                                    location_lat="42.4071855",
                                    location_lng="-91.013356",
                                    farmer=user)

        Produce.objects.create(name="CARROTS", description="This is a carrot", price=1.0, min_quantity=10, is_organic=True, farm=farm, mode_of_sale="WHOLESALE")
        Produce.objects.create(name="KALE", price=1.0, min_quantity=10, is_organic=False, farm=farm, mode_of_sale="RETAIL")

        Produce.objects.create(name="CARROTS", description="This is a carrot", price=1.0, min_quantity=10, is_organic=True, farm=farm2, mode_of_sale="WHOLESALE")

    def test_homepage_route_results_in_200(self):
        response = c.get('/')
        self.assertEqual(response.status_code, 200)

    def test_customer_view_of_produce(self):
        response = c.get('/?lng=-71.0169325&lat=42.4068238')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'produce/customer_view.html')
        self.assertContains(response, 'List of Produce')
        self.assertContains(response, '>CARROTS')
        self.assertContains(response, 'This is a carrot')
        self.assertContains(response, 'Test POS')
        self.assertContains(response, '<b>Min. Quantity : </b>10.0 lbs.')
        self.assertContains(response, 'Test Farm')
        self.assertContains(response, 'Test POS')
        self.assertContains(response, 'www.test.com')
        self.assertContains(response, '123 Test St')
        self.assertContains(response, '<b>Distance:</b> 0.18 miles')
        self.assertContains(response, 'https://maps.google.com/?cid=4806452031478065970')
        self.assertContains(response, 'Contact Farmer')
        self.assertContains(response, 'test@user.com')
        self.assertContains(response, '$1.00')
        self.assertContains(response, 'organic.png')

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

    def test_customer_view_of_produce_filtered_on_sale_type_returns_correct_results(self):
        response = c.get('/?saleType=WHOLESALE')
        self.assertContains(response, ">CARROTS")
        self.assertNotContains(response, ">KALE")

    def test_customer_view_of_produce_filtered_on_distance_returns_correct_results(self):
        response = c.get('/?distance=5&lng=-71.0169325&lat=42.4068238')
        self.assertContains(response, ">CARROTS")

    def test_customer_view_of_produce_displays_produce_filter(self):
        response = c.get('/')
        self.assertContains(response, "Produce")

    def test_customer_view_of_produce_displays_mode_filter(self):
        response = c.get('/')
        self.assertContains(response, "Sale Type")

    def test_customer_view_of_produce_displays_distance_filter(self):
        response = c.get('/')
        self.assertContains(response, "Distance")
