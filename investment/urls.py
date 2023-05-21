from django.contrib import admin
from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path("", views.investment, name="investment"),
    path("search/", views.stock_search, name="stock_search"),
    path("stock/<str:symbol>", views.stock_symbol, name="stock_symbol"),
    path("screener/", views.stock_screener, name="stock_screener"),
    path("news/<int:pk>", views.stock_news, name="stock_news"),
    path("portfolio/", views.stock_portfolio, name="stock_portfolio"),
    path(
        "portfolio/<int:portf_id>",
        views.stock_portfolio_detail,
        name="stock_portfolio_detail",
    ),
]
