from django.urls import path

from sait.views import *

urlpatterns = [
    path('new/', CreateRoomView.as_view()),
    path('my_rooms/', GetUserRoomsView.as_view()),
    path('room/<int:pk>/', GetUserRoomView.as_view())
]
