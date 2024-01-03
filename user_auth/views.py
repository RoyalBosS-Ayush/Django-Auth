from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, LoginForm


def signup(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard")
    else:
        form = SignUpForm()
    return render(request, "signup.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("dashboard")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})


@login_required
def dashboard(request):
    return render(request, "dashboard.html")


@login_required
def profile(request):
    return render(request, "profile.html")


@login_required
def user_logout(request):
    logout(request)
    return redirect("login")
