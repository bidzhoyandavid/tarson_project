from django.db import models

# Create your models here.

# -------------------------- company overview and  
class Company(models.Model):
    name = models.CharField(max_length=255, null = False, blank = False, verbose_name='name')
    symbol = models.CharField(max_length=30, null = False, blank = False, verbose_name='symbol')
    status = models.CharField(max_length=10, null = False, blank=False, verbose_name='status')
    easy_to_borrow = models.BooleanField(verbose_name='easy_to_borrow')
    exchange = models.CharField(max_length=10, verbose_name='exchange')
    fractionable = models.BooleanField(verbose_name='fractionable')
    uuid = models.UUIDField(editable=False, verbose_name='uuid')
    maintenance_margin_requirement = models.FloatField(verbose_name='maintanance')
    marginable = models.BooleanField(verbose_name='marginable')
    min_size_order = models.FloatField(verbose_name='min_size_order')
    min_trade_increment = models.FloatField(verbose_name='min_trade_increment')
    price_increment = models.FloatField(verbose_name='price_increment')
    shortable = models.BooleanField(verbose_name='shortable')
    tradable = models.BooleanField(verbose_name='tradable')
    cik = models.CharField(max_length=20, verbose_name='cik')
    sector = models.CharField(max_length=100, verbose_name='sector')
    industry = models.CharField(max_length=100, verbose_name='industry')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "StockCompany"
        verbose_name_plural = "StockCompanies"
        ordering = ['name']


class CompanyFinRatios(models.Model):
    id_company = models.ForeignKey('Company', on_delete=models.CASCADE) # write
    date_at = models.DateField(null = False, blank = False, verbose_name='date_at')
    market_cap = models.BigIntegerField(null = False, blank = False, verbose_name='market_cap')
    ebitda = models.BigIntegerField(null = False, blank = False, verbose_name='ebitda')
    pe_ratio = models.FloatField(null = False, blank = False, verbose_name='pe_ratio')
    peg_ratio = models.FloatField(null = False, blank=False, verbose_name='peg_ratio')
    book_value = models.FloatField(null = False, blank=False, verbose_name='book_value')
    dividend_per_share = models.FloatField(null = False, blank = False, verbose_name='dividend_per_share')
    dividend_yield = models.FloatField(null = False, blank = False, verbose_name='dividend_yield')
    eps = models.FloatField(null = False, blank = False, verbose_name='eps')
    revenue_per_share = models.FloatField(null = False, blank = False, verbose_name='revenue_per_share')
    profit_margin_ttm = models.FloatField(null = False, blank = False, verbose_name='profit_margin_ttm')
    operating_margin_ttm = models.FloatField(null = False, blank = False, verbose_name='operating_margin_ttm')
    roa_ttm = models.FloatField(null = False, blank = False, verbose_name='roa_ttm')
    roe_ttm = models.FloatField(null = False, blank = False, verbose_name='roe_ttm')
    revenue_ttm = models.BigIntegerField(null = False, blank = False, verbose_name='revenue_ttm')
    gross_profit_ttm = models.BigIntegerField(null = False, blank = False, verbose_name='gross_profit_ttm')
    diluted_eps_ttm = models.FloatField(null = False, blank = False, verbose_name='diluted_eps_ttm')
    trailing_pe = models.FloatField(null = False, blank = False, verbose_name='trailing_pe')
    forward_pe = models.FloatField(null = False, blank = False, verbose_name='forward_pe')
    price2sales_ratio = models.FloatField(null = False, blank = False, verbose_name='price2sales_ratio')
    price2book_ratio = models.FloatField(null = False, blank = False, verbose_name='price2book_ratio')
    ev2revenue = models.FloatField(null = False, blank = False, verbose_name='ev2revenue')
    ev2ebitda = models.FloatField(null = False, blank = False, verbose_name='ev2ebitda')
    beta = models.FloatField(null = False, blank = False, verbose_name='beta')
    shares_outstanding = models.BigIntegerField(null = False, blank = False, verbose_name='shares_outstanding')

    class Meta:
        verbose_name = 'Company Financial Report'
        verbose_name_plural = 'Companies Financail Reports'
        ordering = ['id_company', 'date_at']


class StockPrices(models.Model):
    id_stock = models.ForeignKey('Company', on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=False, verbose_name='date', null = False)
    open = models.FloatField(null = False, verbose_name='open')
    high = models.FloatField(null = False, verbose_name='high')
    low = models.FloatField(null = False, verbose_name='low')
    close = models.FloatField(null = False, verbose_name='close')
    volume = models.BigIntegerField(null=False, verbose_name='volume')
    trade_count = models.BigIntegerField(null=False, verbose_name='trade_count')
    vwap = models.FloatField(null=False, verbose_name='vwap')

    def __srt__(self):
        return self.id_stock
    
    class Meta:
        verbose_name = 'StockPrices'
        verbose_name_plural = 'StockPrices'
        ordering = ['id_stock']


