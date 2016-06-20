__author__ = 'Tommy Lundgren'


class Request:

    def __init__(self, env):
        self.method = env.get('REQUEST_METHOD')
        self.path = env.get('PATH_INFO', '')
        self.query_string = env.get('QUERY_STRING')  # todo: parse the querystring to dictionary
        self.content_type = env.get('CONTENT_TYPE')
        self.content_length = env.get('CONTENT_LENGTH')
        self.protocol = env.get('SERVER_PROTOCOL')
        self.http_cookie = env.get('HTTP_COOKIE')

