

_content_type_switch = {
    'html': 'text/html; charset=utf-8',
    'css': 'text/css; charset=utf-8',
    'js': 'text/javascript; charset=utf-8'
}


def get_content_type(resource):
    delim = resource.rfind('.')
    suffix = resource[delim + 1:]

    return _content_type_switch.get(suffix)