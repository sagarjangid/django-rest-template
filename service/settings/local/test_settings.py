"""
Local test settings
"""
from service.settings.test import *  # pylint: disable=W0614,W0401

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': 'localhost',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'

PROTOCOL = 'http'
HOST_NAME = 'localhost'

TEST_DATA_FILE_PATH = 'service/api/v1/tests/data/'
