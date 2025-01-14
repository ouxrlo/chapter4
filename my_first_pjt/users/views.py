from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login , logout, get_user_model
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from .forms import CustomUserCreationForm


User = get_user_model()


def index(request):
    return render(request, 'index.html')


def users(request):
    context = {'name' : 'username'}
    return render(request, 'users.html', context)


def profile(request):
    user = get_object_or_404('User', username='username')
    return render(request, 'users/profile.html', {'user': user})


@login_required
def profile_view(request):
    userProfile = get_object_or_404(UserProfile, user=request.user)
    return render(request, 'profile.html', {'user': request.user})



@require_POST
def login_view(request):
    if request.method == "POST":
        auth_logout(request)
    return redirect('index')


@login_required
def delete(request):
    if request.method == 'POST':
        user = request.user
        user.delete()  # 사용자를 삭제
        logout(request)  # 사용자 로그아웃
        return redirect('accounts:signup')  # 회원탈퇴 후 회원가입 페이지로 리디렉션
    return render(request, 'users/delete_confirm.html')



def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/signup.html', {'form': form})

