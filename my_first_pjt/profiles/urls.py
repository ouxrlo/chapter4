from django.contrib.auth import views 
from django.urls import path
from . import views

app_name = 'profile'

urlpatterns = [
    path('users/profile/', views.profile_view, name='uesrprofile'), 
]