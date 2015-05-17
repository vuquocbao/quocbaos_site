# Local Setting Python File

# Imports
import os
import os.path

# Site Root
_SITE_ROOT = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    '..', '..', '..')

# SECRET KEY (Keep Secret Key used in production secert)
SECRET_KEY = '0ljox8yo5@!-*1z1u#9+=gi(8m(si14vz3jqaemv-#=by94#3o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = ['*']


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'quocbaos_site',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '8889'

    }
}

# Static files (CSS, JavaScript, Images)
STATIC_ROOT = os.path.join(_SITE_ROOT, 'static')

# Media files (Uploaded Files)
MEDIA_ROOT = os.path.join(_SITE_ROOT, 'media')