from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import UserProfileInfo

# Register your models here.

admin.site.register(UserProfileInfo, UserAdmin)