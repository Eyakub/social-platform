from django.urls import path
from login import views

app_name = 'login'

urlpatterns = [
    path('signup/', views.sign_up, name='sign_up'),
    path('login/', views.login_page, name='login'),
    path('edit/', views.edit_profile, name='edit'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    # path('user/', )
]