# this class is for 'dry' concept
class CompanyCommon(models.Model):
    id_company = models.ForeignKey('Company', on_delete=models.CASCADE)
    fiscal_date = models.DateField(null = False, blank = False, verbose_name='fiscal_date')
    currency = models.CharField(max_length=10, null = False, blank=False, verbose_name='currency')
   

class CompanyIncomeStatement(CompanyCommon):
    gross_profit = models.BigIntegerField( verbose_name='gross_profit')
    total_revenue = models.BigIntegerField( verbose_name='total_revenue')
    cost_of_revenue = models.BigIntegerField( verbose_name='cost_of_revenue')
    cost_of_goos_sold = models.BigIntegerField( verbose_name='cost_of_goods_sold')
    operating_income = models.BigIntegerField( verbose_name='operating_income')
    selling_general_and_admin = models.BigIntegerField( verbose_name='selling_general_and_admin')
    rnd = models.BigIntegerField( verbose_name='rnd')
    operating_expenses = models.BigIntegerField( verbose_name='operating_expenses')
    investment_income_net = models.BigIntegerField( verbose_name='investment_income_net')
    net_interest_income = models.BigIntegerField( verbose_name='net interest income')
    interest_income = models.BigIntegerField( verbose_name='interest_income')
    interest_expense = models.BigIntegerField( verbose_name='interest_expense')
    non_interest_income = models.BigIntegerField( verbose_name='non_interest_income')
    other_nonoper_income = models.BigIntegerField( verbose_name='other_nonoper_income')
    depreciation = models.BigIntegerField( verbose_name='depreciation')
    depreciation_and_amortization = models.BigIntegerField( verbose_name='depreciation_and_amortization')
    income_before_tax = models.BigIntegerField( verbose_name='income_before_tax')
    income_tax_expense = models.BigIntegerField( verbose_name='income_tax_expense')
    interest_debt_expense = models.BigIntegerField( verbose_name='interest_debt_expense')
    net_income_from_contin_operations = models.BigIntegerField( verbose_name='net_income_from_contin_operations')
    comprehensive_income_net_of_tax = models.BigIntegerField( verbose_name='comprehensive_income_net_of_tax')
    ebit = models.BigIntegerField( verbose_name='ebit')
    ebitda = models.BigIntegerField( verbose_name='ebitda')
    net_income = models.BigIntegerField( verbose_name='net_income')


    class Meta:
        verbose_name = 'Company Income Statement'
        verbose_name_plural = 'Companies Income Statement'
        ordering = ['id_company', 'fiscal_date']


class CompanyBalanceSheet(CompanyCommon):
    total_assets = models.BigIntegerField( verbose_name='total_assets')
    total_current_assets = models.BigIntegerField( verbose_name='total_current_assets')
    cash_and_equiv = models.BigIntegerField( verbose_name='cash_and_equiv')
    cash_and_shortinvestment = models.BigIntegerField( verbose_name='cash_and_shortinvestment')
    inventory = models.BigIntegerField( verbose_name='inventory')
    current_net_recievables = models.BigIntegerField( verbose_name='current_net_recievables')
    total_non_current_assets = models.BigIntegerField( verbose_name='total_noncurrent_assets')
    proprety_plan_equipment = models.BigIntegerField( verbose_name='property_plan_equipment')
    accumulated_deprec_amort = models.BigIntegerField( verbose_name='accumulated_deprec_amort')
    intagible_assets = models.BigIntegerField( verbose_name='intangible_assets')
    intagible_assets_exc_goodwill = models.BigIntegerField( verbose_name='intangible_assets_exc_goodwill')
    goodwill = models.BigIntegerField( verbose_name='goodwill')
    investments = models.BigIntegerField( verbose_name='investments')
    long_term_investment = models.BigIntegerField( verbose_name='long_term_investment')
    short_term_investment = models.BigIntegerField( verbose_name='short_term_investment')
    other_current_assets = models.BigIntegerField( verbose_name='other_current_assets')
    other_noncurrent_assets = models.BigIntegerField( verbose_name='other_noncurrent_assets')
    total_liabilities = models.BigIntegerField( verbose_name='total_liabilities')
    total_current_liabilities = models.BigIntegerField( verbose_name='total_current_liabilities')
    current_accounts_payable = models.BigIntegerField( verbose_name='current_accounts_payable')
    deferred_revenue = models.BigIntegerField( verbose_name='deferred_revenue')
    current_debt = models.BigIntegerField( verbose_name='current_debt')
    short_term_debt = models.BigIntegerField( verbose_name='short_term_debt')
    total_noncurrent_liab = models.BigIntegerField( verbose_name='total_noncurrent_liab')
    capital_lease_obligations = models.BigIntegerField( verbose_name='capital_lease_obligations')
    long_term_debt = models.BigIntegerField( verbose_name='long_term_debt')
    current_long_term_debt = models.BigIntegerField( verbose_name='current_long_term_debt')
    long_term_noncurrent = models.BigIntegerField( verbose_name='long_term_noncurrent')
    short_long_term_debt_total = models.BigIntegerField( verbose_name='short_long_term_debt_total')
    other_current_liab = models.BigIntegerField( verbose_name='other_current_liab')
    other_noncurrent_liab = models.BigIntegerField( verbose_name='other_noncurrent_liab')
    total_shareholder_equity = models.BigIntegerField( verbose_name='totak_shareholder_equity')
    treasury_stock = models.BigIntegerField( verbose_name='treasury_stock')
    retained_earnings = models.BigIntegerField( verbose_name='retained_earnings')
    common_stock = models.BigIntegerField( verbose_name='common_stock')
    common_stock_shares_outstand = models.BigIntegerField( verbose_name='common_stock_shares_outstan')


    class Meta:
        verbose_name = 'Company Balance Sheet'
        verbose_name_plural = 'Companies Balance Sheets'
        ordering = ['id_company', 'fiscal_date']


