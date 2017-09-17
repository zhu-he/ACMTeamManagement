from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Member, Team, Group, Board, OJ, Contest, Problem, RankItem, ScoreItem, Alias


class ProblemInline(admin.TabularInline):
    model = Problem
    extra = 0


class RankItemInline(admin.TabularInline):
    model = RankItem
    extra = 0


class ContestAdmin(admin.ModelAdmin):
    inlines = [ProblemInline, RankItemInline]


admin.site.register(User, UserAdmin)
admin.site.register(Member)
admin.site.register(Team)
admin.site.register(Group)
admin.site.register(Board)
admin.site.register(OJ)
admin.site.register(Contest, ContestAdmin)
admin.site.register(Alias)
