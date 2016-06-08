from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Restaurant(models.Model):
    name            = models.CharField(max_length=255)
    description     = models.TextField(blank=True)
    address         = models.CharField(max_length=255, blank = True)
    active          = models.BooleanField(default=True)

class History(models.Model):
    restaurant      = models.ForeignKey(Restaurant, on_delete=models.PROTECT)
    date            = models.DateField(auto_now_add = True)

class Votes(models.Model):
    user            = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant      = models.ForeignKey(Restaurant, on_delete=models.SET_NULL, null=True)
    veto            = models.BooleanField(default=false)
    timestamp       = models.DateTimeField(auto_now_add = True)
