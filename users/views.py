from rest_framework import generics, permissions

from .auth_system.backends import CustomUserAuth
from .models import CustomUser
from .serializers import CustomUserSerializer


# Create your views here.
class CustomUserAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get_object(self):
        return CustomUser.objects.get(id=self.request.user.id)
