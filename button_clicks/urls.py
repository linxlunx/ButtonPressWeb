from django.urls import path
from . import views


urlpatterns = [
    path('', views.button_clicks_home, name='button_clicks_home'),
]