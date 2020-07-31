from django.shortcuts import render
from django.utils.crypto import get_random_string
from rest_framework import generics, status, permissions, authentication

# Create your views here.
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .backends import CustomUserAuth
from .managers import CustomUserManager
from .serializers import RegisterSerializer, LoginSerializer
from users.serializers import CustomUserSerializer


class RegisterAPI(generics.CreateAPIView):
    serializer_class = RegisterSerializer


# @method_decorator(csrf_exempt, name='dispatch')
class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer
    authentication_classes = [
        CustomUserAuth
    ]
    permission_classes = [
        permissions.AllowAny
    ]

    # @csrf_exempt
    def post(self, request, *args, **kwargs):

        user = request.user
        if user is not None:
            if user and user.is_active:
                token, created = Token.objects.get_or_create(user=user)
                return Response({
                    "user": CustomUserSerializer(user, context=self.get_serializer_context()).data,
                    "token": token.key
                }, status=status.HTTP_202_ACCEPTED)
            else:
                return Response({'status':'not auth'},status=401)

