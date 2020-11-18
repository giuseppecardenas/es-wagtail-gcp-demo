import os
import random
import string

import dj_database_url
import django_cache_url

from .base import *  # noqa: F403

DEBUG = False

# # Make sure Django can detect a secure connection properly on Heroku:
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
#
# # Redirect all requests to HTTPS
# SECURE_SSL_REDIRECT = os.getenv('DJANGO_SECURE_SSL_REDIRECT', 'off') == 'on'

# Accept all hostnames, since we don't know in advance which hostname will be used for any given Heroku instance.
# IMPORTANT: Set this to a real hostname when using this in production!
# See https://docs.djangoproject.com/en/1.10/ref/settings/#allowed-hosts
ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', '*').split(';')

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# BASE_URL required for notification emails
BASE_URL = 'http://localhost:8000'

# db_from_env = dj_database_url.config(conn_max_age=500)
# DATABASES['default'].update(db_from_env)

# Override settings here
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.environ.get('DATABASE_HOST', 'db'),
        'NAME': os.environ.get('DATABASE_NAME', 'app_db'),
        'USER': os.environ.get('DATABASE_USER', 'app_user'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD', 'changeme'),
        'PORT': '5432',
    }
}

# configure CACHES from CACHE_URL environment variable (defaults to locmem if no CACHE_URL is set)
CACHES = {'default': django_cache_url.config()}

# Configure Elasticsearch, if present in os.environ
ELASTICSEARCH_ENDPOINT = os.getenv('ELASTICSEARCH_ENDPOINT', '')


WAGTAILSEARCH_BACKENDS = {
    'default': {
        'BACKEND': 'wagtail.search.backends.elasticsearch6',
        'URLS': ['http://10.128.0.2:9200'],
        'INDEX': 'wagtail',
        'TIMEOUT': 5,
        'OPTIONS': {},
        'INDEX_SETTINGS': {
            'settings': {
                'analysis': {
                    'analyzer': {
                        'rebuilt_standard_default': {
                            'tokenizer': 'classic',
                            'filter': [
                                'lowercase'
                            ]
                        },
                    },
                },
            }
        },
    },
    'russian': {
        'BACKEND': 'wagtail.search.backends.elasticsearch6',
        'URLS': ['http://10.128.0.2:9200'],
        'INDEX': 'russian',
        'TIMEOUT': 5,
        'OPTIONS': {},
        'INDEX_SETTINGS': {
            'settings': {
                'analysis': {
                    'analyzer': {
                        "rebuilt_russian": {
                            "tokenizer": "standard",
                            "filter": [
                                "lowercase",
                                "russian_stop",
                                "russian_keywords",
                                "russian_stemmer"
                            ]
                        },
                    },
                },
            }
        },
    }
}

ELASTICSEARCH_INDICES = {
    'en-us': 'default',
    'ja-jp': 'japanese',
    'ru-ru': 'russian'
}

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

GS_BUCKET_NAME = os.getenv('GS_BUCKET_NAME')
GS_PROJECT_ID = os.getenv('GS_PROJECT_ID')
GS_DEFAULT_ACL = 'publicRead'
GS_AUTO_CREATE_BUCKET = False
STATIC_URL = 'https://storage.googleapis.com/' + GS_PROJECT_ID + '-static/'
MEDIA_URL = 'https://storage.googleapis.com/' + GS_PROJECT_ID + '-media/'
INSTALLED_APPS.append('storages')
DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
STATICFILES_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
    },
}
