__author__ = 'Tommy Lundgren'

import http.cookies

from .cookie import Cookie


class ResponseStatus:
    # todo: implement all response statuses
    RESPONSE_STATUS_200 = '200 OK'
    RESPONSE_STATUS_403 = '403 Forbidden'
    RESPONSE_STATUS_404 = '404 Not Found'
    RESPONSE_STATUS_500 = '500 Internal Server Error'


class Response:

    _status = None
    _headers = []
    _body = ''
    _encoding = 'utf-8'  # default encoding

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
        # add the content length
        self._headers.append(('Content-length', str(len(response.body))))
        return self._headers

    @property
    def body(self):
        if isinstance(self._body, str):
            return self._body.encode(self._encoding)
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

    def get_header(self, name):
        for header in self._headers:
            if header[0] == name:
                return header
        return None

    def clear_headers(self):
        self._headers = []

    def clear(self):
        self._status = None
        self._headers = []
        self._body = ''
        self._base_cookie.clear()

response = Response()