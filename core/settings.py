import os
from pathlib import Path
from decouple import config
from django.contrib.messages import constants as messages

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = config('DEBUG', default=False, cast=bool)
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Custom Apps
    'accounts',
    'pages',
    'testimonials',
    'blogs',
    'gallery',
    'events',
    'services',
    'reports',
    # 3rd Party Apps
    'ckeditor',
    'ckeditor_uploader',
    'embed_video',
    # Sitemap
    'django.contrib.sitemaps',
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

ROOT_URLCONF = 'core.urls'

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
                'django.template.context_processors.request',
                'pages.context_processors.Blogs', # Page Context Processors
                'pages.context_processors.adBlockGen', # Page Sidebar Ad-block Context Processors
                'pages.context_processors.adBlocksHome', # Page Home Ad-block Context Processors
                'pages.context_processors.contactPageUniversal', # Page ContactPage Context Processors
                'pages.context_processors.copyrightUniversal', # Page Copyright Context Processors
                'pages.context_processors.webSettingsUnivarsal', # Page Web Settings Context Processors
                'pages.context_processors.termPageUniversal', # Page TermPage Context Processors
                'pages.context_processors.pageCategoryUniversal', # Page Category About Page Context Processors
                'pages.context_processors.bannerHome', # Page Banner Context Processors
                'services.context_processors.serviceCategory' # Service Context Processors
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'
AUTH_USER_MODEL = 'accounts.Account'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': config('DB_ENGINE'),
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT'),
    }
}

# Database Cache Settings
CACHES = {
    'default':{
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'webCache',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = os.path.join(BASE_DIR, '/static/')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'core/static'),
]

# Media settings

MEDIA_URL = os.path.join(BASE_DIR, '/media/')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

#CK Editor Upload Path

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'n1theme',
        'width': '100%',
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_YourCustomToolbarConfig': [
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', '-']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-']},
            {'name': 'links', 'items': ['Link', 'Unlink']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'insert','items': ['Image', 'Smiley', 'Iframe']},
            {'name': 'document', 'items': ['Source']},
        ],
        'toolbar': 'YourCustomToolbarConfig',  # put selected toolbar config here
        'tabSpaces': 4,
    }
}

# Messages Feature
MESSAGE_TAGS = {
    messages.DEBUG: 'secondary',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger',
}

# SMTP Details
DEFAULT_FROM_EMAIL = config('SMTP_FROM_EMAIl')
EMAIL_HOST = config('SMTP_EMAIL_HOST', default='localhost')
EMAIL_PORT = config('SMTP_EMAIL_PORT', default=25, cast=int)
EMAIL_HOST_USER = config('SMTP_EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD = config('SMTP_EMAIL_HOST_PASSWORD', default='')
EMAIL_USE_TLS = config('SMTP_EMAIL_USE_TLS', default=False, cast=bool)
EMAIL_USE_SSL = config('SMTP_EMAIL_USE_SSL', default=False, cast=bool)

# Google Recaptcha Key
RECAPTCHA_PUBLIC_KEY = config('GOOGLE_RECAPTCHA_PUBLIC_KEY')
RECAPTCHA_PRIVATE_KEY = config('GOOGLE_RECAPTCHA_PRIVATE_KEY')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'