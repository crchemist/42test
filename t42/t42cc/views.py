"""Definition of views
"""
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django import forms
from django.core.urlresolvers import reverse

from t42cc.models import Person


def index(request):
    """Main page
    """
    person = Person.objects.get()
    return render_to_response('person.html',
                 {'person': person}, context_instance=RequestContext(request))

class PersonForm(forms.ModelForm):
    """Form for Person model
    """
    class Meta:
        model = Person

def edit(request):
    """/edit - Edit person information
    """
    person = Person.objects.get(id=1)
    if request.method != 'POST':
        form = PersonForm(instance=person)
        return render_to_response('person_edit.html',
                   {'form': form}, context_instance=RequestContext(request))
    return HttpResponseRedirect(reverse(index))

