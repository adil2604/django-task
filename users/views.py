from rest_framework import generics
from .models import CustomUser
from .serializers import CustomUserSerializer


# Create your views here.
class CustomUserAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()

    def get_object(self):
        return CustomUser.objects.get(id=self.request.user.id)
