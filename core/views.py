from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError


# Create your views here.


def home(request):
    context = {}
    return render(request, "core/home.html", context=context)


def about(request):
    context = {}
    return render(request, "core/about.html", context=context)


def contacts(request):
    context = {}
    return render(request, "core/contacts.html", context=context)


def signupuser(request):
    if request.method == "GET":
        context = {"register_form": UserCreationForm}
        return render(request, "core/signup.html", context=context)
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"]
                )
                user.save()
                login(request, user)
                return redirect("home")
            except IntegrityError:
                context = {
                    "register_form": UserCreationForm,
                    "error": "The username is already exists",
                }
                return render(
                    request,
                    "core/signup.html",
                    context=context,
                )
        else:
            context = {
                "register_form": UserCreationForm,
                "error": "Password didn't match",
            }
            return render(
                request,
                "core/signup.html",
                context=context,
            )


def login(request):
    if request.method == "GET":
        context = {"login_form": AuthenticationForm}
        return render(request, "core/login.html", context=context)
    else:
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )
        if user is None:
            context = {
                "form": AuthenticationForm,
                "error": "Invalid username or password!",
            }
            return render(
                request,
                "core/login.html",
                context=context,
            )
        else:
            login(request, user)
            return redirect("home")
