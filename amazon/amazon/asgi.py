"""
ASGI config for amazon project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter

from Channel_app import routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'amazon.settings')

application = ProtocolTypeRouter(
    {
        'http':get_asgi_application(),
        'websocket': URLRouter(routing.ws_urlpatterns),  # Add your WebSocket URL routing here.
    }
)

