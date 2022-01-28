from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

# Create your models here.
class Users (models.Model):
   first_name = models.CharField(max_length=20)
   last_name = models.CharField(max_length=30)
   username = models.CharField(max_length=30)
   email_address = models.CharField(max_length=30)
   password = models.CharField(max_length=15)


class Url(models.Model):
   short_url = models.URLField(max_length=10)
   long_url = models.URLField(max_length=200) 
   user = models.ForeignKey(User, on_delete=models.CASCADE) 
   date_created = models.DateField()

