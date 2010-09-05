"""Print all models names and number of entiries of each model
"""
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    """Implement django-admin.py command
    """
    help = 'Print project models info'

    def __format_output(self, col1, col2):
        """All output formatting stuff must be placed here
        """
        return '%-20s%-20s'%(col1, col2)

    def handle(self, *args, **options):
        """Command handler
        """
        print self.__format_output('Model name', 'Number of entiries')

