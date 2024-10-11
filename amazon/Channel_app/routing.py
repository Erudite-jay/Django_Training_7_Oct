from django.urls import path
from . import consumers

ws_urlpatterns=[
    path('ws/sc/',consumers.MySyncConsumer.as_asgi()),
]