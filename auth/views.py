from django.shortcuts import render, redirect
from django.contrib.auth import logout
from . import forms


def auth_login(request):
    form = forms.AuthForm()
    return render(request, 'auth/login.html', {'form': form})


def auth_register(request):
    form = forms.AuthForm()
    return render(request, 'auth/register.html', {'form': form})


def auth_logout(request):
    logout(request)
    return redirect('home_index')
