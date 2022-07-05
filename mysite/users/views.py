from django.http import JsonResponse
from rest_framework import generics
from rest_framework.views import APIView

from .models import CustomUser
from .serializer import UserSerializer


class UserViewList(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
