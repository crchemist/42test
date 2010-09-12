"""Definition of views
"""
import json

from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django import forms
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from t42cc.models import Person
from t42cc.widgets import CalendarWidget


def index(request):
    """Main page
    """
    person = Person.objects.get()
    return render_to_response('person.html',
                 {'person': person}, context_instance=RequestContext(request))


class PersonForm(forms.ModelForm):
    """Form for Person model
    """
    def __init__(self, *args, **kw):
        super(PersonForm, self).__init__(*args, **kw)
        self.fields.keyOrder.reverse()

    class Meta:
        """Metaclass for constucting PersonForm class
        """
        model = Person
        widgets = {
             'birth': CalendarWidget(),
        }


@login_required
def edit(request):
    """/edit - Edit person information
    """
    person = Person.objects.get(id=1)
    if request.method != 'POST':
        form = PersonForm(instance=person)
        return render_to_response('person_edit.html',
                   {'form': form}, context_instance=RequestContext(request))
    # Ajax part is taken here http://djangosnippets.org/snippets/992/
    # and little modified to be more pythonic
    resp_dict = {'bad': False}
    form = PersonForm(request.POST, instance=person)
    if form.is_valid():
        form.save()
        if request.is_ajax():
            return HttpResponse(json.dumps(resp_dict, ensure_ascii=False),
                                mimetype='application/json')
        else:
            return HttpResponseRedirect(reverse(index))
    else:
        if request.is_ajax():
            resp_dict['bad'] = True
            errs = {}
            for item_id, err_val in form.errors.items():
                errs[item_id] = unicode(err_val)
            resp_dict['errs'] = errs
            return HttpResponse(json.dumps(resp_dict, ensure_ascii=False),
                                mimetype='application/json')

        else:
            return render_to_response('person_edit.html',
                   {'form': form}, context_instance=RequestContext(request))
