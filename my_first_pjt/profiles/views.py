from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile


@login_required 
def profile_view(request):
    userProfile = get_object_or_404(UserProfile, user=request.user) 
    return render(request, 'profile.html', {'profile': UserProfile, 'user': request.user})
