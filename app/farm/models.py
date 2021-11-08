from django.contrib.auth.models import User
from django.db import models


class Farm(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    phone_no = models.CharField(max_length=12, blank=True, null=True)
    farmer = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name
