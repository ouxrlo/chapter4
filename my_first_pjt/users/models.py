### 사용자 인증 시스템을 구성할 때 사용되는 모델
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):

    # # 프로필 이미지 
    profile_image = models.ImageField(upload_to='queen.jpg/', null=True, blank=True)

    # 소개글 
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.username




## 이미지 경로 저장

class Product(models.Model):
    name = models.CharField(max_length=100)
    image_path = models.CharField(max_length=255)  

    def __str__(self):
        return self.name