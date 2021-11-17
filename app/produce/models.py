from django.db import models
from farm.models import Farm


class Produce(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    min_quantity = models.FloatField()
    is_organic = models.BooleanField()
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
