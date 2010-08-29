"""Definition of views
"""
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    """Main page
    """
    return HttpResponse('Hello world')
