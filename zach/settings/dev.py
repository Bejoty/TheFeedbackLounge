from zach.settings.base import *
from zach.secret import DB_PASS

DEBUG = True

TEMPLATE_DEBUG = True

SECRET_KEY = 'this is not a secret key'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'sexymic': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sexymic_db',
        'USER': 'db_admin',
        'PASSWORD': DB_PASS,
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = '/home/bejoty/tmp/django/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = '/home/bejoty/tmp/django/media/'
