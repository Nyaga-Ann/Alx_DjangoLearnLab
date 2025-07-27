# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.view_articles, name='view_articles'),
    path('articles/create/', views.create_article, name='create_article'),
    path('articles/edit/<int:pk>/', views.edit_article, name='edit_article'),
    path('articles/delete/<int:pk>/', views.delete_article, name='delete_article'),
]
