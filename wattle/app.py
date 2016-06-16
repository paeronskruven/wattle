__author__ = 'Tommy Lundgren'

from .routing import Router
from .request import Request
from .response import Response, ResponseStatus


class App:

    def __init__(self):
        self._router = Router()

    def route(self, path):
        def decorator(func):
            self._router.add_route(path, func)
            return func
        return decorator

    def _handle_request(self, request):
        response = Response()
        # todo: determine if the request is for an static resource before trying to match an route

        response.headers = [('Content-type', 'text/html; charset=utf-8')]
        route = self._router.resolve_route(request.path)
        if route:
            response.status = ResponseStatus.RESPONSE_STATUS_200
            kwargs, func = route
            response.body = func(**kwargs)
        else:
            response.status = ResponseStatus.RESPONSE_STATUS_404
            response.body = '404 page'

        return response

    def __call__(self, environ, start_response):
        request = Request(environ)
        response = self._handle_request(request)

        start_response(response.status, response.headers)
        return [response.body.encode('utf-8')]