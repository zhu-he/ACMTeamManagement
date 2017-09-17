from django.contrib import admin
from .models import OJ, Contest, Problem, RankItem, ScoreItem, Alias


class ProblemInline(admin.TabularInline):
    model = Problem
    extra = 0


class RankItemInline(admin.TabularInline):
    model = RankItem
    extra = 0


class ContestAdmin(admin.ModelAdmin):
    inlines = [ProblemInline, RankItemInline]


admin.site.register(OJ)
admin.site.register(Contest, ContestAdmin)
admin.site.register(Alias)
