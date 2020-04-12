from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('new_review/', views.new),
    path('create_review/', views.create),
    path('review_detail/<int:review_pk>/', views.detail),
    path('edit_review/<int:review_pk>/', views.edit),
    path('delete_review/<int:review_pk>/', views.delete),
]