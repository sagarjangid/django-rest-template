from service.settings import *   # pylint: disable=W0614,W0401
import logging

DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'service',
        'USER': 'service',
        'PASSWORD': 'service',
        'HOST': '',
    }
}

INSTALLED_APPS += (
    'django_nose',
)


NOSE_ARGS = ['--logging-filter=-django.request',
             '--with-coverage',
             '--exe'
            ]
NOSE_PLUGINS = ['service.core.nose_plugins.SilenceMigrations']
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'


PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]

REST_FRAMEWORK['DATETIME_FORMAT'] = 'iso-8601'
DEFAULT_USER_EMAIL = 'manish.2184@gmail.com'
NOSE_INCLUDE_EXE=1


class DisableMigrations(object):

    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return None

MIGRATION_MODULES = DisableMigrations()
OAUTH2_PROVIDER_ACCESS_TOKEN_MODEL = 'oauth2_provider.AccessToken'
OAUTH2_PROVIDER_APPLICATION_MODEL = 'oauth2_provider.Application'
OAUTH2_PROVIDER_REFRESH_TOKEN_MODEL = 'oauth2_provider.RefreshToken'

#removed unneeded middleware
MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

logging.disable(logging.CRITICAL)