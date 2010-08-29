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

    def save(self):
        """Implement Singleton pattern
        """
        self.id = 1
        super(Person, self).save()

    def delete(self):
        """Do nothing
        """
        pass


class RequestModel(models.Model):
    """Store path of each request
    """
    path = models.CharField(max_length=256)
