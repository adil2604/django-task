from django.shortcuts import render
from django.utils.crypto import get_random_string
from rest_framework import generics, status, permissions

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .backends import CustomUserAuth
from .managers import CustomUserManager
from .serializers import RegisterSerializer, LoginSerializer
from users.serializers import CustomUserSerializer


class RegisterAPI(generics.CreateAPIView):
    serializer_class = RegisterSerializer


# @method_decorator(csrf_exempt, name='dispatch')
class LoginAPI(generics.CreateAPIView):
    serializer_class = LoginSerializer
    authentication_classes = [
        CustomUserAuth
    ]
    permission_classes = [
        permissions.AllowAny
    ]

    # @csrf_exempt
    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        print()

        if user is not None:
            if user and user.is_active:
                return Response({
                    "user": CustomUserSerializer(user, context=self.get_serializer_context()).data,
                }, status=status.HTTP_202_ACCEPTED)
            else:
                return Response(serializer.errors)
