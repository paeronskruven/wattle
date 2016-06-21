__author__ = 'Tommy Lundgren'

import os
import sys

from .routing import Router
from .request import Request
from .response import Response, ResponseStatus
from .resource import get_content_type


class NotFoundException(BaseException):
    pass


class InvalidResourceTypeException(BaseException):
    pass


class App:
    response = Response()

    static_path = os.path.join(os.path.dirname(sys.modules['__main__'].__file__), 'static')

    def __init__(self):
        self._router = Router()
        self._router.add_route('/static/<resource>', self._handle_static_resource)

    def route(self, path):
        def decorator(func):
            self._router.add_route(path, func)
            return func

        return decorator

    def _handle_static_resource(self, resource):
        path = os.path.join(self.static_path, resource)
        if os.path.exists(path):
            self.response.headers = [];
            self.response.headers.append(('Content-type', get_content_type(resource)))
            with open(path) as f:
                source = f.read()
            return source
        else:
            raise NotFoundException()

    def _handle_request(self, request):
        self.response.clear()
        self.response.headers = [('Content-type', 'text/html; charset=utf-8')]
        route = self._router.resolve_route(request.path)
        if route:
            self.response.status = ResponseStatus.RESPONSE_STATUS_200
            kwargs, func = route
            self.response.body = func(**kwargs)
        else:
            raise NotFoundException()

    def __call__(self, environ, start_response):
        request = Request(environ)
        try:
            self._handle_request(request)
        except NotFoundException:
            self.response.clear()
            self.response.status = ResponseStatus.RESPONSE_STATUS_404

        start_response(self.response.status, self.response.headers)
        return [self.response.body.encode('utf-8')]
