import os
import sys
import logging
"""
WSGI config for project.

It exposes the WSGI callable as a module-level variable named ``application``.
"""
from django.core.wsgi import get_wsgi_application

class StubsFilter(logging.Filter):

    def filter(self, record):
        return 'stubs.py' not in record.pathname


logging.root.addFilter(StubsFilter())

#sys.path.insert(0, 'lib')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bakerydemo.settings.production")

app = get_wsgi_application()
application = get_wsgi_application()

def warmup(request):
    """Warm up an instance of the app."""
    logging.info('Warming up.')
