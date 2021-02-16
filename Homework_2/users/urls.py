from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('create/', views.create_user, name = "create_user"),
    path('login1/', views.log_in, name="LogIn"),
    path('logout1/', views.log_out, name="LogOut"),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('usershome/', views.users_home, name="UsersHome"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]