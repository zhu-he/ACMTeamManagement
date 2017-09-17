from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Member(models.Model):
    name = models.CharField(max_length=64)
    user = models.OneToOneField(User, blank=True, null=True)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=64)
    owner = models.ForeignKey(User)
    members = models.ManyToManyField(Member)

    def __str__(self):
        return self.name

