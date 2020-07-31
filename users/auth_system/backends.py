from rest_framework import authentication, exceptions
from rest_framework.authtoken.models import Token
from rest_framework.request import WrappedAttributeError

from users.models import CustomUser

# authentication.TokenAuthentication


# authentication.SessionAuthentication
class CustomUserAuth(authentication.BaseAuthentication):

    def authenticate(self, request):
        username = request.data.get('email')
        password = request.data.get('password')
        print(password)
        try:
            user = CustomUser.objects.get(email=username)
            if user.check_password(password):
                print(user)
                return (user, None)
        except CustomUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            user = CustomUser.objects.get(pk=user_id)
            if user.is_active:
                return user
            return None
        except CustomUser.DoesNotExist:
            return None
    # def authenticate_header(self, request):
    #     return self.keyword


class CustomTokenAuthentication(authentication.BaseAuthentication):
    authentication_header_prefix = 'Bearer'

    def authenticate(self, request):

        request.user = None

        # `auth_header` should be an array with two elements: 1) the name of
        # the authentication header (in this case, "Token") and 2) the JWT
        # that we should authenticate against.
        auth_header = authentication.get_authorization_header(request).split()
        auth_header_prefix = self.authentication_header_prefix.lower()

        if not auth_header:
            return None

        if len(auth_header) == 1:
            msg = 'Invalid token header. No credentials provided.'
            raise exceptions.AuthenticationFailed(msg)

        elif len(auth_header) > 2:
            msg = 'Invalid token header. Token string should not contain spaces.'
            raise exceptions.AuthenticationFailed(msg)

        prefix = auth_header[0].decode('utf-8')

        if prefix.lower() != auth_header_prefix:
            return None
        # try to decode token
        try:
            token = auth_header[1].decode()
        except UnicodeError:
            msg = 'Invalid token header. Token string should not contain invalid characters.'
            raise exceptions.AuthenticationFailed(msg)

        return self._authenticate_credentials(token)

    def _authenticate_credentials(self, token):
        """
        Try to authenticate the given credentials. If authentication is
        successful, return the user and token.
        """

        try:
            token = Token.objects.select_related('user').get(key=token)
        except Token.DoesNotExist:
            msg = 'Token invalid.'
            raise exceptions.AuthenticationFailed(msg)
        except WrappedAttributeError:
            msg = 'No user matching this token was found.'
            raise exceptions.AuthenticationFailed(msg)

        if not token.user.is_active:
            msg = 'This user has been deactivated or deleted.'
            raise exceptions.AuthenticationFailed(msg)

        return (token.user, token)
