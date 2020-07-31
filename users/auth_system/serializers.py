from django.core import exceptions
from rest_framework import serializers
import django.contrib.auth.password_validation as validators
from users.auth_system.backends import CustomUserAuth
from users.models import CustomUser
from django.contrib.auth import authenticate


class RegisterSerializer(serializers.ModelSerializer):
    """Registration serializer"""
    password = serializers.CharField(max_length=255, style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['fullname', 'email', 'phone_number', 'password']

    def validate_password(self, data):

        errors = dict()
        try:
            # validate the password and catch the exception
            validators.validate_password(password=data)

        # the exception raised here is different than serializers.ValidationError
        except exceptions.ValidationError as e:
            errors['password'] = list(e.messages)

        if errors:
            raise serializers.ValidationError(errors)

        return super(RegisterSerializer, self).validate(data)

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    class Meta:
        model = CustomUser
        fields = ['email', 'password']

    # def validate(self, attrs):
    #     user, = authenticate(**attrs)
    #     print(user)
    #     # user=TokenAuthentication().authenticate(attrs)
    #     if user and user.is_active:
    #         return user
    #     elif not user:
    #         raise serializers.ValidationError({"status": "Incorrect data"})
    #     elif not user.is_active:
    #         raise serializers.ValidationError({"status": "CustomUser not active"})
