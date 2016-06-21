class ResourceUtil:
    _content_type_headers = {
        'html': 'text/html; charset=utf-8',
        'css': 'text/css; charset=utf-8',
        'js': 'application/javascript; charset=utf-8',
        'jpeg': 'image/jpeg',
        'jpg': 'image/jpeg',
        'png': 'image/png'
    }

    _image_types = [
        'png',
        'jpg',
        'jpeg'
    ]


    def get_content_type(self, resource):
        suffix = self._get_file_suffix(resource)

        return self._content_type_headers.get(suffix)

    def is_image(self, resource):
        suffix = self._get_file_suffix(resource)

        if suffix in self._image_types:
            return True
        return False

    def _get_file_suffix(self, resource):
        delim = resource.rfind('.')
        suffix = resource[delim + 1:]

        return suffix

resourceUtil = ResourceUtil()
