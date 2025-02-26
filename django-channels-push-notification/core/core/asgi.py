import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django_application = get_asgi_application()

from . import urls # noqa isort:skip 


application = ProtocolTypeRouter(

    {
        # source_code
        "http": get_asgi_application(),
        "websocket": URLRouter(urls.websocket_urlpatterns)

        # my code
        # "http": django_application,
        # "websocket": URLRouter(getattr(urls, "websocket_urlpatterns", []))
    }
)
