# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomSignupForm(UserCreationForm):
    profile_picture = forms.ImageField(required=False, label="Profile Image")
    birth_date = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={'type': 'date'}),
        label="Birth Date"
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'profile_picture', 'birth_date')
