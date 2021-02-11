from django.urls import path
from . import views

urlpatterns = [
    path('', views.general, name = "General"),
    path('homepage', views.home, name = "HomePage"),
    path('actors', views.actors, name = "BestActors"),
    path('films', views.film, name="film"),
]