class CompanyCashFlow(CompanyCommon):
    operating_cashflow = models.BigIntegerField( verbose_name='operating_cashflow')
    payment_from_oper_activities = models.BigIntegerField( verbose_name='payment_from_oper_activities')
    proceeds_from_oper_activities = models.BigIntegerField( verbose_name='proceeds_from_oper_activities')
    change_in_oper_liab = models.BigIntegerField( verbose_name='change_in_oper_liab')
    change_in_oper_assets = models.BigIntegerField( verbose_name='change_in_oper_assets')
    deprec_depletion_amort = models.BigIntegerField( verbose_name='deprec_deplet_amort')
    capital_expenditures = models.BigIntegerField( verbose_name='capital_expenditures')
    change_in_recievables = models.BigIntegerField( verbose_name='change_in_recievables')
    change_in_inventory = models.BigIntegerField( verbose_name='change_in_inventory')
    profit_loss = models.BigIntegerField( verbose_name='profit_loss')
    cashflow_from_investment = models.BigIntegerField( verbose_name='cashflow_from_investment')
    cashflow_from_financing = models.BigIntegerField( verbose_name='cashflow_from_financing')
    proceeds_from_repayment_of_short_term_debt = models.BigIntegerField( verbose_name='proceeds_from_repayment_of_short_term_debt')
    payments_for_repurchase_of_common_stocks = models.BigIntegerField( verbose_name='paymenys_for_repayment_of_repurchase_common_stocks')
    payment_for_repurchase_of_equity = models.BigIntegerField( verbose_name='payment_for_repurchase_equity')
    payment_for_repurchase_of_preferred_stock = models.BigIntegerField( verbose_name='payment_for_repurchase_of_preferred_stock')
    dividend_payout = models.BigIntegerField( verbose_name='dividend_payout')
    dividend_payout_common_stock = models.BigIntegerField( verbose_name='dividend_payout_common_stock')
    dividend_payout_preferred_stock = models.BigIntegerField( verbose_name='dividend_payout_preferred_stock')
    proceeds_from_issuance_of_common_stocks = models.BigIntegerField( verbose_name='proceeds_from_issuance_of_common_stocks')
    proceeds_from_issuance_of_long_term_debt = models.BigIntegerField( verbose_name='proceeds_from_issuance_of_long_term_debt')
    proceeds_from_issuance_of_preferres_stocks = models.BigIntegerField( verbose_name='proceeds_from_issuance_of_preferred_stocks')
    proceeds_from_repurchase_of_equity = models.BigIntegerField( verbose_name='proceeds_of_repurchase_equity')
    proceeds_from_sale_of_treasury_stock = models.BigIntegerField( verbose_name='proceeds_from_sale_of_treasury_stock')
    change_in_cash_and_equiv = models.BigIntegerField( verbose_name='change_in_cash_and_equiv')
    change_in_exchange_rate = models.BigIntegerField( verbose_name='change_in_exchange_rate')
    net_income = models.BigIntegerField( verbose_name='net_income')

    class Meta:
        verbose_name = 'Company Cash Flow'
        verbose_name_plural = "Companys' Cash Flow"
        ordering = ['id_company', 'fiscal_date'] 



# a new database vision
class CompanyFinancialReport(CompanyCommon):
    reports_type = models.CharField(max_length=20, null = False, verbose_name='report_type')
    variable_name = models.CharField(max_length=100, null = False, verbose_name='variable_name')
    value = models.BigIntegerField(verbose_name='value')


# ----------------------- RISK section ----------------
class StockRisk(models.Model):
    id_stock = models.ForeignKey('Company', on_delete=models.CASCADE)
    date_at = models.DateField(verbose_name='date_at', blank = False, null = False)
    historical_var = models.FloatField(blank=False, null=False, verbose_name='historical_var')
    ewma_var = models.FloatField(null = False, blank = False, verbose_name='ewma_var')
    parametric_var = models.FloatField(null = False, blank = False, verbose_name='parametric_var')
    sharp_ratio = models.FloatField(null = False, blank = False, verbose_name='sharp_ratio')
    sortino_ratio = models.FloatField(null = False, blank = False, verbose_name='sortino_ratio')
    traynor_ratio = models.FloatField(null = False, blank = False, verbose_name='trainor_ratio')

    class Meta:
        verbose_name = 'Stock Risk'
        verbose_name_plural = 'Stocks Risks'
        ordering = ['id_stock', 'date_at']


