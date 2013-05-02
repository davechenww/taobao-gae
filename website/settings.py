import os

import jinja2


DEBUG = False

STATIC_URL = '/static'
STATIC_PATH = os.path.join(os.path.dirname(__file__), 'static')

TEMPLATES_PATH = os.path.join(os.path.dirname(__file__), 'templates')

try:
    from local_settings import *
except Exception:
    pass

JINJA_ENVIRONMENT = \
        jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATES_PATH))

