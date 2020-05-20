from django.urls import path
from post import views

app_name = 'posts'

urlpatterns = [
    path('', views.home, name='home')
]
