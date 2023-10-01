from .settings import *

import logging

log = logging.getLogger(__name__)

DEBUG = False

# fix ssl mixed content issues
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# Django security checklist settings.
# More details here: https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

USE_HTTPS_IN_ABSOLUTE_URLS = True

RENDER_DOMAIN = env("RENDER_DOMAIN", default="")
ALLOWED_HOSTS = [
    RENDER_DOMAIN,
]
log.info(f"ALLOWED_HOSTS: {ALLOWED_HOSTS}, RENDER_DOMAIN: {RENDER_DOMAIN}")

# Adjust logging config for production
# File handler instead of StreamHandler etc.
# Add additional loggers for specific parts of the codebase, as needed
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "formatter": {
            "format": "{asctime} {levelname} {module} {name} {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "formatter",
        },
        "file_overall": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": "debug_overall.log",
            "formatter": "formatter",
        },
        "file_specific": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": "debug_specific.log",
            "formatter": "formatter",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["file_overall", "console"],
            "level": "INFO",
            "propagate": True,
        },
        "apps": {
            "handlers": ["file_overall", "console"],
            "level": "INFO",
            "propagate": True,
        },
    },
}
