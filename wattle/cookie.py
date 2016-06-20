__author__ = 'Tommy Lundgren'

import http.cookies


class CookieCollectionException(BaseException):
    pass


class CookieCollection(dict):

    def __init__(self):
        super().__init__()
        self._cookie = http.cookies.BaseCookie()

    def clear(self):
        super().clear()
        self._cookie.clear()

    def __setitem__(self, key, value):
        if key in self:
            raise CookieCollectionException('Cookie key: {} already added to the collection'.format(key))

        self._add_cookie(value)
        super().__setitem__(key, value)

    def parse_request(self, http_cookie):
        self._cookie.load(http_cookie)
        for key in self._cookie:
            Cookie.from_http_cookie(self._cookie[key])

    def update_cookie(self, cookie):
        if cookie.key not in self._cookie:
            raise CookieCollectionException('Cannot update cookie: {}, doesnt exist'.format(cookie.key))

        self._add_cookie(cookie)

    def _add_cookie(self, cookie):
        self._cookie[cookie.key] = cookie.value
        self._cookie[cookie.key]['path'] = cookie.path
        # todo: implement the rest of the cookie properties

    def get_output(self, key):
        return self._cookie[key].OutputString()

cookie_collection = CookieCollection()


class Cookie:

    def __init__(self, key, value, **kwargs):
        self._key = key
        self._value = value
        self._path = kwargs.get('path')

        # todo: implement these
        self._expires = None
        self._comment = None
        self._domain = None
        self._max_age = None
        self._secure = None
        self._version = None
        self._http_only = None

        # when send is set to True the cookie will be passed to the client
        self.send = False

        # add the cookie to the cookie collection
        cookie_collection[self._key] = self  # todo: handle exception

    @classmethod
    def from_http_cookie(cls, http_cookie):
        return cls(http_cookie.key, http_cookie.value, **http_cookie)

    @property
    def key(self):
        return self._key

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
        cookie_collection.update_cookie(self)
        self.send = True

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, path):
        self._path = path
        cookie_collection.update_cookie(self)
        self.send = True

    def get_header(self):
        return 'Set-Cookie', cookie_collection.get_output(self._key)