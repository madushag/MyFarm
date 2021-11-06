from django.db import models


class Farm(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    phone_no = models.IntegerField(default=0)

    def __str__(self):
        return self.name
