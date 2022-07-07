from rest_framework import serializers
from sait.models import *


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = "__all__"


class RoomDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ("name_room", "is_music", "owner_id")
