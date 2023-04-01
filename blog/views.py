from django.shortcuts import render, HttpResponse
from .models import *

# Create your views here.
def blog(request):
    return render(request, 'blog/blog.html')