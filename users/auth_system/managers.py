from datetime import datetime

from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):

    def _create_user(self, password, fullname, email
                     , phone_number, is_active=True
                     , **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        now = datetime.now()

        user = self.model(is_active=is_active, fullname=fullname, email=email,
                          phone_number=phone_number,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, password,
                    phone_number,
                    fullname, email,
                    is_active=True, **extra_fields):
        return self._create_user(password, phone_number=phone_number, fullname=fullname, email=email,
                                 is_active=is_active, **extra_fields)

    def create_superuser(self, password,
                         phone_number,
                         fullname, email,
                         is_active=True, **extra_fields):
        return self._create_user(password, phone_number=phone_number, fullname=fullname,email=email,
                                 is_active=is_active, **extra_fields)
