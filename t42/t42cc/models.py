"""Models definition.
"""
from django.db import models
from django.db.models import signals
from django.contrib.admin.models import LogEntry


class Person(models.Model):
    """Represent person's data
    """

    name = models.CharField(max_length=250)
    surname = models.CharField(max_length=250)
    birth = models.CharField(max_length=12, blank=True, null=True)
    bio = models.TextField()
    contacts = models.TextField()

    def save(self):
        """Implement Singleton pattern
        """
        self.id = 1
        super(Person, self).save()

    def delete(self, *args):
        """Do nothing
        """
        pass


class RequestModel(models.Model):
    """Store path of each request
    """
    path = models.CharField(max_length=256)
    username = models.CharField(max_length=256, blank=True)
    method = models.CharField(max_length=256)

    def __unicode__(self):
        return self.path


class LogModelModification(LogEntry):
    """Store information about models modifications.
    """


def log_modify(sender, instance, **kwargs):
    """Create LogModelModification entry each time
    any model is modified.
    """
    pass


def log_delete(sender, instance, **kwargs):
    """Create LogModelModification entry each time
    any entry is deleted.
    """
    pass


signals.post_save.connect(log_modify)
signals.post_delete.connect(log_delete)
