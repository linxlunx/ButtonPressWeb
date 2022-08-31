from django.shortcuts import render


def auth_login(request):
    return render(request, 'auth/login.html')


def auth_register(request):
    return render(request, 'auth/register.html')
