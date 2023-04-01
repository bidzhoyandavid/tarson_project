from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError


# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def contacts(request):
    return render(request, 'core/contacts.html')

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'core/signup.html', {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'core/signup.html', {'form': UserCreationForm, 'error': 'The username is already exists'})
        else:
            return render(render, 'core/signup.html', {'form':UserCreationForm, 'error': "Password didn't match"})
        
def login(request):
    if request.method == 'GET':
        return render(request, 'core/login.html', {'form': AuthenticationForm})
    else:
        user = authenticate(request, username = request.POST['username'], password = request.POST['password'])
        if user is None:
            return render(request, 'core/login.html', {'form': AuthenticationForm, 'error': "The username doesn't exist"})
        else:
            login(request, user)
            return redirect('home')