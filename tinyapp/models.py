from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class User(AbstractUser):
   pass
    
# Create your models here.
class Users (models.Model):
   first_name = models.CharField(max_length=20)
   last_name = models.CharField(max_length=30)
   username = models.CharField(max_length=30)
   email_address = models.CharField(max_length=30)
   password = models.CharField(max_length=15)

   def __str__(self):
        return f'{self.last_name}, {self.first_name}'


class Url(models.Model):
   short_url = models.URLField(max_length=10)
   long_url = models.URLField(max_length=200) 
   user = models.ForeignKey(User, on_delete=models.CASCADE) 
   date_created = models.DateField()

   def __str__(self):
        return self.short_url

   def get_absolute_url(self):
       return reverse('urls_detail', args=[str(self.pk)])

   
