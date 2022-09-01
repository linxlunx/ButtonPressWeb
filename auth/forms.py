from django import forms
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator

PASSWORD_VALIDATION_ALERT = 'Password must contain at least 8 characters and cannot be entirely numeric'
USERNAME_ALREADY_EXIST_ALERT = 'Username already exists'


class AuthLoginForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class AuthRegisterForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                               validators=[MinLengthValidator(8)])

    def clean_username(self):
        username = self.cleaned_data.get('username')
        # check if username is exists
        if User.objects.filter(username=username).first():
            raise forms.ValidationError(USERNAME_ALREADY_EXIST_ALERT)
        return username
