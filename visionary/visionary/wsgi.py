"""
WSGI config for visionary project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "visionary.settings")

# Default
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Heroku
# from django.core.wsgi import get_wsgi_application
# from dj_static import Cling

# application = Cling(get_wsgi_application())
