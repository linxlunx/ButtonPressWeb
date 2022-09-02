from django.db import models
from django.contrib.auth.models import User


class ButtonClickLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'button_click_logs'

    def __str__(self):
        return self.created_at.strftime('%Y-%m-%d %H:%M:%S')
