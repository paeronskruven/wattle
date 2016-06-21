__author__ = 'Tommy Lundgren'


class Cookie:

    def __init__(self, key, value, **kwargs):
        self.key = key
        self.value = value
        self.path = kwargs.get('path')

        # todo: implement these
        self.expires = None
        self.comment = None
        self.domain = None
        self.max_age = None
        self.secure = None
        self.version = None
        self.http_only = None