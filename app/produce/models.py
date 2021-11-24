import os

from django.conf import settings
from django.db import models
from farm.models import Farm


# def UploadedConfigPath(instance, filename):
#     return os.path.join(settings.MEDIA_ROOT, str(instance.id), filename)

class Produce(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    min_quantity = models.FloatField(verbose_name='Min. Qty')
    is_organic = models.BooleanField(verbose_name='Organic')
    # picture = models.ImageField(upload_to=UploadedConfigPath, blank=True)
    # picture = models.ImageField(upload_to='produce_pics', blank=True)
    picture = models.FileField(upload_to='produce_pics', blank=True)
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

