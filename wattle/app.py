__author__ = 'Tommy Lundgren'

from .routing import Router


class App:

    def __init__(self):
        self._router = Router()

    def route(self, path):
        def decorator(func):
            self._router.add_route(path, func)
            return func
        return decorator

    def __call__(self, environ, start_response):
        path = environ.get('PATH_INFO')
        route = self._router.resolve_route(path)
        if route:
            kwargs, func = route
            content = func(**kwargs)
            status = '200 OK'
            headers = [('Content-type', 'text/html; charset=utf-8')]
        else:
            status = '404 NOT FOUND'
            headers = [('Content-type', 'text/html; charset=utf-8')]
            content = 'whoops'

        start_response(status, headers)
        return [content.encode('utf-8')]