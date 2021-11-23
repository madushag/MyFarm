from django.conf import settings
from django.db import models

# STATES = (
#     ('-1', ''),
#     ('MA', 'Massachusetts'),
#     ('VT', 'Vermont'),
#     ('NH', 'New Hampshire')
# )


class Farm(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    phone_no = models.CharField(max_length=12, verbose_name="Phone", blank=True, null=True)
    location_state = models.CharField(max_length=2, verbose_name="State")
    city = models.CharField(max_length=200, blank=True, null=True)
    farmer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
