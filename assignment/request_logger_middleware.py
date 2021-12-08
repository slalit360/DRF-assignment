import logging
from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger(__name__)


class RequestLoggerMiddleware(MiddlewareMixin):

    def process_request(self, request):
        logger.info(str(request.get_full_path_info()) + ' [' + request.method + '] ')

    def process_response(self, request, response):
        logger.info(str(request.get_full_path_info()) + ' [' + request.method + '] ' + str(request.user) + ' ' + str(
            response.status_code))
        return response