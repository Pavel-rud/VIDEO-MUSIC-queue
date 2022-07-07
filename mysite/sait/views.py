import json

from django.contrib.auth.models import Group
from rest_framework import generics
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import CustomUser
from .models import Room, Link

from sait.serializer import RoomSerializer


class CreateRoomView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            ser = request.data
            username_r = ser.pop("username")
            t = CustomUser.objects.filter(username=username_r).values()
            ser['owner_id'] = t[0]['id']
            ser = RoomSerializer(data=ser)
            ser.is_valid()
            ser.save()
            new_group = Group()
            new_group.name = ser.data.get("id")
            new_group.save()
            t_g = Group.objects.get(name=ser.data.get("id"))
            t_g.user_set.add(CustomUser.objects.get(id=t[0]['id']))
            return Response({"result": True})
        except Exception as e:
            return Response({"result": str(e)})


class GetUserRoomsView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        username_r = request.data["username"]
        user = CustomUser.objects.get(username=username_r)
        t = user.groups.all()
        data = list()
        for i in t:
            if Room.objects.get(id=i.name).owner_id == user:
                data.append({"id_room": i.name, "name_room": Room.objects.get(id=i.name).name_room, "is_owner": True})
            else:
                data.append({"id_room": i.name, "name_room": Room.objects.get(id=i.name).name_room, "is_owner": False})
        return Response({"result": data})


class GetUserRoomView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        print(pk)
        return Response({"result": request.data})