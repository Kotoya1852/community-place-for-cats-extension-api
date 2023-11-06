"""
WSGI config for community-place-for-cats-extension-api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import logging
import os

from django.core.wsgi import get_wsgi_application

_build_arg = os.getenv("BUILD_ARG", None)

logger = logging.getLogger("djnago.server")

logger.info(_build_arg)
if _build_arg == "dev":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.dev")
elif _build_arg == "stg":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.stg")
elif _build_arg == "prod":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.prod")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")

application = get_wsgi_application()
