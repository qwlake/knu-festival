
from .base import *
import os

ROOT_URLCONF = 'festival.urls'

SECRET_KEY = '+zj4-xdycu$d7sxxn8%v@su&n89m$tre!2e6j7t^$tg!q%z2hp'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'festival', 'static'),
    os.path.join(BASE_DIR, 'static'),
]

STATIC_ROOT = os.path.join(BASE_DIR, '.static_root')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
