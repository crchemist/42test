"""t42cc custom widgets
"""
from django.forms.widgets import DateInput


class CalendarWidget(DateInput):
    """jQuery datepicker widget
    """
    format = '%m/%d/%Y'
    class Media:
        """Include jquery.ui.datepicker media
        """
        js = ('/static/js/calendar.js',)

