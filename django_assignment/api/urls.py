from django.urls import path
from .views import private_api, telegram_webhook

urlpatterns = [
    path('private-api/', private_api, name='private-api'),
    path('telegram-webhook/', telegram_webhook, name='telegram-webhook'),
]
