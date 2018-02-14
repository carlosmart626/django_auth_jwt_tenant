import sys
import os

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

SECRET_KEY = '1'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'django_test.sqlite',
    }
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
    },
]

ROOT_URLCONF = 'django_auth_jwt_tenant.tests.urls'