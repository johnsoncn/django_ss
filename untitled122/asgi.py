"""
ASGI config for untitled122 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""


# python应用与web服务器之间的接口，不需要修改
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'untitled122.settings')

application = get_asgi_application()
