from django.conf.urls.defaults import *
from django.contrib.auth.views import login, logout_then_login

from django.contrib import admin
admin.autodiscover()

import settings

urlpatterns = patterns('',
    (r'^accounts/login/$',  login),
    (r'^accounts/logout/$', logout_then_login),

    (r'^admin/', include(admin.site.urls)),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),

    (r'', include('t42cc.urls')),
)
