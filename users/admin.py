from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import Group, User

from users.models import CustomUser

admin.site.register(CustomUser)
admin.site.unregister(Group)
# admin.site.unregister(User)
