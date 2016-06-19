
class ResourceUtil:

    @staticmethod
    def _get_content_type(resource):
        delim = resource.rfind('.')
        suffix = resource[delim + 1:]

        def content_type_switch(suffix):
            return {
                'html': 'text/html; charset=utf-8',
                'css': 'text/css; charset=utf-8',
                'js': 'text/javascript; charset=utf-8'
            }.get(suffix)

        return content_type_switch(suffix)