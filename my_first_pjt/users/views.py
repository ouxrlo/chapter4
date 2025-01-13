from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def users(request):
    context = {'name' : 'ouxrlo'}
    return render(request, 'users.html', context)

def login(request):
    return render(request, 'login.html')