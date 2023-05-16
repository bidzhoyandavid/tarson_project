from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.blog, name="blog"),
    path("post/<int:blog_id>", views.blog_post, name="blog_post"),
    path("search/", views.blog_search, name="blog_search"),
]
