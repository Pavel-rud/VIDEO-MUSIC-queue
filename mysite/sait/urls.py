from django.urls import path, include
from sait.views import *

urlpatterns = [
    path('new/', CreateRoomView.as_view()),
    path('my_rooms/', GetUserRoomsView.as_view()),
    path('room/<int:pk>/', GetUserRoomView.as_view()),
    path('links/<int:pk>/', ListLinksView.as_view()),
    path('delete_first_link/<int:pk>/', ListLinksView.as_view()),
    path('add_to_room/', AddUserToRoomView.as_view()),
    # path('delete_link/<int:pk>/', DeleteLinkView.as_view())
]
