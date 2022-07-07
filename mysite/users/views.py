from django.http import JsonResponse, HttpResponse
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CustomUser
from .serializer import UserSerializer
from rest_framework.permissions import IsAuthenticated


class UserViewList(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class GetAvataeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        username_r = request.data["username"]
        user = CustomUser.objects.get(username=username_r)
        print(user.avatar)
        return HttpResponse(user.avatar)
