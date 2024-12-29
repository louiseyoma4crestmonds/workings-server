import environ
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from knox.models import AuthToken

from .managers import CustomUserManager


# Initialise environment variables
ENV = environ.Env()
environ.Env.read_env()

# Create your models here.

class ApplicationUserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    country = models.CharField(max_length=50, default='')
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_added = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'


    objects = CustomUserManager()

    def __str__(self):
        return self.email 



    
