from django.conf import settings


def django_settings(request):
    """Add project settings to template context
    """
    return {'django_settings': settings}
