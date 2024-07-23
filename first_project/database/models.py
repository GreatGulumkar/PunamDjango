from django.db import models

# Create your models here.


# User's username and password will be stored in Django's default User model.
# User's email is their username


class UserProfile(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
