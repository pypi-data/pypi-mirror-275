import os
from pathlib import Path

import boto3
from decouple import RepositoryEnv, Config
from storages.backends.s3boto3 import S3Boto3Storage

from core.enums import EnvironmentVariables
from core.logger import app_logger

config = Config(RepositoryEnv(".env"))

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', default='django-insecure-j$03nrrudq1a4m2#$$5w=gyj(n#l(y8ntti@#z^uzqg6nmjigq')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='*', cast=lambda v: [s.strip() for s in v.split(',')])

SHARED_APPS = (
    'django_tenants',
    'corsheaders',
    'drf_yasg',
    'django_filters',
    'rest_framework',
    'rest_framework_simplejwt',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core.apps.CoreConfig',
)

TENANT_APPS = (
    "tenant.apps.TenantConfig",
)

TENANT_MODEL = "core.Client"
TENANT_DOMAIN_MODEL = "core.Domain"

INSTALLED_APPS = list(SHARED_APPS) + [app for app in TENANT_APPS if app not in SHARED_APPS]

MIDDLEWARE = [
    'django_tenants.middleware.main.TenantMainMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'core.middlewares.RequestIDMiddleware',
]

ROOT_URLCONF = 'PyStarter.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'PyStarter.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django_tenants.postgresql_backend',
        'NAME': config(EnvironmentVariables.DB_NAME),
        'USER': config(EnvironmentVariables.DB_USER),
        'PASSWORD': config(EnvironmentVariables.DB_PASSWORD),
        'HOST': config(EnvironmentVariables.DB_HOST),
        'PORT': config(EnvironmentVariables.DB_PORT),
    }
}

DATABASE_ROUTERS = (
    'django_tenants.routers.TenantSyncRouter',
)

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DEFAULT_API_VERSION = '1'
ALLOWED_API_VERSIONS = ['1', '2']

REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'core.exceptions.custom_exception_handler',
    'DEFAULT_VERSIONING_CLASS': 'core.base.version.VersioningMixin',
    'DEFAULT_VERSION': DEFAULT_API_VERSION,
    'ALLOWED_VERSIONS': ALLOWED_API_VERSIONS,
    'VERSION_PARAM': 'v',
    'DEFAULT_PAGINATION_CLASS': 'core.base.pagination.StandardResultsSetPagination',
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'PAGE_SIZE': 10
}

AUTH_USER_MODEL = 'core.AppUser'

# Set AWS settings if using S3 storage
AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')

AWS_PUBLIC_STORAGE_BUCKET_NAME = config('AWS_PUBLIC_STORAGE_BUCKET_NAME')
AWS_PUBLIC_STORAGE_REGION = config('AWS_PUBLIC_STORAGE_REGION')
AWS_PUBLIC_STORAGE_ENDPOINT_URL = config('AWS_PUBLIC_STORAGE_ENDPOINT_URL')
AWS_PUBLIC_STORAGE_SERVE_URL = config('AWS_PUBLIC_STORAGE_SERVE_URL')

AWS_PRIVATE_STORAGE_REGION = config('AWS_PRIVATE_STORAGE_REGION')
AWS_PRIVATE_STORAGE_ENDPOINT_URL = config('AWS_PRIVATE_STORAGE_ENDPOINT_URL')
AWS_PRIVATE_STORAGE_BUCKET_NAME = config('AWS_PRIVATE_STORAGE_BUCKET_NAME')
AWS_QUERYSTRING_EXPIRE = config('AWS_PRIVATE_STORAGE_QUERYSTRING_EXPIRE', default=3600, cast=int)

STATIC_URL = f'/static/'
STATIC_ROOT = "staticfiles"
MEDIA_URL = f'/media/'

# STATICFILES_STORAGE = 'core.storages.s3.S3StaticStorage'
DEFAULT_FILE_STORAGE = 'core.storages.s3.PrivateS3Storage'

LOGGING_CONFIG = None
