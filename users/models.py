from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField


# Create your models here.


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="почта")
    phone_number = models.CharField(max_length=40, verbose_name="телефон")
    avatar = models.ImageField(upload_to="users/", verbose_name="аватар", blank=True, null=True)
    country = CountryField(verbose_name="страна")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
