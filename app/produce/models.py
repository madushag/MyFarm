from django.db import models
from farm.models import Farm


class Produce(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    min_quantity = models.FloatField(verbose_name='Min. Qty')
    is_organic = models.BooleanField(verbose_name='Organic')
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
