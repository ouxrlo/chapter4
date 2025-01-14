from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login

def index(request):
    return render(request, 'index.html')

def users(request):
    context = {'name' : 'ouxrlo'}
    return render(request, 'users.html', context)


def profile(request):
    user = get_object_or_404('User', username='username')
    return render(request, 'users/profile.html', {'user': user})   
    

def login_view(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            next_url = request.GET.get('next', 'users:profile')  # 로그인 후 리디렉션할 URL
            return redirect(next_url)
        return render(request, 'users/login.html', {'error': 'Invalid login credentials'})

    return render(request, 'users/login.html')
