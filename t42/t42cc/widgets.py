"""t42cc custom widgets
"""
from django.forms.widgets import DateInput


class CalendarWidget(DateInput):
    """jQuery datepicker widget
    """
    class Media:
        """Include jquery.ui.datepicker media
        """

