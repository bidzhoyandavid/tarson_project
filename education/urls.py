from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path("", views.education, name="education"),
    path("<int:educ_id>/", views.educationPost, name="educationpost"),
    path("vocabulary/", views.vocabulary, name="vocabulary"),
    path("vocabulary/<str:title>", views.vocabularyItem, name="vocabularyitem"),
    path("ckedit", include("ckeditor_uploader.urls")),
] + static(settings.MEDIA_URL, documnent_root=settings.MEDIA_ROOT)
