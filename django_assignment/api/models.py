from django.db import models

class TelegramUser(models.Model):
    username = models.CharField(max_length=150, blank=True, null=True)
    telegram_id = models.BigIntegerField(unique=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username or str(self.telegram_id)
