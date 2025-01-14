### 사용자 인증 시스템을 구성할 때 사용되는 모델
from django.contrib.auth.models import AbstractUser, User
from django.db import models

class User(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)

    
    def __str__(self):
        return self.title 

class CustomUser(AbstractUser):

    birthday = models.DateField(null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile_pics/', null=True, blank=True) 
    # 소개글 
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.username





