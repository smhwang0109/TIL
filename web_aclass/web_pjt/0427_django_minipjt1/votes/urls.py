from django.urls import path
from . import views

app_name = 'votes'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('detail/<int:vote_pk>/', views.detail, name='detail'),
    path('<int:vote_pk>/comment_create/', views.comment_create, name='comment_create'),
    path('random/', views.random, name='random'),
]