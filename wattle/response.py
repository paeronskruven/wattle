__author__ = 'Tommy Lundgren'

import http.cookies

from .cookie import Cookie


class ResponseStatus:
    # todo: implement all response statuses
    RESPONSE_STATUS_200 = '200 OK'
    RESPONSE_STATUS_404 = '404 NOT FOUND'
    RESPONSE_STATUS_500 = '500 INTERNAL SERVER ERROR'


class Response:

    _status = None
    _headers = []
    _body = ''
    _encoding = ''

    def __init__(self):
        self._base_cookie = http.cookies.BaseCookie()

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

    @property
    def headers(self):
        # add the cookie headers
        for key in self._base_cookie:
            self._headers.append(('Set-Cookie', self._base_cookie[key].OutputString()))
        return self._headers

    @property
    def body(self):
        return self._body

    @body.setter
    def body(self, body):
        self._body = body

    @property
    def encoding(self):
        return self._encoding

    @encoding.setter
    def encoding(self, encoding):
        self._encoding = encoding

    def add_cookie(self, cookie):
        if not isinstance(cookie, Cookie):
            raise TypeError('Excepted <class wattle.cookie.Cookie>, got {}'.format(type(cookie)))

        self._base_cookie[cookie.key] = cookie.value
        self._base_cookie[cookie.key]['path'] = cookie.path
        # todo: implement the rest of the cookie attributes

    def add_header(self, header):
        self._headers.append(header)

    def clear_headers(self):
        self._headers = []

    def clear(self):
        self._status = None
        self._headers = []
        self._body = ''
        self._base_cookie.clear()

    def exec_body_encoding(self):
        if self._encoding != '':
            self._body = self.body.encode(self._encoding)

response = Response()