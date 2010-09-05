"""Models admin interface
"""
from t42cc.models import RequestModel, Person
from django.contrib import admin

admin.site.register(RequestModel)
admin.site.register(Person)
