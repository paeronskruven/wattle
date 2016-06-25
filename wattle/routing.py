__author__ = 'Tommy Lundgren'

import re

# flags
REQUIRE_AUTHORIZATION = 1


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
        self._routes.append((pattern, func, 0))

    def add_flags(self, func, flag):
        try:
            route = [route for route in self._routes if route[1] == func][0]
            index = self._routes.index(route)
            self._routes[index] = (route[0], route[1], route[2] + flag)
        except IndexError:
            raise RouteException(
                'Error when adding flag {0} to {1}, make sure the route has been added before adding adding flag'
                .format(flag, func)
            )

    def resolve_route(self, path):
        for pattern, func, flags in self._routes:
            match = pattern.match(path)
            if match:
                return match.groupdict(), func, flags
        return None
