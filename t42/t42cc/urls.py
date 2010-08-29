"""Urls configuration
"""

from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('t42cc.views',
    (r'^$', 'index'),
)
