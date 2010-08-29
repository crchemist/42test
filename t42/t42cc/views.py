"""Definition of views
"""
from django.shortcuts import render_to_response

from t42cc.models import Person


def index(request):
    """Main page
    """
    person = Person.objects.get()
    return render_to_response('person.html',
                 {'person': person})
