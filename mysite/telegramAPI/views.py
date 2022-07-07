from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from sait.serializer import *


class RoomViewList(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomViewOne(generics.RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class LinkViewSave(generics.CreateAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer


class LinkAddView(APIView):
    def post(self, request):
        ser = request.data.dict()
        print(ser, type(ser))
        password_message = ser.pop("password")
        try:
            Room.objects.get(password_room=password_message)
            ser = LinkSerializer(data=ser)
            ser.is_valid(raise_exception=True)
            ser.save()
            print('add true')
            return Response({"result": True})
        except Exception as e:
            print('add false')
            return Response({"result": str(e)})
