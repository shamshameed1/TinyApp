from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import User, Url

admin.site.register(User, UserAdmin)
admin.site.register(Url)

# Register your models here.
