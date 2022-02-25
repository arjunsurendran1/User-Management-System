from django.db import models

# Create your models here.


class Registration(models.Model):

    First_name = models.CharField(max_length=200)
    Last_name = models.CharField(max_length=200)
    User_name = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)
    password1 = models.CharField(max_length=200)
    password2 = models.CharField(max_length=200)


class UserRegistration(models.Model):
    First_name = models.CharField(max_length=200)
    Last_name = models.CharField(max_length=200)
    User_name = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)
    password1 = models.CharField(max_length=200)
    password2 = models.CharField(max_length=200)


