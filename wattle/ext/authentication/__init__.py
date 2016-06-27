__author__ = 'Tommy Lundgren'

from wattle.ext import Extension
from wattle.response import response, ResponseStatus


class Authentication(Extension):

    _protected_funcs = []

    def process(self, **kwargs):
        if kwargs['func'] in self._protected_funcs:
            response.status = ResponseStatus.RESPONSE_STATUS_403
            return 'You cant touch this! do dododo bap bap, yeeeaaah'

    def require(self, func):
        self._protected_funcs.append(func)


