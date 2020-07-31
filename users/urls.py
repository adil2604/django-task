from django.urls import path, include
from .views import CustomUserAPI

urlpatterns = [
    path('me/', CustomUserAPI.as_view()),
    path('auth/',include('users.auth_system.urls'))
]
