class InvalidResourceTypeException(BaseException):
    pass

# Static resource: (Content Type Header, Buffer Mode, Encoding)
_static_resources = {
    'html': ('text/html; charset=utf-8', 'r'),
    'css': ('text/css; charset=utf-8', 'r'),
    'js': ('application/javascript; charset=utf-8', 'r'),
    'jpeg': ('image/jpeg', 'rb'),
    'jpg': ('image/jpeg', 'rb'),
    'png': ('image/png', 'rb')
}


def get_resource_type_data(resource):
    suffix = _get_file_suffix(resource)

    resource = _static_resources.get(suffix)
    if not resource:
        raise InvalidResourceTypeException('Resource type: {} is invalid'.format(suffix))

    return resource


def _get_file_suffix(resource):
    delim = resource.rfind('.')
    suffix = resource[delim + 1:]

    return suffix
