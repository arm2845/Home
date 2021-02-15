from django.shortcuts import render, redirect
from . forms import UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate


def create_user(request):
    form = UserRegistrationForm()

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.data.get('username')
            password = form.data.get('password1')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
            return redirect('HomePage')
    return render(request, 'users/create_user.html', {'form': form})


def log_out(request):
    logout(request)
    return redirect('HomePage')


def log_in(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.data.get('username')
            password = form.data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('HomePage')

    form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form})