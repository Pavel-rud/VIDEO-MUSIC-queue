from django.db import models
from users.models import CustomUser


class Room(models.Model):
    name_room = models.CharField(max_length=50, unique=True)
    password_room = models.CharField(max_length=50)
    owner_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # owner_name = models.CharField(max_length=50, default=CustomUser.objects.get(name=), editable=False)
    is_music = models.BooleanField(default=True)

    def __str__(self):
        return self.name_room


class Link(models.Model):
    room = models.ForeignKey('Room', on_delete=models.CASCADE, db_index=True)
    link = models.CharField(max_length=255)
    user_id = models.IntegerField(default=777777, blank=True)
    tg_name = models.CharField(default="", max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.link
