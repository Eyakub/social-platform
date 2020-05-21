from django.urls import path
from post import views

app_name = 'posts'

urlpatterns = [
    path('', views.home, name='home'),
    path('liked/<pk>/', views.liked, name='liked'),
    path('unliked/<pk>/', views.unliked, name='unliked'),
]
