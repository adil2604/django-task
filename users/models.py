from django.contrib.auth.base_user import AbstractBaseUser
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models

# Create your models here.
from users.auth_system.managers import CustomUserManager

phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                             message="Phone number must be entered in the format: '+77751234567'.")
SEX = (
    ('male', 'Male'),
    ('female', 'Female')
)


def file_size_validate(file):
    if file.size > 2 * 1024 * 1024:
        raise ValidationError("Image file too large ( > 2mb )")


# Create your models here.
class CustomUser(AbstractBaseUser):
    fullname = models.CharField(max_length=255)
    email = models.EmailField(unique=True, db_index=True)
    sex = models.CharField(choices=SEX, max_length=25)
    date_birth = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='users_pic/', validators=[file_size_validate])
    phone_number = models.CharField(validators=[phone_regex], unique=True, max_length=17)  # validators should be a list
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    password = models.CharField(max_length=255)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fullname', 'phone_number']

    objects = CustomUserManager()

    class Meta:
        db_table = 'auth_users'
        verbose_name = 'Users'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.fullname

    def get_absolute_url(self):
        pass
        # return "/users/%s/" % urlquote(self.email)

    def get_short_name(self):
        "Returns the short name for the user."
        return self.fullname

    def email_user(self, subject, message, from_email=None):
        """
        Sends an email to this User.
        """
        pass

    def get_user(self):
        return self
