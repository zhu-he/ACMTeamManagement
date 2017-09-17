from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=64)
    owner = models.ForeignKey('base.User')
    teams = models.ManyToManyField('base.Team')

    def __str__(self):
        return self.name


class Board(models.Model):
    name = models.CharField(max_length=64)
    owner = models.ForeignKey('base.User')
    groups = models.ManyToManyField(Group)

    def __str__(self):
        return self.name

