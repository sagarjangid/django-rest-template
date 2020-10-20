from service.settings import *
import logging

DEBUG = True
TEMPLATE_DEBUG = DEBUG


logging.basicConfig(
    level = logging.INFO,
    format = " %(levelname)s %(name)s: %(message)s",
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase',
    }
}

ALLOWED_HOSTS += ['127.0.0.1', ]


ADMINS = (
    ('You', 'your@email'),
)
MANAGERS = ADMINS

ROOT_URLCONF = 'service.settings.local.urls'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

PROTOCOL = 'http'
HOST_NAME = 'localhost'
