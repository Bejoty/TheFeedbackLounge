from zach.settings.base import *
from zach.secret import SECRET_KEY, DB_PASS

DEBUG = False

ALLOWED_HOSTS = [
    'mic.bejoty.com',
]

ADMINS = (
    ('Bejoty', 'bejotygames@gmail.com'),
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mic_db',
        'USER': 'db_admin',
        'PASSWORD': DB_PASS,
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = '/home/bejoty/webapps/mic_static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = '/home/bejoty/webapps/mic_media/'
