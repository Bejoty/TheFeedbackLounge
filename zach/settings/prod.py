from zach.settings.defaults import *
from zach.secret import SECRET_KEY, DB_PASS

DEBUG = FALSE

ALLOWED_HOSTS = ['sexymic.bejoty.com']

ADMINS = (
    ('Bejoty', 'bejotygames@gmail.com'),
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sexymic_db',
        'USER': 'db_admin',
        'PASSWORD': 'notthebestpassword',
    }

}

STATIC_URL = '/static/'
STATIC_ROOT = '/home/bejoty/webapps/sexymic_static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = '/home/bejoty/webapps/sexymic_media/'

