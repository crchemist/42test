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
   """
   """
   path = models.CharField(max_length=256)

