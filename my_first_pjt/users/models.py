from django.db import models
from django.contrib.auth.models import AbstractUser  

class CustomUser(AbstractUser):
    birthday = models.DateField(null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.username

class UserProfile(models.Model):
    user = models.OneToOneField('users.CustomUser', on_delete=models.CASCADE)  # 문자열로 참조
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username






