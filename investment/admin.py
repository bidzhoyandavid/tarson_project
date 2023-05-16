from django.contrib import admin
from .models import *
# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'symbol', 'cik', 'status')
    list_display_links = ('id', 'name', 'symbol')
    ordering = ('symbol',)

class SectorAdmin(admin.ModelAdmin):
    list_display = ('id', 'sector_name')
    list_display_links = ('sector_name',)
    search_fields = ('sector_name',)

class IndustryAdmin(admin.ModelAdmin):
    list_display = ('id', 'industry_name')
    list_display_links = ('industry_name',)
    search_fields = ('industry_name',)

class ExchangeAdmin(admin.ModelAdmin):
    list_display = ('id', 'exchange_name')
    list_display_links = ('id', 'exchange_name')
    search_fields = ('exchange_name',)

class SecurityTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'security_type')
    list_display_links = ('id', 'security_type')
    search_fields = ('security_type',)


class SoucreDomainAdmin(admin.ModelAdmin):
    list_display = ('id', 'source', 'domain')
    list_display_links = ('source',)
    search_fields = ('source',)

class NewsCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category')
    list_display_links = ('category',)
    search_fields = ('category',)

class NewsSentimentAdmin(admin.ModelAdmin):
    list_display = ('id', 'sentiment', 'range')
    list_display_links = ('sentiment', 'range')
    search_fields = ('sentiment',)

class NewsTopicsAdmin(admin.ModelAdmin):
    list_display = ('id', 'topics')
    list_display_links = ('topics',)
    ordering = ('topics',)

class PricePeriodAdmin(admin.ModelAdmin):
    list_display = ('id', 'period')
    list_display_links = ('period',)
    ordering = ('period',)

class ReportRepiodAdmin(admin.ModelAdmin):
    list_display = ('id', 'period')
    list_display_links = ('id', 'period')
    ordering = ['id']

class PhysicalCurrencyAdmin(admin.ModelAdmin):
    list_display = ('id', 'currency_code', 'currency_name')
    list_display_links = ('currency_code', 'currency_name')
    ordering = ('currency_code',)

class DigitalCurrencyAdmin(admin.ModelAdmin):
    list_display = ('id', 'currency_code', 'currency_name')
    list_display_links = ('currency_code', 'currency_name')
    ordering = ('currency_code',)

class CommodityAdmin(admin.ModelAdmin):
    list_display = ('id', 'CommodityType')
    list_display_links = ('CommodityType',)
    ordering = ('CommodityType',)

class IndicatorAdmin(admin.ModelAdmin):
    list_display = ('id', 'indicatorType')
    list_display_links = ('indicatorType',)
    ordering = ('indicatorType',)

class MaturityAdmin(admin.ModelAdmin):
    list_display = ('id', 'maturityType')
    list_display_links = ('maturityType',)
    ordering = ('maturityType',)



admin.site.register(Company, CompanyAdmin)
admin.site.register(Sector, SectorAdmin)
admin.site.register(Industry, IndustryAdmin)
admin.site.register(Exchange, ExchangeAdmin)
admin.site.register(SecurityType, SecurityTypeAdmin)
admin.site.register(SourceDomain, SoucreDomainAdmin)
admin.site.register(NewsCategory, NewsCategoryAdmin)
admin.site.register(NewsSentiment, NewsSentimentAdmin)
admin.site.register(NewsTopics, NewsTopicsAdmin)
admin.site.register(PricePeriod, PricePeriodAdmin)
admin.site.register(ReportPeriod, ReportRepiodAdmin)
admin.site.register(PhysicalCurrency, PhysicalCurrencyAdmin)
admin.site.register(DigitalCurrency, DigitalCurrencyAdmin)
admin.site.register(Commodity, CommodityAdmin)
admin.site.register(Indicator, IndicatorAdmin)
admin.site.register(Maturity, MaturityAdmin)
