from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from sait.models import Room, Link
from users.models import CustomUser
from .serializer import *


class RoomViewList(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class UserViewList(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class RoomViewOne(generics.RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class LinkViewSave(generics.CreateAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer


class LinkAddView(APIView):
    def post(self, request):
        ser = request.data
        password_message = ser.pop("password")
        try:
            Room.objects.get(password_room=password_message)
            ser = LinkSerializer(data=ser)
            ser.is_valid(raise_exception=True)
            ser.save()
            return Response({"result": True})
        except:
            return Response({"result": False})
