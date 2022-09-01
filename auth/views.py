from django.shortcuts import render, redirect
from django.contrib.auth import logout


def auth_login(request):
    return render(request, 'auth/login.html')


def auth_register(request):
    return render(request, 'auth/register.html')


def auth_logout(request):
    logout(request)
    return redirect()
