__author__ = 'Tommy Lundgren'


class ResponseStatus:
    # todo: implement all response statuses
    RESPONSE_STATUS_200 = '200 OK'
    RESPONSE_STATUS_404 = '404 NOT FOUND'


class Response:

    status = None
    headers = []
    body = ''