from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from . import forms

WRONG_USER_PASSWORD_ALERT = 'Wrong Username/Password!'
SUCCESS_CREATE_USER_ALERT = 'Successfully Created User!'


def auth_login(request):
    form = forms.AuthLoginForm()
    if request.method == 'POST':
        form = forms.AuthLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if not user:
                form.add_error('username', WRONG_USER_PASSWORD_ALERT)
                return render(request, 'auth/login.html', {'form': form})
            if not user.is_active:
                form.add_error('username', WRONG_USER_PASSWORD_ALERT)
                return render(request, 'auth/login.html', {'form': form})
            login(request, user)
            return redirect('home_index')
    return render(request, 'auth/login.html', {'form': form})


def auth_register(request):
    form = forms.AuthRegisterForm()
    if request.method == 'POST':
        form = forms.AuthRegisterForm(request.POST)
        if form.is_valid():
            user = User(
                username=form.cleaned_data['username'],
                password=make_password(form.cleaned_data['password'])
            )
            user.save()
            messages.success(request, SUCCESS_CREATE_USER_ALERT)
            return redirect('auth_login')
    return render(request, 'auth/register.html', {'form': form})


def auth_logout(request):
    logout(request)
    return redirect('home_index')
