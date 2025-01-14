from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout as auth_logout
from django.views.decorators.http import require_POST




def index(request):
    return render(request, 'index.html')


def users(request):
    context = {'name' : 'users: name'}
    return render(request, 'users.html', context)


def profile(request):
    user = get_object_or_404('User', username='username')
    return render(request, 'users/profile.html', {'user': user})




@require_POST
def login_view(request):
    if request.method == "POST":
        auth_logout(request)
    return redirect('index')

