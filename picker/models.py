from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Restaurant(models.Model):
    name            = models.CharField(max_length=255)
    description     = models.TextField(blank=True)
    address         = models.CharField(max_length=255, blank = True)
    active          = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Option(models.Model):
    restaurant      = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    vetoed          = models.BooleanField(default=False)

class History(models.Model):
    restaurant      = models.ForeignKey(Restaurant, on_delete=models.PROTECT)
    date            = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.date.strftime('%Y-%m-%d')

class Vote(models.Model):
    user            = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant      = models.ForeignKey(Restaurant, on_delete=models.SET_NULL, null=True)
    veto            = models.BooleanField(default=False)
    timestamp       = models.DateTimeField(auto_now_add=True)
