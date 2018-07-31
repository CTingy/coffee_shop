from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    fullname = models.CharField(default='', max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
