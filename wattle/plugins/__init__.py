__author__ = 'Tommy Lundgren'


class Plugin:

    def __init__(self, app):
        self.app = app
        self.app.add_plugin(self.process)

    def init(self):
        """ Override this to add initialization-logic to an plugin """
        pass

    def process(self, **kwargs):
        raise NotImplementedError()
