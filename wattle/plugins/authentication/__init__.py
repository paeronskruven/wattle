__author__ = 'Tommy Lundgren'

from wattle.plugins import Plugin
from wattle.response import response, ResponseStatus
from wattle.request import request
from wattle.config import config

AUTH_COOKIE_NAME = 'AUTH_COOKIE_NAME'


class Authentication(Plugin):

    _auth_cookie = None
    _protected_funcs = []

    def init(self):
        if AUTH_COOKIE_NAME not in config:
            config[AUTH_COOKIE_NAME] = 'wattle_auth'

    def process(self, **kwargs):
        # check for an authentication cookie
        try:
            self._auth_cookie = [c for c in request.cookies if c.key == config.get(AUTH_COOKIE_NAME)][0]
        except IndexError:
            pass

        if kwargs['func'] in self._protected_funcs:
            response.status = ResponseStatus.RESPONSE_STATUS_403
            return 'You cant touch this! do dododo bap bap, yeeeaaah'

    def require(self, func):
        self._protected_funcs.append(func)


