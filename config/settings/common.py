import os
from os.path import join
from configurations import Configuration
import environ

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
env = environ.Env()
env.read_env(os.path.join(BASE_DIR, ".env"))


class Common(Configuration):
    INSTALLED_APPS = [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        # Third party apps
        "rest_framework",  # utilities for rest apis
        "rest_framework.authtoken",  # token authentication
        "django_filters",  # for filtering rest endpoints
        "drf_spectacular",
        "django_extensions",
        "rest_framework_simplejwt",
        # Your apps
        "user",
        "post",
    ]

    # https://docs.djangoproject.com/en/2.0/topics/http/middleware/
    MIDDLEWARE = [
        "django.middleware.security.SecurityMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
    ]

    ALLOWED_HOSTS = ["*"]
    ROOT_URLCONF = "config.urls"
    SECRET_KEY = env("DJANGO_SECRET_KEY")
    WSGI_APPLICATION = "config.wsgi.application"

    # Email
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

    ADMINS = (("Author", "a4rcvv@gmail.com"),)

    # Postgres
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": env("POSTGRES_DB"),
            "USER": env("POSTGRES_USER"),
            "PASSWORD": env("POSTGRES_PASSWORD"),
            "HOST": env("POSTGRES_HOST"),
            "PORT": env("POSTGRES_PORT"),
        }
    }

    # General
    APPEND_SLASH = False
    TIME_ZONE = "Asia/Tokyo"
    LANGUAGE_CODE = "ja"
    # If you set this to False, Django will make some optimizations so as not
    # to load the internationalization machinery.
    USE_I18N = False
    USE_L10N = True
    USE_TZ = True
    LOGIN_REDIRECT_URL = "/"

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/2.0/howto/static-files/
    STATIC_ROOT = "/static/"
    STATICFILES_DIRS = []
    STATIC_URL = "/static/"
    STATICFILES_FINDERS = (
        "django.contrib.staticfiles.finders.FileSystemFinder",
        "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    )

    # Media files
    MEDIA_ROOT = join(os.path.dirname(BASE_DIR), "media")
    MEDIA_URL = "/media/"

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
    DEBUG = False

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
    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "django.server": {
                "()": "django.utils.log.ServerFormatter",
                "format": "[%(server_time)s] %(message)s",
            },
            "verbose": {
                "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s"
            },
            "simple": {"format": "%(levelname)s %(message)s"},
        },
        "filters": {
            "require_debug_true": {
                "()": "django.utils.log.RequireDebugTrue",
            },
        },
        "handlers": {
            "django.server": {
                "level": "INFO",
                "class": "logging.StreamHandler",
                "formatter": "django.server",
            },
            "console": {
                "level": "DEBUG",
                "class": "logging.StreamHandler",
                "formatter": "simple",
            },
            "mail_admins": {
                "level": "ERROR",
                "class": "django.utils.log.AdminEmailHandler",
            },
        },
        "loggers": {
            "django": {
                "handlers": ["console"],
                "propagate": True,
            },
            "django.server": {
                "handlers": ["django.server"],
                "level": "INFO",
                "propagate": False,
            },
            "django.request": {
                "handlers": ["mail_admins", "console"],
                "level": "ERROR",
                "propagate": False,
            },
            "django.db.backends": {"handlers": ["console"], "level": "INFO"},
        },
    }

    # Custom user app
    AUTH_USER_MODEL = "user.User"

    # Django Rest Framework
    REST_FRAMEWORK = {
        "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
        "PAGE_SIZE": env("DJANGO_PAGINATION_LIMIT", default=10),
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
            "rest_framework_simplejwt.authentication.JWTAuthentication",
        ),
        "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
        "DEFAULT_FILTER_BACKENDS": ("django_filters.rest_framework.DjangoFilterBackend",)
    }

    # drf-spectacular
    SPECTACULAR_SETTINGS = {
        "TITLE": "Example API",
        "DESCRIPTION": "Example API",
        "VERSION": "0.1.0",
        "SERVE_INCLUDE_SCHEMA": False,
        # OTHER SETTINGS
    }

    # jwt
    SIMPLE_JWT = {"ROTATE_REFRESH_TOKENS": True}
