__author__ = 'Tommy Lundgren'

import os
import sys
import traceback

from .routing import Router
from .request import request
from .response import response, ResponseStatus
from .resource import get_resource_type_data


class NotFoundException(BaseException):
    pass


class App:

    static_path = os.path.join(os.path.dirname(sys.modules['__main__'].__file__), 'static')

    def __init__(self):
        self._router = Router()
        self._router.add_route('/static/<resource>', self._handle_static_resource)

        self._preprocessors = []

    def route(self, path):
        def decorator(func):
            self._router.add_route(path, func)
            return func

        return decorator

    def add_preprocessor(self, pp):
        self._preprocessors.append(pp)

    def _handle_static_resource(self, resource):
        path = os.path.join(self.static_path, resource)
        if os.path.exists(path):
            content_type, buffer_mode = get_resource_type_data(resource)
            response.add_header(('Content-type', content_type))
            with open(path, buffer_mode) as f:
                source = f.read()
            return source
        else:
            raise NotFoundException('Could not find resource: {}'.format(resource))

    def _handle_preprocessors(self, func, kwargs):
        for pp in self._preprocessors:
            retval = pp(func=func, **kwargs)
            if retval:
                return retval
        return None

    def _handle_request(self):
        response.reset()

        route = self._router.resolve_route(request.path)
        if route:
            kwargs, func = route

            retval = self._handle_preprocessors(func, kwargs)
            if not retval:
                retval = func(**kwargs)

            response.body = retval
            # if no status has been set assume 200 OK
            if not response.status:
                response.status = ResponseStatus.RESPONSE_STATUS_200
            # if no content-type has been set assume text/html
            if not response.get_header('Content-type'):
                response.add_header(('Content-type', 'text/html; charset=utf-8'))
        else:
            raise NotFoundException('Could not find route on path: {}'.format(request.path))

    def __call__(self, environ, start_response):
        request.parse_env(environ)

        try:
            self._handle_request()
        except NotFoundException:
            # todo: implement 404 html page
            response.reset()
            response.status = ResponseStatus.RESPONSE_STATUS_404
        except:
            response.reset()
            response.status = ResponseStatus.RESPONSE_STATUS_500
            response.body = traceback.format_exc()

        start_response(response.status, response.headers)
        return [response.body]
