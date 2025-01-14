from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class UserForm(forms.Form):
    title = forms.CharField(max_length=10)
    content = forms.CharField()


class CustomSignupForm(UserCreationForm):
    profile_picture = forms.ImageField(required=False, label="profile image")
    birth_date = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={'type': 'date'}),
        label="Birth"
    )

    class Meta:
        model = User
        fields = ('profile_picture', 'username', 'email', 'password1', 'password2', 'birth_date')
