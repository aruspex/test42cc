from .models import HttpRequestInfo


class HttpRequestStorageMiddleware(object):
    """
    Stores all HTTP requests in database
    """

    def process_request(self, request):
        request_params = {
            'method': request.method,
            'path': request.get_full_path(),
            'is_ajax': request.is_ajax()
        }
        HttpRequestInfo.objects.create(**request_params)
