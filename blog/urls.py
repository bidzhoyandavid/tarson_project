from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path("", views.blog, name="blog"),
    path("post/<int:blog_id>", views.blog_post, name="blog_post"),
    path("ckedit", include("ckeditor_uploader.urls")),
    path("tag/<slug:tag_slug>", views.blog, name="blog_by_tag"),
] + static(settings.MEDIA_URL, documnent_root=settings.MEDIA_ROOT)
