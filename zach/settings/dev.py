from zach.settings.base import *

DEBUG = True

TEMPLATE_DEBUG = True

SECRET_KEY = 'this is not a secret key'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = '/home/bejoty/tmp/django/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = '/home/bejoty/tmp/django/media/'
