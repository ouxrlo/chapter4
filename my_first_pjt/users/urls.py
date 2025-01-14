# urls.py
from django.contrib.auth import views as auth_views  # 인증기능 손쉽게 해줌
from django.urls import path
from . import views

app_name = 'users' 

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),  
    path('login/', views.login_view, name='login'), 
]
