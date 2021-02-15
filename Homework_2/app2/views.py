from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Film


def general(request):
    return HttpResponse("Great job!")


def home(request):
    return render(request, 'homepage.html')
    # return render(request, 'homepage.html', {'question': question})


def actors(request):
    path = "C:/Users/User/Desktop/python_enviroments/my_env/Home/Homework_2/app2/static/sample.json"
    with open(path, 'r') as json_file:
        data = json.load(json_file)
    return render(request, 'actors.html', data)
    # movie = Movie.objects.all()
    # data = {'movies': movie}
    # return render(request, 'actors.html', data)


def film(request):
    film = Film.objects.all()
    filmdata = {"films": film}
    return render(request, "films.html", filmdata)