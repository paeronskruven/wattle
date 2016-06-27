# Static resource: (Content Type Header, Buffer Mode, Encoding)
_static_resources = {
    'html': ('text/html; charset=utf-8', 'r', 'utf-8'),
    'css': ('text/css; charset=utf-8', 'r', 'utf-8'),
    'js': ('application/javascript; charset=utf-8', 'r', 'utf-8'),
    'jpeg': ('image/jpeg', 'rb', ''),
    'jpg': ('image/jpeg', 'rb', ''),
    'png': ('image/png', 'rb', '')
}


def get_resource_type_data(resource):
    suffix = _get_file_suffix(resource)

    return _static_resources.get(suffix)


def _get_file_suffix(resource):
    delim = resource.rfind('.')
    suffix = resource[delim + 1:]

    return suffix
