from django.conf import settings
from django.db import models


class Farm(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    phone_no = models.CharField(max_length=12, verbose_name="Phone", blank=True, null=True)
    website_url = models.URLField(blank=True, null=True)
    farmer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    city = models.CharField(max_length=200, blank=True, null=True)
    location_state = models.CharField(max_length=2, verbose_name="State", blank=True, null=True)
    location_lat = models.DecimalField(max_digits=16, decimal_places=14, blank=True, null=True)
    location_lng = models.DecimalField(max_digits=16, decimal_places=13, blank=True, null=True)
    location_name = models.CharField(max_length=500, blank=True, null=True)
    location_url = models.URLField(blank=True, null=True)
    location_address = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name
