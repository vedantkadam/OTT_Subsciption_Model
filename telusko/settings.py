"""
Django settings for telusko project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path
# import django_heroku
import dj_database_url
# from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY ='django-insecure-cly%(5-34f8d1pc_fi*l_p@m3^x%#a$!iq(yu=s&&ez%-_pk$3'
WE_CHAT_USR = os.environ.get("WE_CHAT_USR") or ""
WE_CHAT_PASS = os.environ.get("WE_CHAT_PASS") or ""
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*','ott-subscription-model.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'travello.apps.TravelloConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_email_verification', 
    'payment',
    ]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'telusko.urls'

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

WSGI_APPLICATION = 'telusko.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "djongo",
        "CLIENT": {
            'name': 'ott_plat',
            'host': 'mongodb+srv://'+WE_CHAT_USR+':'+WE_CHAT_PASS+'@cluster0.1yefb.mongodb.net/myFirstDatabase?retryWrites=true&w=majority',
            #'host': 'mongodb+srv://'+WE_CHAT_USR+':'+WE_CHAT_PASS+'@cluster0.1yefb.mongodb.net/myFirstDatabase?retryWrites=true&w=majority',
            'username': WE_CHAT_USR,
            'password': WE_CHAT_PASS,
            "authMechanism": "SCRAM-SHA-1",
        },
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


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static')
]
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')
# STATICFILES_STORAGE = 'whitenoise.storage.CompressManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
#
#
#
# def verified_callback(user):
#     user.is_active = True
#
#
#
#
#
# EMAIL_ACTIVE_FIELD = 'is_active'
# EMAIL_SERVER = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_ADDRESS = 'hitanshuparekh72@student.sfit.ac.in'
# EMAIL_PASSWORD = 'hitanshu72'
# EMAIL_FROM_ADDRESS = 'Tripology@gmail.com'
# EMAIL_MAIL_SUBJECT = 'Confirm your email'
# EMAIL_MAIL_HTML = 'mail_body.html'
# EMAIL_MAIL_PLAIN = 'mail_body.txt'
# EMAIL_TOKEN_LIFE = 60 * 60
# EMAIL_PAGE_TEMPLATE = 'confirm_template.html'
# EMAIL_PAGE_DOMAIN = 'http://mydomain.com/'
#





# EMAIL_VERIFIED_CALLBACK = verified_callback
# EMAIL_FROM_ADDRESS = 'Tripology@gmail.com'
# EMAIL_MAIL_SUBJECT = 'Confirm your email'
# EMAIL_MAIL_HTML = 'mail_body.html'
# EMAIL_MAIL_PLAIN = 'mail_body.txt'
# EMAIL_TOKEN_LIFE = 60 * 60
# EMAIL_PAGE_TEMPLATE = 'confirm_template.html'
# EMAIL_PAGE_DOMAIN = 'http://mydomain.com/'


#SMTP Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'vedantkadam@student.sfit.ac.in'
EMAIL_HOST_PASSWORD = 'albsbwcscidvgyqp'
# EMAIL_ACTIVE_FIELD = 'is_active'

# django_heroku.settings(locals())

RAZOR_KEY_ID ='rzp_test_Q8AZkEbm7RUitk'
RAZOR_KEY_SECRET ='Esu9mt6ZyXxjrEgnqKKJTjLn'