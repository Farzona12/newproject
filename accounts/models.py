from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

<<<<<<< HEAD
# Create your models here.
=======

class CustomUser(AbstractUser):
    username = models.CharField(max_length=100,null=True)
    email = models.CharField(max_length=200,unique=True)

    email_verified = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

>>>>>>> be7f8673523485291320f792f7c7aaa1d799cf9c
