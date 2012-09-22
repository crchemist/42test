"""Middleware for recording requests to database
"""

from t42cc.models import RequestModel


class RequestMiddleware(object):
    """Save path of each request to database
    """
    def process_request(self, request):
        """Record request to database
        """
        entry = RequestModel(path=request.path,
                   username=request.user.username,
                   method=request.method)
        entry.save()
        return None  # pylint wants this
