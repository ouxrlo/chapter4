# urls.py
from django.contrib.auth import views as auth_views  # 인증기능 손쉽게 해줌
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(), name='login'), 
]
