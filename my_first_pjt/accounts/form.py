from django import forms


class UserForm(forms.Form):
    title = forms.CharField(max_length=10)
    content = forms.CharField()