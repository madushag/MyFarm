"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 3.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
from pathlib import Path
from os import environ, path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'q_4yzrc-(no7po&tap8o^6a)7u8r3^s@k6$8&z30y!qkgs3rky'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'homepage',
    'authenticate',
    'storages',
    'farm.apps.FarmConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
        "NAME": environ.get("SQL_DATABASE", path.join(BASE_DIR, "db.sqlite3")),
        "USER": environ.get("SQL_USER", "user"),
        "PASSWORD": environ.get("SQL_PASSWORD", "password"),
        "HOST": environ.get("SQL_HOST", "localhost"),
        "PORT": environ.get("SQL_PORT", "5432"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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

# Redirect LoginView on successful login
LOGIN_REDIRECT_URL = '/'

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

USE_S3 = os.getenv('USE_S3') == 'TRUE'

if USE_S3:
  # AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
  # AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
  AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
  AWS_DEFAULT_ACL = 'public-read'
  AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
  AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
  # s3 static settings
  AWS_LOCATION = 'static'
  PUBLIC_MEDIA_LOCATION = 'media' 
  DEFAULT_FILE_STORAGE = 'app.storage_backends.PublicMediaStorage'
  MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/'
  STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/'
  STATICFILES_STORAGE = 'app.storage_backends.StaticStorage'
  COMPRESS_URL = STATIC_URL
  COMPRESS_ROOT = os.path.join(BASE_DIR, 'static')
else:
  STATIC_ROOT = path.join(BASE_DIR, 'static')
  STATIC_URL = environ.get("STATIC_URL", '/static/')
  MEDIA_ROOT = path.join(BASE_DIR, 'media')
  MEDIA_URL = '/media/'



LOGOUT_REDIRECT_URL = '/'

