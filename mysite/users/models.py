from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    tg_name = models.CharField(max_length=50, blank=True)
    avatar = models.ImageField(blank=True, default='default.jpg')

    REQUIRED_FIELDS = ['tg_name', 'avatar', 'email']

    def __str__(self):
        return self.username
