"""Settings for Ghadah Alabbadi's portfolio.

Local development works with Django alone. On Render, set the environment
variables listed in README.md; WhiteNoise then serves the static files.
"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get("SECRET_KEY", "dev-only-key-change-me-in-production")
DEBUG = os.environ.get("DEBUG", "True").lower() == "true"

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
ALLOWED_HOSTS += [h.strip() for h in os.environ.get("ALLOWED_HOSTS", "").split(",") if h.strip()]
RENDER_EXTERNAL_HOSTNAME = os.environ.get("RENDER_EXTERNAL_HOSTNAME")
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

INSTALLED_APPS = [
    "django.contrib.staticfiles",
    "pages",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

try:
    import whitenoise  # noqa: F401

    MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")
    HAS_WHITENOISE = True
except ImportError:
    HAS_WHITENOISE = False

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {"context_processors": ["django.template.context_processors.request"]},
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# The site has no database: all content lives in pages/content.py.
DATABASES = {}

LANGUAGE_CODE = "en"
TIME_ZONE = "Asia/Riyadh"
USE_I18N = False
USE_TZ = True

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

if HAS_WHITENOISE and not DEBUG:
    STORAGES = {
        "default": {"BACKEND": "django.core.files.storage.FileSystemStorage"},
        "staticfiles": {"BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage"},
    }

if not DEBUG:
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SECURE_SSL_REDIRECT = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_REFERRER_POLICY = "strict-origin-when-cross-origin"
