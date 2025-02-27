from django.contrib import admin
from django.urls import path
from notification import views
from notification.consumers_me import MyNotificationConsumer
from notification.consumers import NotificationConsumer

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.notification_page_view, name="notification_page"),
    path("me/", views.notification_page_view_me, name="notification_page_me")
]


websocket_urlpatterns = [
    path("ws/notifications/",MyNotificationConsumer.as_asgi())
]

# websocket_urlpatterns = [
#     path("ws/notifications/", NotificationConsumer.as_asgi())
# ]
