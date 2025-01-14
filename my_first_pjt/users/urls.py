from django.urls import path
from . import views

app_name = 'users' 

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),  
    path('login/', views.login_view, name='login'),
    path('users/profile/', views.profile_view, name='profile'),
    path("signup/", views.signup, name="signup"),
    path("delete/", views.delete, name="delete"), 
]
