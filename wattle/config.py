__author__ = 'Tommy Lundgren'

import os
import sys

cfg_path = os.path.join(os.path.dirname(sys.modules['__main__'].__file__), 'config.cfg')
config = {}


class InvalidConfigFormat(BaseException):
    pass


def _default_config():
    """ Default values of the config """
    config['DEBUG'] = False


def str2bool(value):
    if value.lower() == 'true':
        return True
    elif value.lower() == 'false':
        return False
    raise ValueError()


def convert2type(value):
    for fn in (str2bool, int, float):
        try:
            return fn(value)
        except ValueError:
            pass
    return value  # value is a string


def read_config():
    _default_config()
    try:
        with open(cfg_path) as f:
            for line in f.readlines():
                line = line.strip()
                pair = line.split('=')
                if len(pair) != 2:
                    raise InvalidConfigFormat('Invalid config format at line: {}'.format(line))

                config[pair[0]] = convert2type(pair[1])
    except FileNotFoundError:
        pass