"""
Django settings for pythonfi project.

Generated by 'django-admin startproject' using Django 1.11.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from decouple import config
from dj_database_url import parse as dburl
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = ['pythonfi.herokuapp.com', 'localhost',]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'pythonfi_web.admin_fi.apps.AdminFiConfig',
    'pythonfi_web.website.apps.WebsiteConfig',
    'social_django',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'pythonfi.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'pythonfi_web/templates').replace('\\','/')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],

            'libraries': {
                'tags': 'pythonfi_web.website.templatestags.tags',
            }

        },
    },
]


WSGI_APPLICATION = 'pythonfi.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'fidb',
        'USER': 'pythonpg',
        'PASSWORD': 'pythonpg',
        'HOST': '127.0.0.11',
        'PORT': '5432',
        'TEST': {
            'NAME': 'test_fidb',
        },
    }
}


AUTHENTICATION_BACKENDS = (
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',

    'django.contrib.auth.backends.ModelBackend',

)

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'home'


SOCIAL_AUTH_GITHUB_KEY = 'e9a05a588ae1ae28a1e4'
SOCIAL_AUTH_GITHUB_SECRET = '3a2fecba786817ffb14d7c01e959eb4f15eab6e3'

SOCIAL_AUTH_TWITTER_KEY = 'NOZfkj9cFNvvhi2LbdKo2WkHI'
SOCIAL_AUTH_TWITTER_SECRET = 'nmSWTuXHujBDcDgccRmrUGQwEUapU2RuMAS6zynF6hOh7rahVF'

SOCIAL_AUTH_FACEBOOK_KEY = '179211132813131'
SOCIAL_AUTH_FACEBOOK_SECRET = 'c4555b8aeecccb9babf968130665d00a'

SOCIAL_AUTH_LOGIN_ERROR_URL = '/settings/'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/settings/'
SOCIAL_AUTH_RAISE_EXCEPTIONS = False

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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


REST_FRAMEWORK = {
    'PAGE_SIZE': 10
}


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#AUTH_USER_MODEL = 'admin_fi.User'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
STATICFILES_DIRS = [
    str( os.path.join(BASE_DIR, 'pythonfi_web/static') )
]



STATIC_URL = '/static/'

MEDIA_ROOT = str( os.path.join(BASE_DIR, 'pythonfi_web/media') )
MEDIA_URL = '/media/'


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')