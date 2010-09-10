"""Models admin interface
"""
from t42cc.models import RequestModel, Person, LogModelModification
from django.contrib import admin

admin.site.register(RequestModel)
admin.site.register(Person)
admin.site.register(LogModelModification)
