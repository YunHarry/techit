from .base import *

def read_secret(secret_name):
    file = open('/run/secrets/' + secret_name)
    secret = file.read()
    secret = secret.lstrip().rstrip()
    file.close()
    return secret


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-b_nh5b666g01hxp9*rd1ulj8$w6ac(2s%fw^w)=39u#&ax7gbn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    '*'
]

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": read_secret("MARIADB_DATABASE)"),
        "USER": read_secret("MARIADB_USER"),
        "PASSWORD": read_secret("MARIADB_PASSWORD"),
        "HOST": "mariadb",
        "PORT": "3306",
    }
}