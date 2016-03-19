"""The ship's log."""
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Ship(models.Model):
    """A startship."""

    name = models.CharField(max_length=128)
    capacity = models.IntegerField(
        blank=True, null=True, help_text='Max number of passengers'
    )
    passengers = models.ManyToManyField(User, blank=True)


class Log(models.Model):
    """A log, you know, for logging stuff, like a ship's log."""

    user = models.ForeignKey(User, related_name='logs')
    ship = models.ForeignKey('Ship', related_name='logs')
    message = models.TextField(null=True, blank=True)
    title = models.CharField(max_length=128)
    captains_log = models.BooleanField(default=False, blank=True)
