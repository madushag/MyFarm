from django.db import models


# Adding a stub farmer model for now. This should ideally be linked to the user account created during user
# registration.
class FarmerStub(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Farm(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    phone_no = models.CharField(max_length=12, blank=True, null=True)
    farmer = models.ForeignKey(FarmerStub, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name
