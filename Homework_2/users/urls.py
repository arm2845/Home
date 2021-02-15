from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_user, name = "create_user"),
    path('login/', views.log_in, name="LogIn"),
    path('logout/', views.log_out, name="LogOut"),
]