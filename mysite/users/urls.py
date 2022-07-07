from django.conf.urls.static import static
from django.urls import path, include, re_path

from mysite import settings
from users.views import GetAvataeView

urlpatterns = [
    path('auth/', include('djoser.urls')),
    re_path('auth/', include('djoser.urls.authtoken')),
    path('auth_drf/', include('rest_framework.urls')),
    path('avatar/', GetAvataeView.as_view()),
]

