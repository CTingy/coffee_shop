import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$t2)vx=tq33#k@@st%686s0n0ur@f&xj*a&z0@*l#!g2xkd@!p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
if 'DYNO' in os.environ:    # Running on Heroku
    DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'board',
    'account',
    'main',
    'product',
    'cart',
    'contact'
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

ROOT_URLCONF = 'coffee_shop.urls'

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

WSGI_APPLICATION = 'coffee_shop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

if DEBUG:  # Running on the development environment
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'coffeedb1',
            'USER': 'coffee',
            'PASSWORD': 'coffee',
            'HOST': 'localhost',
            'PORT': '',
        }
    }
else:   # Running on Heroku
    # Parse database configuration from $DATABASE_URL
    import dj_database_url
    DATABASES = {'default': dj_database_url.config()}
    # Honor the 'X-Forwarded-Proto' header for request.is_secure()
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'zh-hant'

TIME_ZONE = 'Asia/Taipei'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

# For Heroku deployment
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static_cdn', 'static_root')
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static_cdn', 'media_root')

AUTH_USER_MODEL = 'account.User'

LOGIN_URL = '/account/login/'
