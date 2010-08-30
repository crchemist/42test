"""Models definition.
"""
from django.db import models


class Person(models.Model):
    """Represent person's data
    """

    name = models.CharField(max_length=250)
    surname = models.CharField(max_length=250)
    bio = models.TextField()
    contacts = models.TextField()


class RequestModel(models.Model):
    """Store path of each request
    """
    path = models.CharField(max_length=256)
    username = models.CharField(max_length=256, blank=True)
    method = models.CharField(max_length=256)
