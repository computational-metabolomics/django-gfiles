# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from gfiles.models import GenericFile, User

# class CustomUserAdmin(UserAdmin):
#     model = User
#     list_display = ['email', 'username']


admin.site.register(User, UserAdmin)
admin.site.register(GenericFile)
