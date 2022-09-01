from django.shortcuts import render


def button_clicks_home(request):
    return render(request, 'button_clicks/home.html')
