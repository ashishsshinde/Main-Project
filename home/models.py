from statistics import mode
from django.db import models


# Create your models here.
class User(models.Model):
    Firstname = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Contact = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)

class contactForm(models.Model):
    names = models.CharField(max_length=100)
    emailAddress = models.CharField(max_length=100)
    message = models.CharField(max_length=100)

class call(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)