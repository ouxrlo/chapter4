from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomSignupForm



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
        

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('index')
    else:
        form = CustomSignupForm()
    
    return render(request, 'accounts/signup.html', {'form': form})



def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
    return redirect("index")