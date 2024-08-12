from django.db import models

# Create your models here.


class Books(models.Model):
    name = models.CharField(max_length=20)
    Auther = models.CharField(max_length=20)
    publication_date = models.DateField()
    edition = models.IntegerField()
