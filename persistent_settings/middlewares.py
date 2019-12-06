import logging

from persistent_settings.models import Variable

_LOGGER = logging.getLogger(__name__)


class PersistentSettingsMiddleware:
    """
    A middleware for persistent settings.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        self.process_request(request)
        return self.get_response(request)

    def process_request(self, request):
        """
        Injects `persistent_settings` into the request instance.
        """
        _LOGGER.debug("Injecting `persistent_settings` into the request instance...")
        request.persistent_settings = Variable.objects
