from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contacts/", views.contacts, name="contacts"),
    path("login/", views.login_request, name="login_request"),
    path("signup/", views.signupuser, name="signup"),
    path("logout/", views.logout_request, name="logout_request"),
    path("social-auth/", include("social_django.urls", namespace="social")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
