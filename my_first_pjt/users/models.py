from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser




    
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_profile')  # related_name 추가
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s profile"
    

# users/models.py
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

# CustomUserManager 추가
class CustomUserManager(UserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        """일반 사용자 생성"""
        if not email:
            raise ValueError('Email address must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        """슈퍼유저 생성"""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, email, password, **extra_fields)


# CustomUser 모델 정의
class CustomUser(AbstractUser):
    birthday = models.DateField(null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    # CustomUserManager를 매니저로 설정
    objects = CustomUserManager()

    def __str__(self):
        return self.username
    





    











