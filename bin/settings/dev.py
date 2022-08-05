from .base import *  # noqa F403

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-ky!=^@#wkm-*p44(t^q9&5ta&f933&c^^5m%hjv%%n9b_x@lkx"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

WAGTAIL_QR_CODE_BASE_URL = "http://localhost:8000"

try:
    from .local import *  # noqa F403 F401
except ImportError:
    pass
