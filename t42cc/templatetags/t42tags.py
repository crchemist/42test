"""t42cc tags library
"""
from django import template
from django.core.urlresolvers import reverse
from django.contrib.contenttypes.models import ContentType

register = template.Library()


def edit_link(obj):
    """Usage: {% edit_link some_obj %}
    """
    obj_ct = ContentType.objects.get_for_model(obj.__class__)
    return reverse('admin:%s_%s_change' % (obj_ct.app_label, obj_ct.name),
                args=(obj.id,))

register.simple_tag(edit_link)
