from bakerydemo.settings.dev import *   # noqa

# Override settings here
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': '127.0.0.1',
        'NAME': 'wagtail',
        'USER': 'root',
        'PASSWORD': 'abcd1234',
        'PORT': '5432',
    }
}

WAGTAILSEARCH_BACKENDS = {
    'default': {
        'BACKEND': 'wagtail.search.backends.elasticsearch6',
        'URLS': ['http://34.71.200.181:9200'],
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
        'URLS': ['http://34.71.200.181:9200'],
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
                    "filter": {
                        "russian_stop": {
                            "type": "stop",
                            "stopwords": "_russian_"
                        },
                        "russian_keywords": {
                            "type": "keyword_marker",
                            "keywords": ["пример"]
                        },
                        "russian_stemmer": {
                            "type": "stemmer",
                            "language": "russian"
                        }
                    },
                },
            },
        },
    }
}

# from elasticsearch import RequestsHttpConnection
# WAGTAILSEARCH_BACKENDS = {
#     'default': {
#         'BACKEND': 'wagtail.search.backends.elasticsearch6',
#         'HOSTS': [{
#             'host': '34.71.200.181',
#             'port': 9200,
#             'use_ssl': False,
#             'verify_certs': False,
#         }],
#         'OPTIONS': {
#             'connection_class': RequestsHttpConnection,
#         },
#     }
# }

GS_BUCKET_NAME = 'ornate-hangar-125622-static'
GS_PROJECT_ID = 'ornate-hangar-125622'
GS_DEFAULT_ACL = 'publicRead'
GS_AUTO_CREATE_BUCKET = True
STATIC_URL = 'https://storage.googleapis.com/' + GS_PROJECT_ID + '-static/'
MEDIA_URL = 'https://storage.googleapis.com/' + GS_PROJECT_ID + '-media/'
INSTALLED_APPS.append('storages')
DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
STATICFILES_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
SECRET_KEY = 'dilfubglsufdbgliugaurebgluarbg'