from behave import *
from django.contrib.auth.models import User

from produce.models import Produce
from farm.models import Farm


@given("POS {pos_name:w} exists at location {pos_pat:f}, {pos_lng:f}")
def step_impl(context, pos_name, pos_pat, pos_lng):
    farmer = User.objects.create_user(username='testuser', email='test@user.com', password='testpassword')
    Farm.objects.create(name=pos_name,
                        farm_name='Test Farm',
                        description="Test Description",
                        phone_no="123-456-7890",
                        website_url="www.test.com",
                        location_address="123 Test St",
                        location_lat=pos_pat,
                        location_lng=pos_lng,
                        location_url="https://maps.google.com/?cid=4806452031478065970",
                        farmer=farmer)


@step("Produce {produce:w} are available at {pos_name:w}")
def step_impl(context, produce, pos_name):
    farm = Farm.objects.get(name=pos_name)
    Produce.objects.create(name=produce, description="This is a carrot", price=1.0, min_quantity=10, is_organic=True,
                           farm=farm, mode_of_sale="WHOLESALE")


@then("User at location {user_lat:f}, {user_lng:f} should see distance of produce {produce:w} at this POS is {distance:f} miles")
def step_impl(context, user_lat, user_lng, produce, distance):
    produce = Produce.objects.get(name=produce)
    assert (produce.get_distance(user_lat, user_lng) == distance)
