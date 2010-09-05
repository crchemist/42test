"""Print all models names and number of entiries of each model
"""
from django.core.management.base import BaseCommand, CommandError
from django.db import models, router, DEFAULT_DB_ALIAS


class Command(BaseCommand):
    """Implement django-admin.py command
    """
    help = 'Print project models info'

    def __format_output(self, col1, col2):
        """All output formatting stuff must be placed here
        """
        return '%-50s%-20s'%(col1, col2)

    def __print(self, model_name, entries_count):
        print self.__format_output(model_name, entries_count)

    def handle(self, *args, **options):
        """Command handler
        """
        print self.__format_output('Model name', 'Number of entiries')
        for app in models.get_apps():
            for app_model in models.get_models(app, include_auto_created=True):
                self.__print('%s:%s' % (app.__name__, app_model.__name__),
                             app_model.objects.count())
