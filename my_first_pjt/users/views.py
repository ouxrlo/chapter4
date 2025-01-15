from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.views.generic import CreateView
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import logout, get_user_model
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import UserProfile
from .forms import CustomSignupForm





def index(request):
    return render(request, 'index.html')


def index_view(request):
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
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST.get('email', '')

        
        User = get_user_model()

        
        user = User.objects.create_user(username=username, password=password, email=email)

        return HttpResponse(f"User {user.username} created successfully!")
    return render(request, 'signup.html')






User = get_user_model()

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        # 사용자 생성
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()

        # 회원 가입 성공 후 인덱스 페이지로 리디렉션
        return redirect('index')  # 'index'는 인덱스 페이지에 대한 URL 패턴 이름입니다.

    return render(request, 'accounts/signup.html')


class CustomSignupView(CreateView):
    model = User
    form_class = CustomSignupForm
    template_name = 'accounts/signup.html'  # 회원가입 템플릿 경로
    success_url = reverse_lazy('home')  # 회원가입 성공 후 이동할 URL

    def form_valid(self, form):
        response = super().form_valid(form)
        return response





