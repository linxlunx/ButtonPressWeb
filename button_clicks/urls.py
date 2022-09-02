from django.urls import path
from . import views


urlpatterns = [
    path('', views.button_clicks_home, name='button_clicks_home'),
    path('api/', views.button_clicks_api_click, name='button_clicks_api_click'),
]
