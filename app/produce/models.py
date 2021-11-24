from django.db import models
from farm.models import Farm

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

class Produce(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    min_quantity = models.FloatField()
    is_organic = models.BooleanField()
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    name = models.CharField(
        max_length=20,
        choices=name_choices,
    )
    def __str__(self):
        return self.name