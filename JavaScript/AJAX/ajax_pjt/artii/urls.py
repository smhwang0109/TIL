from django.urls import path
from . import views

app_name = 'art'

urlpatterns = [
    path('ping/', views.ping),
    path('pong/', views.pong),
]