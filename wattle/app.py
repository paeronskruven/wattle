__author__ = 'Tommy Lundgren'

import os
import sys

from .routing import Router
from .request import request
from .response import response, ResponseStatus
from .resource import resourceUtil


class NotFoundException(BaseException):
    pass


class InvalidResourceTypeException(BaseException):
    pass


class App:

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
            response.clear_headers()
            response.add_header(('Content-type', resourceUtil.get_content_type(resource)))
            buffer_mode = 'r'
            if resourceUtil.is_image(resource):
                response.encoding = ''
                buffer_mode = 'rb'
            with open(path, buffer_mode) as f:
                source = f.read()
            return source
        else:
            raise NotFoundException()

    def _handle_request(self):
        response.clear()
        response.add_header(('Content-type', 'text/html; charset=utf-8'))
        response.encoding = 'utf-8'
        route = self._router.resolve_route(request.path)
        if route:
            response.status = ResponseStatus.RESPONSE_STATUS_200
            kwargs, func = route
            response.body = func(**kwargs)
            content_length = str(len(response.body))
            response.add_header(('Content-length', content_length))
        else:
            raise NotFoundException()

    def __call__(self, environ, start_response):
        request.parse_env(environ)

        try:
            self._handle_request()
        except NotFoundException:
            # todo: implement 404 html page
            response.clear()
            response.status = ResponseStatus.RESPONSE_STATUS_404

        start_response(response.status, response.headers)
        response.exec_body_encoding()
        return [response.body]
