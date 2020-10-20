from django.conf.global_settings import *
import sys
import logging


# Generic Django project settings

DEBUG = True
TEMPLATE_DEBUG = DEBUG

SECRET_KEY = 'Your Key Here'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'oauth2_provider',
    'corsheaders',
    'rest_framework',
    'service.apps.movie',
    'rest_framework_swagger'
)

# ============================================================================
# Calculation of directories relative to the project module location
# ============================================================================

import os
import service as project_module

PROJECT_DIR = os.path.dirname(os.path.realpath(project_module.__file__))

VAR_ROOT = os.path.join(PROJECT_DIR, 'settings', 'local')

if not os.path.exists(VAR_ROOT):
    os.mkdir(VAR_ROOT)

# ============================================================================
# Project URLS and media settings
# ============================================================================

ROOT_URLCONF = 'service.urls'

STATIC_URL = '/static/'
MEDIA_URL = '/uploads/'

STATIC_ROOT = os.path.join(VAR_ROOT, 'static')
MEDIA_ROOT = os.path.join(VAR_ROOT, 'uploads')

STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, 'static'),
)

# ============================================================================
# Templates
# ============================================================================
BASE_DIR = os.path.dirname(__file__)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_DIR, 'templates'),
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates'),
)

# ============================================================================
# Middleware
# ============================================================================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'oauth2_provider.middleware.OAuth2TokenMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

# ============================================================================
# Auth / security
# ============================================================================

ALLOWED_HOSTS = ['127.0.0.1', ]


AUTHENTICATION_BACKENDS = (
    'oauth2_provider.backends.OAuth2Backend',
)

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.SHA1PasswordHasher',
    'django.contrib.auth.hashers.MD5PasswordHasher',
    'django.contrib.auth.hashers.CryptPasswordHasher',

]

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# ============================================================================
# Miscellaneous project settings
# ============================================================================


CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = [
    'http://127.0.0.1',
    'http://localhost',
]
CORS_ALLOW_CREDENTIALS = True

# ============================================================================
# Third party app settings
# ============================================================================

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    'UNICODE_JSON': False,
    'PAGINATE_BY': None,
    'PAGINATE_BY_PARAM': 'page_size',
    'MAX_PAGINATE_BY': 100,
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
    ],
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
    )
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'basic': {
            'format': '{"level":"%(levelname)s","time":"%(asctime)s", "logger.thread_name" : "%(process)d %(thread)d", "module_info": "%(name)-20s %(module)s:%(lineno)s:%(funcName)s","dd.trace_id" : "%(dd.trace_id)s", "dd.span_id" : "%(dd.span_id)s", "message": "%(message)s"}',
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'basic',
            'filename': os.path.join(VAR_ROOT, 'service.log'),
            'maxBytes': 10 * 1024 * 1024,  # 10 MB
            'backupCount': 10,
        },
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'service': {
            'handlers': ['file', 'mail_admins'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}


OAUTH2_PROVIDER = {
    '_SCOPES': ['read', 'write', 'vendor'],
    '_DEFAULT_SCOPES': ['read', 'write'],
    'SCOPES': {
        'read': 'Read scope',
        'write': 'Write scope',
        'vendor': 'Token for Trusted Application'
    },
    'DEFAULT_SCOPES': ['read', 'write'],
    'ACCESS_TOKEN_EXPIRE_SECONDS': 1296000,
}

SWAGGER_SETTINGS = {
    'USE_SESSION_AUTH': False,
    'SECURITY_DEFINITIONS': {
        'api_key': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization'
        }
    },
    'DOC_EXPANSION': 'list',
    'APIS_SORTER': None,
    'OPERATIONS_SORTER': None,
    'JSON_EDITOR': False,
    'SHOW_REQUEST_HEADERS': False,
    'SUPPORTED_SUBMIT_METHODS': [
        'get',
        'post',
        'put',
        'delete',
        'patch'
    ],
    'VALIDATOR_URL': None,
}