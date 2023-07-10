import os
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
try:
    SECRET_KEY = os.environ["SECRET_KEY"]
except KeyError as e:
    raise RuntimeError("Could not find a SECRET_KEY in environment") from e


# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = [".itsbillw.xyz", "*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .local import *
except ImportError:
    pass
