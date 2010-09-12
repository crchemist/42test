"""Models definition.
"""
from django.db import models
from django.contrib.admin.models import ADDITION, CHANGE, DELETION
from django.db.models import signals
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User


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
    request_time = models.DateTimeField(auto_now=True)

    class Meta:
        """Metaclass for creating RequestModel class
        """
        ordering = ('-request_time', )

    def __unicode__(self):
        return self.path


class LogModelModification(models.Model):
    """Store information about models modifications.
    """
    action_time = models.DateTimeField(auto_now=True)
    content_type = models.ForeignKey(ContentType, blank=True, null=True)
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()

    class Meta:
        """Metaclass for creating LogModelModification class
        """
        verbose_name = 'log entry'
        ordering = ('-action_time',)

    def __unicode__(self):
        """Represent entry in django.contib.admin and other places
        """
        action_str = 'Unknown action'
        if self.action_flag == ADDITION:
            action_str = 'Added'
        elif self.action_flag == CHANGE:
            action_str = 'Changed'
        elif self.action_flag == DELETION:
            action_str = 'Deleted'
        return '%s: %s' % (action_str, self.object_repr)


def log_modify(sender, instance, created, **kwargs):
    """Create LogModelModification entry each time
    any model is modified.
    """
    if sender is LogModelModification:
        return

    obj_ct = ContentType.objects.get_for_model(sender)
    obj_id = instance.pk
    action_flag = ADDITION if created else CHANGE
    LogModelModification.objects.create(content_type=obj_ct,
                          object_id=obj_id,
                          object_repr=repr(instance),
                          action_flag=action_flag)


def log_delete(sender, instance, **kwargs):
    """Create LogModelModification entry each time
    any entry is deleted.
    """
    if sender is LogModelModification:
        return

    obj_ct = ContentType.objects.get_for_model(sender)
    obj_id = instance.id if hasattr(instance, 'id') else None
    LogModelModification.objects.create(content_type=obj_ct,
                          object_id=obj_id,
                          object_repr=repr(instance),
                          action_flag=DELETION)


signals.post_save.connect(log_modify)
signals.post_delete.connect(log_delete)
