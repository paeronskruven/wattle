__author__ = 'Tommy Lundgren'

import re


class RouteException(BaseException):
    pass


class Router:

    def __init__(self):
        self._routes = []

    @staticmethod
    def compile_route(path):
        regex = re.sub(r'(<\w+>)', r'(?P\1.+)', path)
        return re.compile('^{}$'.format(regex))

    def add_route(self, path, func):
        pattern = self.compile_route(path)
        if len([p for p in self._routes if p[0] == pattern]) > 0:
            raise RouteException('Route "{}" already exists'.format(path))
        self._routes.append((pattern, func))

    def resolve_route(self, path):
        for pattern, func in self._routes:
            match = pattern.match(path)
            if match:
                return match.groupdict(), func
        return None
