"""
Django settings for inventory project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

# BASE_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$xb5siy!nm^#hq%iz84k+3*5=w0-r7m(!0i5a15ip@8x*t_2@4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'kucun.apps.KucunConfig',
    'weixin.apps.WeixinConfig',
    'meizu.apps.MeizuConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'inventory.urls'

WSGI_APPLICATION = 'inventory.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# if 'SERVER_SOFTWARE' in os.environ:
#     from sae.const import (
#         MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASS, MYSQL_DB
#         )
# else:
#     MYSQL_HOST = 'localhost'
#     MYSQL_PORT = '3306'
#     MYSQL_USER = 'root'
#     MYSQL_PASS = 'root'
#     MYSQL_DB = 'xlhw'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': MYSQL_DB,
#         'USER': MYSQL_USER,
#         'PASSWORD': MYSQL_PASS,
#         'HOST': MYSQL_HOST,
#         'PORT': MYSQL_PORT,
#     }

# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
# TEMPLATE_LOADERS = (
#     # 'django.template.loaders.filesystem.Loader',
#     'django.template.loaders.app_directories.Loader',
#         # 'django.template.loaders.eggs.Loader',
# )
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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
STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
# TEMPLATE_DIRS = (
#     # os.path.join(os.path.dirname(__file__), '..', 'templates').replace('\\', '/'),
# )


SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_AGE = 60*60*12
