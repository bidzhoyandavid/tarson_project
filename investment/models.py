from django.db import models

# Create your models here.


# -------------------------- company overview and
class Company(models.Model):
    name = models.CharField(
        max_length=255, null=False, blank=False, verbose_name="name"
    )
    symbol = models.CharField(
        max_length=30, null=False, blank=False, verbose_name="symbol"
    )
    status = models.CharField(
        max_length=10, null=False, blank=False, verbose_name="status"
    )
    ipo_date = models.DateField(verbose_name="IPO_date", null=True)
    cik = models.CharField(null=True, max_length=20, verbose_name="cik")
    sector = models.ForeignKey("Sector", on_delete=models.CASCADE, null=True)
    industry = models.ForeignKey("Industry", on_delete=models.CASCADE, null=True)
    exchange = models.ForeignKey("Exchange", on_delete=models.PROTECT, null=True)
    security_type = models.ForeignKey(
        "SecurityType", on_delete=models.PROTECT, null=True
    )
    date_upload = models.DateField(auto_now_add=True, verbose_name="date_upload")
    date_update = models.DateField(auto_now=True, verbose_name="date_update")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "StockCompany"
        verbose_name_plural = "StockCompanies"
        ordering = ["name"]


class CompanyRatios(models.Model):
    name = models.ForeignKey("Company", on_delete=models.CASCADE)
    date_at_findata = models.DateField(null=True, blank=False, verbose_name="date_at")
    market_cap = models.BigIntegerField(
        null=True, blank=False, verbose_name="market_cap"
    )
    ebitda = models.BigIntegerField(null=True, blank=False, verbose_name="ebitda")
    pe_ratio = models.FloatField(null=True, blank=False, verbose_name="pe_ratio")
    peg_ratio = models.FloatField(null=True, blank=False, verbose_name="peg_ratio")
    book_value = models.FloatField(null=True, blank=False, verbose_name="book_value")
    dividend_per_share = models.FloatField(
        null=True, blank=False, verbose_name="dividend_per_share"
    )
    dividend_yield = models.FloatField(
        null=True, blank=False, verbose_name="dividend_yield"
    )
    eps = models.FloatField(null=True, blank=False, verbose_name="eps")
    revenue_per_share = models.FloatField(
        null=True, blank=False, verbose_name="revenue_per_share"
    )
    profit_margin_ttm = models.FloatField(
        null=True, blank=False, verbose_name="profit_margin_ttm"
    )
    operating_margin_ttm = models.FloatField(
        null=True, blank=False, verbose_name="operating_margin_ttm"
    )
    roa_ttm = models.FloatField(null=True, blank=False, verbose_name="roa_ttm")
    roe_ttm = models.FloatField(null=True, blank=False, verbose_name="roe_ttm")
    revenue_ttm = models.BigIntegerField(
        null=True, blank=False, verbose_name="revenue_ttm"
    )
    gross_profit_ttm = models.BigIntegerField(
        null=True, blank=False, verbose_name="gross_profit_ttm"
    )
    diluted_eps_ttm = models.FloatField(
        null=True, blank=False, verbose_name="diluted_eps_ttm"
    )
    trailing_pe = models.FloatField(null=True, blank=False, verbose_name="trailing_pe")
    forward_pe = models.FloatField(null=True, blank=False, verbose_name="forward_pe")
    price2sales_ratio = models.FloatField(
        null=True, blank=False, verbose_name="price2sales_ratio"
    )
    price2book_ratio = models.FloatField(
        null=True, blank=False, verbose_name="price2book_ratio"
    )
    ev2revenue = models.FloatField(null=True, blank=False, verbose_name="ev2revenue")
    ev2ebitda = models.FloatField(null=True, blank=False, verbose_name="ev2ebitda")
    beta = models.FloatField(null=True, blank=False, verbose_name="beta")
    shares_outstanding = models.BigIntegerField(
        null=True, blank=False, verbose_name="shares_outstanding"
    )

    class Meta:
        verbose_name = "Company Ratio"
        verbose_name_plural = "Company Ratios"
        ordering = ["name"]


