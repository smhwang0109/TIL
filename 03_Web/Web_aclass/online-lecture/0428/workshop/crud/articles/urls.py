from django.urls import path
from . import views 

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:article_pk>/like/', views.like, name='like'),
    path('<int:article_pk>/add_hashtag/', views.add_hashtag, name='add_hashtag'),
    path('<int:article_pk>/delete_hashtag/<int:hashtag_pk>/', views.delete_hashtag, name='delete_hashtag'),
]