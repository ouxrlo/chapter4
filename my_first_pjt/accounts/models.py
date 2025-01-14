from django.db import models
from django.conf import settings

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='account_user_profile')  # related_name 추가
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s account profile"

