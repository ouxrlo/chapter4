from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, CustomSignupForm



def login(request):
    form = AuthenticationForm()
    context = {"form": form}
    return render(request, "accounts/login.html", context)


def logout(request):
    auth_logout(request)
    return redirect("index.html")


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save
            return redirect ("user/userprofile")
        else:
            form = UserCreationForm()
        context = {'form': form}
        return render(request, 'accounts/signup.html', context)
        

from .forms import SignUpForm

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # 사용자 생성
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = CustomUser.objects.create_user(username=username, email=email, password=password)
            
            # 로그인 처리 (로그인 후 인덱스로 리디렉션)
            login(request, user)
            
            return redirect('index')  # 인덱스 페이지로 리디렉션
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})



def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
    return redirect("index")


def profile_view(request):
    return render(request, 'accounts/profile.html')