class Sector(models.Model):
    sector_name = models.CharField(
        max_length=50, null=False, blank=False, verbose_name="sector_name"
    )

    def __srt__(self):
        return self.sector_name

    class Meta:
        verbose_name = "Sector"
        verbose_name_plural = "Sectors"
        ordering = ("id",)


class Industry(models.Model):
    industry_name = models.CharField(
        max_length=100, null=False, blank=False, verbose_name="industry_name"
    )

    def __srt__(self):
        return self.industry_name

    class Meta:
        verbose_name = "Industry"
        verbose_name_plural = "Industries"
        ordering = ("id",)


class Exchange(models.Model):
    exchange_name = models.CharField(
        max_length=20, null=False, blank=False, verbose_name="exchange_name"
    )

    class Meta:
        verbose_name = "Exchange name"
        verbose_name_plural = "Exchange names"
        ordering = ["id"]


class SecurityType(models.Model):
    security_type = models.CharField(
        max_length=20, null=False, blank=False, verbose_name="security_type"
    )

    class Meta:
        verbose_name = "Security type"
        verbose_name_plural = "Security types"
        ordering = ["id"]


# ---------------- News section ----------------------
class SourceDomain(models.Model):
    source = models.CharField(
        max_length=50, null=False, blank=False, verbose_name="source"
    )
    domain = models.URLField(max_length=100)

    def __str__(self):
        return self.source

    class Meta:
        verbose_name = "Source Domain"
        verbose_name_plural = "Source Domains"
        ordering = ("id",)


class NewsCategory(models.Model):
    category = models.CharField(
        max_length=50, null=False, blank=False, verbose_name="category"
    )

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = "News Category"
        verbose_name_plural = "News Categories"
        ordering = ("id",)


class NewsSentiment(models.Model):
    sentiment = models.CharField(
        max_length=30, null=False, blank=False, verbose_name="sentiment"
    )
    range = models.CharField(
        max_length=40, null=False, blank=False, verbose_name="range"
    )

    def __str__(self):
        return self.sentiment

    class Meta:
        verbose_name = "News Sentiment"
        verbose_name_plural = "News Sentiments"
        ordering = ["id"]


class NewsTopics(models.Model):
    topics = models.CharField(
        max_length=100, null=False, blank=False, verbose_name="topic"
    )

    def __str__(self):
        return self.topics

    class Meta:
        verbose_name = "News Topic"
        verbose_name_plural = "News Topics"
        ordering = ("id",)


