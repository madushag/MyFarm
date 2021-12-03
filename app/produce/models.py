import os

import geopy
from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models
from farm.models import Farm
from geopy.distance import distance

name_choices = [
    ("CARROTS", "Carrots"),
    ("KALE", "Kale"),
    ("BROCCOLI", "Broccoli"),
    ("PEAS", "Peas"),
    ("SWEET POTATOES", "Sweet potatoes"),
    ("BEETS", "Beets"),
    ("SPINACH", "Spinach"),
    ("TOMATOES", "Tomatoes"),
    ("GARLIC", "Garlic"),
    ("ONIONS", "Onions"),
]

mode_of_sale = [
    ("WHOLESALE", "Wholesale"),
    ("RETAIL", "Retail"),
    ("PICK YOUR OWN", "Pick Your Own"),
]


# def UploadedConfigPath(instance, filename):
#     return os.path.join(settings.MEDIA_ROOT, str(instance.id), filename)

class Produce(models.Model):
    description = models.TextField()
    price = models.FloatField(validators=[MinValueValidator(0.0)])
    min_quantity = models.FloatField(verbose_name='Min. Qty', validators=[MinValueValidator(0.0)])
    is_organic = models.BooleanField(verbose_name='Organic')
    # picture = models.ImageField(upload_to=UploadedConfigPath, blank=True)
    # picture = models.ImageField(upload_to='produce_pics', blank=True)
    picture = models.FileField(upload_to='produce_pics', blank=True)
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    name = models.CharField(
        max_length=20,
        choices=name_choices,
    )

    mode_of_sale = models.CharField(
        max_length=50,
        choices=mode_of_sale,
        )

    def __str__(self):
        return self.name

    def get_distance(self, customer_lat, customer_lng):
        if self.farm.location_lat:
            return distance(
                (customer_lat, customer_lng),
                (self.farm.location_lat, self.farm.location_lng)
            ).miles
        else:
            return -1
