from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core import validators as v
# Create your models here.

class App_user(AbstractUser):
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField(default=18, validators = [v.MinValueValidator(18), v.MaxValueValidator(100)])
    display_name = models.CharField(default='unknown' , max_length=50)
    address = models.TextField(default='unknown')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =[]
    # lists

class UserManager(BaseUserManager):
    def create_superuser(self, email, password=None, **extra_fields):
        # Note: no username parameter here
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user