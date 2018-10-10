# -*- coding: utf-8 -*-
# Django settings for turkle project.

import os

DEBUG = False
ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

if 'TURKLE_DB_ENGINE' in os.environ and os.environ['TURKLE_DB_ENGINE'].lower() == 'mysql':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ['TURKLE_DB_NAME'],
            'USER': os.environ['TURKLE_DB_USER'],
            'PASSWORD': os.environ['TURKLE_DB_PASSWORD'],
            'HOST': os.environ['TURKLE_DB_HOST'],
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'db.sqlite3',
        }
    }

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'imdcm3*5i8lov-m=0qu9-yxjuk!_qk$ykgde&amp;cxq(8n(l_a63*'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

MIDDLEWARE = (
    # Uncomment to use whitenoise to serve static files
    # 'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'turkle.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'turkle.wsgi.application'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Our app comes before django.contrib.admin so that Django uses
    # our password change/reset templates instead of the templates
    # from django.contrib.admin
    'hits',
    'django.contrib.admin',

    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'django_nose',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Set max size for file uploads and POST requests to 100MB
DATA_UPLOAD_MAX_MEMORY_SIZE = 104857600
FILE_UPLOAD_MAX_MEMORY_SIZE = 104857600

LOGIN_REDIRECT_URL = '/'

# If True, the "Password Reset" link will be added to the login form
TURKLE_EMAIL_ENABLED = False
