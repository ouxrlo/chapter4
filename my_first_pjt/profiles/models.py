
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField('users.CustomUser', on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)  # 프로필 사진
    birth_date = models.DateField(blank=True, null=True)  # 생일

    def __str__(self):
        return f'{self.user.username} Profile'


    def __str__(self):
        return self.user.username
    

