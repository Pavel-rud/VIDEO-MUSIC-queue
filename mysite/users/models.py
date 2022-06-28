from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    tg_name = models.CharField(max_length=50)
    avatar = models.ImageField()
    name = models.CharField(max_length=50, )

    def __str__(self):
        return self.username