class News(models.Model):
    title = models.TextField(null=False, verbose_name="title")
    url = models.URLField(max_length=5000, verbose_name="url", null=True)
    time_published = models.DateTimeField(null=True, verbose_name="time_published")
    summary = models.TextField(null=True, verbose_name="summary")
    source = models.ForeignKey("SourceDomain", on_delete=models.CASCADE, null=True)
    category = models.ForeignKey("NewsCategory", on_delete=models.CASCADE, null=True)
    score = models.FloatField(null=True, verbose_name="score")
    sentiment = models.ForeignKey("NewsSentiment", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"
        ordering = ["id", "time_published"]


class NewsCompanyConnection(models.Model):
    company = models.ForeignKey("Company", on_delete=models.CASCADE, null=True)
    news = models.ForeignKey("News", on_delete=models.CASCADE, null=True)
    relevance = models.FloatField()
    ticker_sentiment_score = models.FloatField(null=True)
    ticker_sentiment_label = models.ForeignKey(
        "NewsSentiment", on_delete=models.CASCADE, null=True
    )


class NewsTopicsConnection(models.Model):
    news = models.ForeignKey("News", on_delete=models.CASCADE, null=True)
    topic = models.ForeignKey("NewsTopics", on_delete=models.CASCADE, null=True)
    relevance = models.FloatField()


# ---------------------- Company fundamental data -----------------


# this class is for 'dry' concept
class CompanyCommon(models.Model):
    company = models.ForeignKey("Company", on_delete=models.CASCADE)
    fiscal_date = models.DateField(null=False, blank=False, verbose_name="fiscal_date")
    currency = models.CharField(
        max_length=10, null=False, blank=False, verbose_name="currency"
    )
    period = models.ForeignKey("ReportPeriod", on_delete=models.CASCADE, null=True)


class CompanyIncomeStatement(CompanyCommon):
    gross_profit = models.FloatField(null=True, verbose_name="gross_profit")
    total_revenue = models.FloatField(null=True, verbose_name="total_revenue")
    cost_of_revenue = models.FloatField(null=True, verbose_name="cost_of_revenue")
    cost_of_goos_sold = models.FloatField(null=True, verbose_name="cost_of_goods_sold")
    operating_income = models.FloatField(null=True, verbose_name="operating_income")
    selling_general_and_admin = models.FloatField(
        null=True, verbose_name="selling_general_and_admin"
    )
    rnd = models.FloatField(null=True, verbose_name="rnd")
    operating_expenses = models.FloatField(null=True, verbose_name="operating_expenses")
    investment_income_net = models.FloatField(
        null=True, verbose_name="investment_income_net"
    )
    net_interest_income = models.FloatField(
        null=True, verbose_name="net interest income"
    )
    interest_income = models.FloatField(null=True, verbose_name="interest_income")
    interest_expense = models.FloatField(null=True, verbose_name="interest_expense")
    non_interest_income = models.FloatField(
        null=True, verbose_name="non_interest_income"
    )
    other_nonoper_income = models.FloatField(
        null=True, verbose_name="other_nonoper_income"
    )
    depreciation = models.FloatField(null=True, verbose_name="depreciation")
    depreciation_and_amortization = models.FloatField(
        null=True, verbose_name="depreciation_and_amortization"
    )
    income_before_tax = models.FloatField(null=True, verbose_name="income_before_tax")
    income_tax_expense = models.FloatField(null=True, verbose_name="income_tax_expense")
    interest_debt_expense = models.FloatField(
        null=True, verbose_name="interest_debt_expense"
    )
    net_income_from_contin_operations = models.FloatField(
        null=True, verbose_name="net_income_from_contin_operations"
    )
    comprehensive_income_net_of_tax = models.FloatField(
        null=True, verbose_name="comprehensive_income_net_of_tax"
    )
    ebit = models.FloatField(null=True, verbose_name="ebit")
    ebitda = models.FloatField(null=True, verbose_name="ebitda")
    net_income = models.FloatField(null=True, verbose_name="net_income")

    class Meta:
        verbose_name = "Company Income Statement"
        verbose_name_plural = "Companies Income Statement"
        ordering = ["company", "fiscal_date"]


class CompanyBalanceSheet(CompanyCommon):
    total_assets = models.FloatField(null=True, verbose_name="total_assets")
    total_current_assets = models.FloatField(
        null=True, verbose_name="total_current_assets"
    )
    cash_and_equiv = models.FloatField(null=True, verbose_name="cash_and_equiv")
    cash_and_shortinvestment = models.FloatField(
        null=True, verbose_name="cash_and_shortinvestment"
    )
    inventory = models.FloatField(null=True, verbose_name="inventory")
    current_net_recievables = models.FloatField(
        null=True, verbose_name="current_net_recievables"
    )
    total_non_current_assets = models.FloatField(
        null=True, verbose_name="total_noncurrent_assets"
    )
    proprety_plan_equipment = models.FloatField(
        null=True, verbose_name="property_plan_equipment"
    )
    accumulated_deprec_amort = models.FloatField(
        null=True, verbose_name="accumulated_deprec_amort"
    )
    intagible_assets = models.FloatField(null=True, verbose_name="intangible_assets")
    intagible_assets_exc_goodwill = models.FloatField(
        null=True, verbose_name="intangible_assets_exc_goodwill"
    )
    goodwill = models.FloatField(null=True, verbose_name="goodwill")
    investments = models.FloatField(null=True, verbose_name="investments")
    long_term_investment = models.FloatField(
        null=True, verbose_name="long_term_investment"
    )
    short_term_investment = models.FloatField(
        null=True, verbose_name="short_term_investment"
    )
    other_current_assets = models.FloatField(
        null=True, verbose_name="other_current_assets"
    )
    other_noncurrent_assets = models.FloatField(
        null=True, verbose_name="other_noncurrent_assets"
    )
    total_liabilities = models.FloatField(null=True, verbose_name="total_liabilities")
    total_current_liabilities = models.FloatField(
        null=True, verbose_name="total_current_liabilities"
    )
    current_accounts_payable = models.FloatField(
        null=True, verbose_name="current_accounts_payable"
    )
    deferred_revenue = models.FloatField(null=True, verbose_name="deferred_revenue")
    current_debt = models.FloatField(null=True, verbose_name="current_debt")
    short_term_debt = models.FloatField(null=True, verbose_name="short_term_debt")
    total_noncurrent_liab = models.FloatField(
        null=True, verbose_name="total_noncurrent_liab"
    )
    capital_lease_obligations = models.FloatField(
        null=True, verbose_name="capital_lease_obligations"
    )
    long_term_debt = models.FloatField(null=True, verbose_name="long_term_debt")
    current_long_term_debt = models.FloatField(
        null=True, verbose_name="current_long_term_debt"
    )
    long_term_noncurrent = models.FloatField(
        null=True, verbose_name="long_term_noncurrent"
    )
    short_long_term_debt_total = models.FloatField(
        null=True, verbose_name="short_long_term_debt_total"
    )
    other_current_liab = models.FloatField(null=True, verbose_name="other_current_liab")
    other_noncurrent_liab = models.FloatField(
        null=True, verbose_name="other_noncurrent_liab"
    )
    total_shareholder_equity = models.FloatField(
        null=True, verbose_name="totak_shareholder_equity"
    )
    treasury_stock = models.FloatField(null=True, verbose_name="treasury_stock")
    retained_earnings = models.FloatField(null=True, verbose_name="retained_earnings")
    common_stock = models.FloatField(null=True, verbose_name="common_stock")
    common_stock_shares_outstand = models.FloatField(
        null=True, verbose_name="common_stock_shares_outstan"
    )

    class Meta:
        verbose_name = "Company Balance Sheet"
        verbose_name_plural = "Companies Balance Sheets"
        ordering = ["company", "fiscal_date"]


class CompanyCashFlow(CompanyCommon):
    operating_cashflow = models.FloatField(null=True, verbose_name="operating_cashflow")
    payment_from_oper_activities = models.FloatField(
        null=True, verbose_name="payment_from_oper_activities"
    )
    proceeds_from_oper_activities = models.FloatField(
        null=True, verbose_name="proceeds_from_oper_activities"
    )
    change_in_oper_liab = models.FloatField(
        null=True, verbose_name="change_in_oper_liab"
    )
    change_in_oper_assets = models.FloatField(
        null=True, verbose_name="change_in_oper_assets"
    )
    deprec_depletion_amort = models.FloatField(
        null=True, verbose_name="deprec_deplet_amort"
    )
    capital_expenditures = models.FloatField(
        null=True, verbose_name="capital_expenditures"
    )
    change_in_recievables = models.FloatField(
        null=True, verbose_name="change_in_recievables"
    )
    change_in_inventory = models.FloatField(
        null=True, verbose_name="change_in_inventory"
    )
    profit_loss = models.FloatField(null=True, verbose_name="profit_loss")
    cashflow_from_investment = models.FloatField(
        null=True, verbose_name="cashflow_from_investment"
    )
    cashflow_from_financing = models.FloatField(
        null=True, verbose_name="cashflow_from_financing"
    )
    proceeds_from_repayment_of_short_term_debt = models.FloatField(
        null=True, verbose_name="proceeds_from_repayment_of_short_term_debt"
    )
    payments_for_repurchase_of_common_stocks = models.FloatField(
        null=True, verbose_name="paymenys_for_repayment_of_repurchase_common_stocks"
    )
    payment_for_repurchase_of_equity = models.FloatField(
        null=True, verbose_name="payment_for_repurchase_equity"
    )
    payment_for_repurchase_of_preferred_stock = models.FloatField(
        null=True, verbose_name="payment_for_repurchase_of_preferred_stock"
    )
    dividend_payout = models.FloatField(null=True, verbose_name="dividend_payout")
    dividend_payout_common_stock = models.FloatField(
        null=True, verbose_name="dividend_payout_common_stock"
    )
    dividend_payout_preferred_stock = models.FloatField(
        null=True, verbose_name="dividend_payout_preferred_stock"
    )
    proceeds_from_issuance_of_common_stocks = models.FloatField(
        null=True, verbose_name="proceeds_from_issuance_of_common_stocks"
    )
    proceeds_from_issuance_of_long_term_debt = models.FloatField(
        null=True, verbose_name="proceeds_from_issuance_of_long_term_debt"
    )
    proceeds_from_issuance_of_preferres_stocks = models.FloatField(
        null=True, verbose_name="proceeds_from_issuance_of_preferred_stocks"
    )
    proceeds_from_repurchase_of_equity = models.FloatField(
        null=True, verbose_name="proceeds_of_repurchase_equity"
    )
    proceeds_from_sale_of_treasury_stock = models.FloatField(
        null=True, verbose_name="proceeds_from_sale_of_treasury_stock"
    )
    change_in_cash_and_equiv = models.FloatField(
        null=True, verbose_name="change_in_cash_and_equiv"
    )
    change_in_exchange_rate = models.FloatField(
        null=True, verbose_name="change_in_exchange_rate"
    )
    net_income = models.FloatField(null=True, verbose_name="net_income")

    class Meta:
        verbose_name = "Company Cash Flow"
        verbose_name_plural = "Companys' Cash Flow"
        ordering = ["company", "fiscal_date"]


class ReportPeriod(models.Model):
    period = models.CharField(null=False, max_length=20, verbose_name="period")

    def __str__(self):
        return self.period

    class Meta:
        verbose_name = "Report Period"
        verbose_name_plural = "Report Periods"
        ordering = ("id",)


# ----------------------- stock prices -----------------------


class PricePeriod(models.Model):
    period = models.CharField(
        max_length=20, null=False, blank=False, verbose_name="period"
    )  # add semiannual

    class Meta:
        verbose_name = "Price Period"
        verbose_name_plural = "Price Periods"
        ordering = ("id",)


class StockPrices(models.Model):
    stock = models.ForeignKey("Company", on_delete=models.CASCADE)
    date_at = models.DateField(verbose_name="date", null=False)
    open = models.FloatField(null=False, verbose_name="open")
    high = models.FloatField(null=False, verbose_name="high")
    low = models.FloatField(null=False, verbose_name="low")
    close = models.FloatField(null=False, verbose_name="close")
    volume = models.BigIntegerField(null=True, verbose_name="volume")
    # trade_count = models.BigIntegerField(null=True, verbose_name='trade_count')
    # vwap = models.FloatField(null=True, verbose_name='vwap')
    period = models.ForeignKey("PricePeriod", on_delete=models.CASCADE, null=True)

    def __srt__(self):
        return self.id_stock

    class Meta:
        verbose_name = "StockPrices"
        verbose_name_plural = "StockPrices"
        ordering = ["stock", "date_at"]


# ----------------------- RISK section ----------------
class StockRisk(models.Model):
    stock = models.ForeignKey("Company", on_delete=models.CASCADE)
    date_at = models.DateField(verbose_name="date_at", blank=False, null=False)
    historical_var = models.FloatField(
        blank=False, null=True, verbose_name="historical_var"
    )
    ewma_var = models.FloatField(null=True, blank=False, verbose_name="ewma_var")
    parametric_var = models.FloatField(
        null=True, blank=False, verbose_name="parametric_var"
    )
    sharp_ratio = models.FloatField(null=True, blank=False, verbose_name="sharp_ratio")
    sortino_ratio = models.FloatField(
        null=True, blank=False, verbose_name="sortino_ratio"
    )
    treynor_ratio = models.FloatField(
        null=True, blank=False, verbose_name="trainor_ratio"
    )
    log_return = models.FloatField(null=True, verbose_name="log_return")

    class Meta:
        verbose_name = "Stock Risk"
        verbose_name_plural = "Stocks Risks"
        ordering = ["stock", "date_at"]


# ----------------- crypto --------------------------------
class PhysicalCurrency(models.Model):
    currency_code = models.CharField(
        max_length=10, null=False, blank=False, verbose_name="currency_code"
    )
    currency_name = models.CharField(
        max_length=40, null=False, blank=False, verbose_name="currency_name"
    )

    def __str__(self):
        return self.currency_name

    class Meta:
        verbose_name = "Physical Currency"
        verbose_name_plural = "Physical Currencies"
        ordering = ("id",)


class DigitalCurrency(models.Model):
    currency_code = models.CharField(
        max_length=10, null=False, blank=False, verbose_name="currency_code"
    )
    currency_name = models.CharField(
        max_length=40, null=False, blank=False, verbose_name="currency_name"
    )

    def __str__(self):
        return self.currency_name

    class Meta:
        verbose_name = "Digital Currency"
        verbose_name_plural = "Digital Currencies"
        ordering = ("id",)


class CryptoPrice(models.Model):
    digital = models.ForeignKey("DigitalCurrency", on_delete=models.CASCADE)
    market = models.ForeignKey("PhysicalCurrency", on_delete=models.CASCADE)
    open = models.FloatField(null=False)
    high = models.FloatField(null=False)
    low = models.FloatField(null=False)
    close = models.FloatField(null=False)
    date_at = models.DateField(null=False)
    volume = models.FloatField(null=False)
    marketcap = models.FloatField(null=False)
    period = models.ForeignKey("PricePeriod", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Crypto price"
        verbose_name_plural = "Crypto prices"
        ordering = ["digital", "date_at"]


# --------------------- commodities --------------------


class Commodity(models.Model):
    CommodityType = models.CharField(
        max_length=30, null=False, blank=False, verbose_name="CommodityType"
    )

    class Meta:
        verbose_name = "Commodity"
        verbose_name_plural = "Commodities"
        ordering = ("id",)


class CommodityPrice(models.Model):
    commodity = models.ForeignKey("Commodity", on_delete=models.CASCADE)
    date_at = models.DateField(null=True)
    value = models.FloatField(null=True)
    timeframe = models.ForeignKey("PricePeriod", on_delete=models.CASCADE, null=True)


# -------------------- economic indicators ------------------


class Indicator(models.Model):
    indicatorType = models.CharField(
        max_length=20, null=False, blank=False, verbose_name="indicatorType"
    )

    class Meta:
        verbose_name = "Indicator"
        verbose_name_plural = "Indicators"
        ordering = ("id",)


class Maturity(models.Model):
    maturityType = models.CharField(
        max_length=10, null=False, blank=False, verbose_name="maturityType"
    )

    class Meta:
        verbose_name = "Maturity"
        verbose_name_plural = "Maturities"
        ordering = ["id"]


class IndicatorValue(models.Model):
    indicator = models.ForeignKey("Indicator", on_delete=models.CASCADE)
    date_at = models.DateField(null=True)
    interval = models.ForeignKey("PricePeriod", on_delete=models.CASCADE, null=True)
    maturity = models.ForeignKey("Maturity", on_delete=models.CASCADE, null=True)
    value = models.FloatField(null=True)
    unit = models.CharField(max_length=50, null=True)
