from typing import Any
from django.db.models.query import QuerySet, Q
import pandas as pd
import plotly.graph_objs as go
import plotly.offline as opy
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from .models import (
    Company,
    CompanyRatios,
    CompanyIncomeStatement,
    CompanyBalanceSheet,
    CompanyCashFlow,
    StockRisk,
    News,
    NewsCompanyConnection,
    NewsTopicsConnection,
    StockPortfolio,
)
from .forms import *
from django.contrib.auth.decorators import login_required


# Create your views here.
def investment(request):
    context = {}
    return render(request, "investment/invest.html", context=context)


def stock_search(request):
    model = Company
    query = request.GET.get("q")
    symbol_list = Company.objects.filter(symbol__startswith=query)
    context = {"symbol_list": symbol_list}
    return render(request, "investment/stock_search.html", context=context)


def stock_symbol(request, symbol):
    stock = Company.objects.filter(symbol__contains=symbol)
    if stock.exists():
        stock = stock.first()
    stock_ratios = CompanyRatios.objects.filter(name_id__symbol=symbol)
    stock_balance = CompanyBalanceSheet.objects.filter(
        companycommon_ptr_id__company_id__symbol=symbol
    ).latest("fiscal_date")
    stock_income = CompanyIncomeStatement.objects.filter(
        companycommon_ptr_id__company_id__symbol=symbol
    ).latest("fiscal_date")
    stock_cash = CompanyCashFlow.objects.filter(
        companycommon_ptr_id__company_id__symbol=symbol
    ).latest("fiscal_date")
    risk = StockRisk.objects.filter(stock_id__symbol=symbol).order_by("-date_at")[:252]
    riskData_latest = StockRisk.objects.filter(stock_id__symbol=symbol).latest(
        "date_at"
    )
    riskData = pd.DataFrame(list(risk.values()))

    stock_news = (
        News.objects.filter(newscompanyconnection__company__symbol=symbol)
        .values(
            "id",
            "title",
            "time_published",
            "score",
            "newscompanyconnection__ticker_sentiment_score",
            "newscompanyconnection__ticker_sentiment_label_id__sentiment",
        )
        .order_by("-time_published")[:10]
    )

    fig = go.Figure()
    fig.add_trace(
        go.Line(
            x=riskData["date_at"],
            y=riskData["log_return"],
            mode="lines",
            name="log return",
        )
    )
    fig.add_trace(
        go.Line(
            x=riskData["date_at"],
            y=riskData["historical_var"],
            mode="lines",
            name="Historical VaR",
        )
    )
    fig.add_trace(
        go.Line(
            x=riskData["date_at"], y=riskData["ewma_var"], mode="lines", name="EWMA VaR"
        )
    )
    fig.add_trace(
        go.Line(
            x=riskData["date_at"],
            y=riskData["parametric_var"],
            mode="lines",
            name="Parametric VaR",
        )
    )

    fig.update_layout(title="Value-at-Risk", xaxis_title="Date", yaxis_title="Return")

    # Convert the figure to HTML
    plot_div = opy.plot(fig, auto_open=False, output_type="div")

    context = {
        "stock": stock,
        "stock_ratios": stock_ratios,
        "stock_balance": stock_balance,
        "stock_income": stock_income,
        "stock_cash": stock_cash,
        "plot_div": plot_div,
        "riskData_latest": riskData_latest,
        "stock_news": stock_news,
    }
    return render(request, "investment/stock_symbol.html", context=context)


def stock_screener(request):
    context = {}
    return render(request, "investment/stock_screener.html", context=context)


def stock_news(request, pk):
    news_current = News.objects.get(pk=pk)
    context = {"news_current": news_current}
    return render(request, "investment/stock_news.html", context=context)


@login_required
def stock_portfolio(request):
    if request.method == "POST":
        form = CreatePortfolio(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.owner_id = request.user.id
            obj.save()
            form.save_m2m()
            return redirect("investment")
    else:
        form = CreatePortfolio

    context = {"form": form}
    return render(request, "investment/stock_portfolio.html", context=context)


@login_required
def stock_portfolio_detail(request, portf_id):
    portfolio = StockPortfolio_stocks.objects.get(stock_portfolio_id=portf_id)
    context = {"portfolio": portfolio}
    return render(request, "investment/stock_portfolio_detail.html", context=context)


def checkbox_search_view(request):
    form = CheckboxSearchForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            selected_options = form.cleaned_data["options"]
            # Do something with the selected options

    # Fetch the data from the Item model
    items = Company.objects.all()
    form.fields["options"].choices = [(item.id, item.name) for item in items]

    return render(request, "investment/checkbox_search.html", {"form": form})
