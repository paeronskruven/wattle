__author__ = 'Tommy Lundgren'

import os
import sys
import jinja2


class TemplateEnvironment(jinja2.Environment):

    def __init__(self):
        super().__init__(
            loader=TemplateLoader()
        )


class TemplateLoader(jinja2.BaseLoader):

    def __init__(self):
        app_path = os.path.dirname(sys.modules['__main__'].__file__)
        self.path = os.path.join(app_path, 'templates')

    def get_source(self, environment, template):
        path = os.path.join(self.path, template)
        if not os.path.exists(path):
            raise jinja2.TemplateNotFound(template)
        mtime = os.path.getmtime(path)
        with open(path) as f:
            source = f.read()
        return source, path, lambda: mtime == os.path.getmtime(path)


template_environment = TemplateEnvironment()


def render_template(template_name, **kwargs):
    template = template_environment.get_template(template_name)
    return template.render(**kwargs)