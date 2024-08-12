from django.db import models

# Create your models here.


class Olympics(models.Model):

    sport_id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=20, null=False)
    category = models.CharField(max_length=20, null=False)


class Sport(models.Model):

    sport_id = models.IntegerField()
    image = models.ImageField(upload_to="media")


class images(models.Model):
    picture = models.BinaryField()
