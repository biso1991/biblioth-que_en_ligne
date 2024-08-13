import os
from os.path import join
from distutils.util import strtobool
# import dj_database_url
from configurations import Configuration
import logging.config
from django.utils.log import DEFAULT_LOGGING

# BASE_DIR = Path(__file__).resolve().parent.parent

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)

class Common(Configuration):
    DEBUG=True
    SECRET_KEY = "django-insecure-allh*#e0kt0k!506olz1h8@7u&qowi7$bfvotufg)37yo@)%vj"

    INSTALLED_APPS = (
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        # "channels",  # Enabeling channels for real time communication
        # Third party apps
        "rest_framework",  # utilities for rest apis
        "django_rest_passwordreset",  # RESET PASSWORD USING EMAIL
        "rest_framework.authtoken",  # token authentication
        "django_filters",  # for filtering rest endpoints
        "corsheaders",  # ENABLING CORS IN REST API
        # "django_celery_beat",
        "django_celery_results",
        # Your apps
        "api.users",
    )

    # CHANNEL_LAYERS = {
    #     "default": {
    #         "BACKEND": "channels_redis.core.RedisChannelLayer",
    #         "CONFIG": {
    #             "hosts": [("redis", 6379)],
    #         },
    #     },
    # }
    ALLOWED_HOSTS = ["*"]
    # https://docs.djangoproject.com/en/2.0/topics/http/middleware/
    MIDDLEWARE = (
        "django.middleware.security.SecurityMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
        "corsheaders.middleware.CorsMiddleware",
        "django.middleware.common.CommonMiddleware",
    )

    CORS_ALLOWED_ORIGINS = []
    ALLOWED_HOSTS = ["localhost", "127.0.0.1","0.0.0.0", "[::1]"]
    ROOT_URLCONF = "api.urls"
    SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")
    WSGI_APPLICATION = "api.wsgi.application"
    # ASGI_APPLICATION = "api.asgi.application_Asgi"


    # TOKEN VALIDITY DURATION
    # TOKEN_EXPIRED_AFTER_SECONDS = timedelta(minutes=1)

    # Email
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_HOST = "mailhog"
    EMAIL_PORT = 1025
    EMAIL_HOST_USER = ""
    EMAIL_HOST_PASSWORD = ""
    EMAIL_USE_TLS = False
    # My Supervisor 
    ADMINS = (("Author", "bilelnasrinasri91@gmail.com"),)

    DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }

    # # Postgres
    # DATABASES = {
    #     "default": dj_database_url.config(
    #         default="postgres://dbuser:dbpassword@postgres:5432/qadb",
    #         conn_max_age=int(os.getenv("POSTGRES_CONN_MAX_AGE", 600)),
    #     )
    # }

    # General
    APPEND_SLASH = False
    TIME_ZONE = "UTC"
    LANGUAGE_CODE = "en-us"
    # If you set this to False, Django will make some optimizations so as not
    # to load the internationalization machinery.
    USE_I18N = False
    USE_L10N = True
    USE_TZ = True
    LOGIN_REDIRECT_URL = "/"

    # REDIS_HOST = "redis://redis"
    # REDIS_PORT = 6379
    # # Celery Configuration Options
    # CELERY_BROKER_URL = REDIS_HOST + ":" + str(REDIS_PORT)
    # DEBUG = True
    # CELERY_TIMEZONE = "Tunisia/Tunis"
    # CELERY_TASK_TRACK_STARTED = True
    # CELERY_TASK_TIME_LIMIT = 30 * 60
    # CELERY_RESULT_BACKEND = "django-db"
    # CELERY_CACHE_BACKEND = "django-cache"
    # CELERY_WORKER_CONCURRENCY = os.getenv("CELERY_WORKER_CONCURRENCY", "4")
    # CELERY_ACKS_LATE = True

    # Redis settings for Django Cache
    # CACHES = {
    #     "default": {
    #         "BACKEND": "django.core.cache.backends.redis.RedisCache",
    #         "LOCATION": CELERY_BROKER_URL + "/1",
    #     }
    # }
    # CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers.DatabaseScheduler'


    ROOT_URL = "http://localhost:8000"
    
    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/2.0/howto/static-files/
    STATIC_ROOT = os.path.normpath(join(os.path.dirname(BASE_DIR), "static"))
    STATICFILES_DIRS = []
    STATIC_URL = "static/"
    STATICFILES_FINDERS = (
        "django.contrib.staticfiles.finders.FileSystemFinder",
        "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    )

    # Media files
    MEDIA_ROOT = join(os.path.dirname(BASE_DIR), "media")
    MEDIA_URL = "media/"




    TEMPLATES = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": STATICFILES_DIRS,
            "APP_DIRS": True,
            "OPTIONS": {
                "context_processors": [
                    "django.template.context_processors.debug",
                    "django.template.context_processors.request",
                    "django.contrib.auth.context_processors.auth",
                    "django.contrib.messages.context_processors.messages",
                ],
            },
        },
    ]

    # Set DEBUG to False as a default for safety
    # https://docs.djangoproject.com/en/dev/ref/settings/#debug
    DEBUG = strtobool(os.getenv("DJANGO_DEBUG", "yes"))

    # Password Validation
    # https://docs.djangoproject.com/en/2.0/topics/auth/passwords/#module-django.contrib.auth.password_validation
    AUTH_PASSWORD_VALIDATORS = [
        {
            "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
        },
    ]

    # Logging
    # Disable Django's logging setup
    LOGGING_CONFIG = None

    LOGLEVEL = os.environ.get('LOGLEVEL', 'info').upper()

    logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            # exact format is not important, this is the minimum information
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
        },
        'django.server': DEFAULT_LOGGING['formatters']['django.server'],
    },
    'handlers': {
        # console logs to stderr
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
        'django.server': DEFAULT_LOGGING['handlers']['django.server'],
    },
    'loggers': {
        # default for all undefined Python modules
        '': {
            'level': 'WARNING',
            'handlers': ['console'],
        },
        # Our application code
        'users': {
            'level': LOGLEVEL,
            'handlers': ['console'],
            # Avoid double logging because of root logger
            'propagate': False,
        },
        # Default runserver request logging
        'django.server': DEFAULT_LOGGING['loggers']['django.server'],
    },
    
    })

    # Custom user app
    AUTH_USER_MODEL = "users.User"

    # Django Rest Framework
    REST_FRAMEWORK = {
        "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
        "PAGE_SIZE": int(os.getenv("DJANGO_PAGINATION_LIMIT", 100)),
        "DATETIME_FORMAT": "%Y-%m-%dT%H:%M:%S%z",
        "DEFAULT_RENDERER_CLASSES": (
            "rest_framework.renderers.JSONRenderer",
            "rest_framework.renderers.BrowsableAPIRenderer",
        ),
        "DEFAULT_PERMISSION_CLASSES": [
            "rest_framework.permissions.IsAuthenticated",
        ],
        "DEFAULT_AUTHENTICATION_CLASSES": (
            "rest_framework.authentication.SessionAuthentication",
            "rest_framework.authentication.TokenAuthentication",
        ),
        "DEFAULT_FILTER_BACKENDS": [
            "django_filters.rest_framework.DjangoFilterBackend"
        ],
        }