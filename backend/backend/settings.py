"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 3.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+!hgi7mynxzcvaimm2%+g)6u8bi04ow!50zh%!*h3n_kq0c9z^'

OTP_VERIFY_SECRET = os.getenv("OTP_VERIFY_SECRET", "BRUH")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG_ENV = os.getenv("DJANGO_DEBUG", 'True')
DEBUG = DEBUG_ENV != 'False'


ALLOWED_HOSTS = ['127.0.0.1', 'faces21.herokuapp.com', os.getenv("PUBLIC_IP", "localhost")]

CSRF_COOKIE_HTTPONLY = False


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    # 'django_markdown',
    'martor',

    'users',
    'events',
    
]

AUTH_USER_MODEL = 'users.User'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
}

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv("DB_NAME"),
        'USER': os.getenv("DB_USERNAME"),
        'PASSWORD': os.getenv("DB_PASSWORD"),
        'HOST': 'localhost',
        'PORT': '',
    }
}


CORS_ALLOW_ALL_ORIGINS = True

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_URL = '/media/'

# Path where media is stored
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



# MATOR SETTINGS
# Choices are: "semantic", "bootstrap"
MARTOR_THEME = 'bootstrap'

# Global martor settings
# Input: string boolean, `true/false`
MARTOR_ENABLE_CONFIGS = {
    'emoji': 'true',        # to enable/disable emoji icons.
    'imgur': 'false',        # to enable/disable imgur/custom uploader.
    'mention': 'false',     # to enable/disable mention
    'jquery': 'true',       # to include/revoke jquery (require for admin default django)
    'living': 'false',      # to enable/disable live updates in preview
    'spellcheck': 'false',  # to enable/disable spellcheck in form textareas
    'hljs': 'true',         # to enable/disable hljs highlighting in preview
}

# To show the toolbar buttons
MARTOR_TOOLBAR_BUTTONS = [
    'bold', 'italic', 'horizontal', 'heading', 'pre-code',
    'blockquote', 'unordered-list', 'ordered-list',
    'link', 'image-link', 'image-upload', 'emoji',
    'direct-mention', 'toggle-maximize', 'help'
]

# To setup the martor editor with title label or not (default is False)
MARTOR_ENABLE_LABEL = False

# Imgur API Keys
MARTOR_IMGUR_CLIENT_ID = 'your-client-id'
MARTOR_IMGUR_API_KEY   = 'your-api-key'

# Markdownify
MARTOR_MARKDOWNIFY_FUNCTION = 'martor.utils.markdownify' # default
MARTOR_MARKDOWNIFY_URL = '/martor/markdownify/' # default

# Markdown extensions (default)
MARTOR_MARKDOWN_EXTENSIONS = [
    'markdown.extensions.extra',
    'markdown.extensions.nl2br',
    'markdown.extensions.smarty',
    'markdown.extensions.fenced_code',

    # Custom markdown extensions.
    'martor.extensions.urlize',
    'martor.extensions.del_ins',      # ~~strikethrough~~ and ++underscores++
    'martor.extensions.mention',      # to parse markdown mention
    'martor.extensions.emoji',        # to parse markdown emoji
    'martor.extensions.mdx_video',    # to parse embed/iframe video
    'martor.extensions.escape_html',  # to handle the XSS vulnerabilities
]

# Markdown Extensions Configs
MARTOR_MARKDOWN_EXTENSION_CONFIGS = {}

# Markdown urls
MARTOR_UPLOAD_URL = '/martor/uploader/' # default
MARTOR_SEARCH_USERS_URL = '/martor/search-user/' # default

MARTOR_MARKDOWN_BASE_MENTION_URL = 'http://127.0.0.1:8000/'                                      # please change this to your domain
