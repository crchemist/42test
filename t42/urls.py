from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

import settings

urlpatterns = patterns('',
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root':
       settings.MEDIA_ROOT, 'show_indexes': True}),

    (r'', include('t42cc.urls')),
)
