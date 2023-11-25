from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomerUser(AbstractUser):
    birth_day = models.DateField(null=True, blank=True)


