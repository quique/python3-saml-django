"""
ASGI config for django_test project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.asgi import get_asgi_application

os.chdir(os.path.join(os.getcwd(), "django_test"))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_test.settings')

application = get_asgi_application()