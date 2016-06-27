__author__ = 'Tommy Lundgren'


class Extension:

    def __init__(self, app):
        self.app = app
        self.app.add_preprocessor(self.process)

    def process(self, **kwargs):
        raise NotImplementedError()
