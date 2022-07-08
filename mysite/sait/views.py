import json
import re

from django.contrib.auth.models import Group
from rest_framework import generics, viewsets
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import CustomUser
from .models import Room, Link

from sait.serializer import RoomSerializer, RoomDataSerializer, LinkSerializer


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
            return Response({"id": ser.data.get("id")})
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
                data.append({
                    "id_room": i.name,
                    "name_room": Room.objects.get(id=i.name).name_room,
                    "is_owner": True,
                    "is_music": Room.objects.get(id=i.name).is_music
                })
            else:
                data.append({
                    "id_room": i.name,
                    "name_room": Room.objects.get(id=i.name).name_room,
                    "is_owner": False,
                    "is_music": Room.objects.get(id=i.name).is_music
                })
        return Response({"result": data})


class AddUserToRoomView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            req = request.data
            t = Room.objects.get(id=req['id_room'])
            if req['password_room'] == t.password_room:
                t_g = Group.objects.get(name=t.id)
                t_g.user_set.add(CustomUser.objects.get(username=req['username']))
                return Response({"result": True})
            else:
                return Response({"result": False})
        except Exception as e:
            return Response({"result": str(e)})


class GetUserRoomView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Room.objects.all()
    serializer_class = RoomDataSerializer

    def post(self, request, pk):
        regex = re.compile(
            r'^(?:http|ftp)s?://'
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
            r'localhost|'
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
            r'(?::\d+)?'
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        try:
            req = request.data
            if re.match(regex, req['link']) is not None:
                username_r = req.pop('username')
                req['room'] = pk
                req['user_id'] = CustomUser.objects.get(username=username_r).id
                ser = LinkSerializer(data=req)
                ser.is_valid()
                ser.save()
                return Response({"result": True})
            else:
                return Response({"result": False})
        except Exception as e:
            return Response({"result": str(e)})


class ListLinksView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        regex = re.compile(
            r'^(?:http|ftp)s?://'
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
            r'localhost|'
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
            r'(?::\d+)?'
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        t = Link.objects.filter(room_id=pk)
        data = list()
        for i in t:
            if re.match(regex, i.link) is not None:
                data.append({
                    "id": i.id,
                    "link": i.link,
                    "username_add": CustomUser.objects.get(id=i.user_id).username,
                    "data_creation": i.created_at
                })
        return Response({"result": data})


class DeleteLinkView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Link.objects.all()
    serializer_class = LinkSerializer