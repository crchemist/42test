"""Urls configuration
"""

from django.conf.urls.defaults import patterns

urlpatterns = patterns('t42cc.views',
    (r'^$', 'index'),
)
