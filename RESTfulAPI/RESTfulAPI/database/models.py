from django.db import models


# Create your models here.
class product(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=100)
    price = models.FloatField()
