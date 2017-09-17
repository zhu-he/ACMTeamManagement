from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Member, Team, Group, Board


admin.site.register(User, UserAdmin)
admin.site.register(Member)
admin.site.register(Team)
admin.site.register(Group)
admin.site.register(Board)
