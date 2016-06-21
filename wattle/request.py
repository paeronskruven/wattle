__author__ = 'Tommy Lundgren'

import http.cookies

from .cookie import Cookie


class Request:

    method = None
    path = None
    query_string = None
    content_type = None
    content_length = None
    protocol = None
    _http_cookie = None

    cookies = []

    def __init__(self):
        self._base_cookie = http.cookies.BaseCookie()

    def _parse_cookies(self):
        self._base_cookie.clear()
        if not self._http_cookie:
            return

        self._base_cookie.load(self._http_cookie)
        for key in self._base_cookie:
            self.cookies.append(
                Cookie(
                    self._base_cookie[key].key,
                    self._base_cookie[key].value,
                    **self._base_cookie[key]
                )
            )

    def parse_env(self, env):
        self.method = env.get('REQUEST_METHOD')
        self.path = env.get('PATH_INFO', '')
        self.query_string = env.get('QUERY_STRING')  # todo: parse the querystring to dictionary
        self.content_type = env.get('CONTENT_TYPE')
        self.content_length = env.get('CONTENT_LENGTH')
        self.protocol = env.get('SERVER_PROTOCOL')
        self._http_cookie = env.get('HTTP_COOKIE')

        self._parse_cookies()

request = Request()
