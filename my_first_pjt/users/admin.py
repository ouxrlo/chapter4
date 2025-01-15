from django.contrib import admin
from .models import CustomUser


#CustomUser 모델 관리자 페이지에 등록
admin.site.register(CustomUser)

