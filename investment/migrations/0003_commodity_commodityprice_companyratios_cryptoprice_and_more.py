# Generated by Django 4.1.7 on 2023-04-14 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("investment", "0002_reportperiod_alter_company_cik_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Commodity",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "CommodityType",
                    models.CharField(max_length=30, verbose_name="CommodityType"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CommodityPrice",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date_at", models.DateField()),
                ("value", models.FloatField()),
                (
                    "commodity",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="investment.commodity",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CompanyRatios",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date_at_findata", models.DateField(verbose_name="date_at")),
                (
                    "market_cap",
                    models.BigIntegerField(null=True, verbose_name="market_cap"),
                ),
                ("ebitda", models.BigIntegerField(null=True, verbose_name="ebitda")),
                ("pe_ratio", models.FloatField(null=True, verbose_name="pe_ratio")),
                ("peg_ratio", models.FloatField(null=True, verbose_name="peg_ratio")),
                ("book_value", models.FloatField(null=True, verbose_name="book_value")),
                (
                    "dividend_per_share",
                    models.FloatField(null=True, verbose_name="dividend_per_share"),
                ),
                (
                    "dividend_yield",
                    models.FloatField(null=True, verbose_name="dividend_yield"),
                ),
                ("eps", models.FloatField(null=True, verbose_name="eps")),
                (
                    "revenue_per_share",
                    models.FloatField(null=True, verbose_name="revenue_per_share"),
                ),
                (
                    "profit_margin_ttm",
                    models.FloatField(null=True, verbose_name="profit_margin_ttm"),
                ),
                (
                    "operating_margin_ttm",
                    models.FloatField(null=True, verbose_name="operating_margin_ttm"),
                ),
                ("roa_ttm", models.FloatField(null=True, verbose_name="roa_ttm")),
                ("roe_ttm", models.FloatField(null=True, verbose_name="roe_ttm")),
                (
                    "revenue_ttm",
                    models.BigIntegerField(null=True, verbose_name="revenue_ttm"),
                ),
                (
                    "gross_profit_ttm",
                    models.BigIntegerField(null=True, verbose_name="gross_profit_ttm"),
                ),
                (
                    "diluted_eps_ttm",
                    models.FloatField(null=True, verbose_name="diluted_eps_ttm"),
                ),
                (
                    "trailing_pe",
                    models.FloatField(null=True, verbose_name="trailing_pe"),
                ),
                ("forward_pe", models.FloatField(null=True, verbose_name="forward_pe")),
                (
                    "price2sales_ratio",
                    models.FloatField(null=True, verbose_name="price2sales_ratio"),
                ),
                (
                    "price2book_ratio",
                    models.FloatField(null=True, verbose_name="price2book_ratio"),
                ),
                ("ev2revenue", models.FloatField(null=True, verbose_name="ev2revenue")),
                ("ev2ebitda", models.FloatField(null=True, verbose_name="ev2ebitda")),
                ("beta", models.FloatField(null=True, verbose_name="beta")),
                (
                    "shares_outstanding",
                    models.BigIntegerField(
                        null=True, verbose_name="shares_outstanding"
                    ),
                ),
            ],
            options={
                "verbose_name": "Company Ratio",
                "verbose_name_plural": "Company Ratios",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="CryptoPrice",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("open", models.FloatField()),
                ("high", models.FloatField()),
                ("low", models.FloatField()),
                ("close", models.FloatField()),
                ("date_at", models.DateField()),
                ("volume", models.FloatField()),
                ("marketcap", models.FloatField()),
            ],
            options={
                "verbose_name": "Crypto price",
                "verbose_name_plural": "Crypto prices",
                "ordering": ["digital", "date_at"],
            },
        ),
        migrations.CreateModel(
            name="DigitalCurrency",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "currency_code",
                    models.CharField(max_length=10, verbose_name="currency_code"),
                ),
                (
                    "currency_name",
                    models.CharField(max_length=40, verbose_name="currency_name"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Indicator",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "indicatorType",
                    models.CharField(max_length=20, verbose_name="indicatorType"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="IndicatorValue",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date_at", models.DateField()),
                ("value", models.FloatField()),
                ("unit", models.CharField(max_length=50)),
                (
                    "indicator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="investment.indicator",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Industry",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "industry_name",
                    models.CharField(max_length=20, verbose_name="industry_name"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Maturity",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "maturityType",
                    models.CharField(max_length=10, verbose_name="maturityType"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="News",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.TextField(verbose_name="title")),
                ("url", models.URLField(verbose_name="url")),
                ("time_published", models.DateTimeField(verbose_name="time_published")),
                ("summary", models.TextField(verbose_name="summary")),
                ("banner_image", models.URLField(verbose_name="banner_image")),
                ("score", models.FloatField(verbose_name="score")),
            ],
            options={
                "verbose_name": "News",
                "verbose_name_plural": "News",
                "ordering": ["id", "time_published"],
            },
        ),
        migrations.CreateModel(
            name="NewsCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("category", models.CharField(max_length=50, verbose_name="category")),
            ],
        ),
        migrations.CreateModel(
            name="NewsCompanyConnection",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("relevance", models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name="NewsSentiment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "sentiment",
                    models.CharField(max_length=30, verbose_name="sentiment"),
                ),
                ("range", models.CharField(max_length=40, verbose_name="range")),
            ],
        ),
        migrations.CreateModel(
            name="NewsTopics",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("topics", models.CharField(max_length=100, verbose_name="topic")),
            ],
        ),
        migrations.CreateModel(
            name="NewsTopicsConnection",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("relevance", models.FloatField()),
                (
                    "news",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="investment.news",
                    ),
                ),
                (
                    "topic",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="investment.newstopics",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PhysicalCurrency",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "currency_code",
                    models.CharField(max_length=10, verbose_name="currency_code"),
                ),
                (
                    "currency_name",
                    models.CharField(max_length=40, verbose_name="currency_name"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PricePeriod",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("period", models.CharField(max_length=20, verbose_name="period")),
            ],
        ),
        migrations.CreateModel(
            name="Sector",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "sector_name",
                    models.CharField(max_length=20, verbose_name="sector_name"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SourceDomain",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("source", models.CharField(max_length=50, verbose_name="source")),
                ("domain", models.URLField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name="company",
            name="easy_to_borrow",
        ),
        migrations.RemoveField(
            model_name="company",
            name="exchange",
        ),
        migrations.RemoveField(
            model_name="company",
            name="fractionable",
        ),
        migrations.RemoveField(
            model_name="company",
            name="maintenance_margin_requirement",
        ),
        migrations.RemoveField(
            model_name="company",
            name="marginable",
        ),
        migrations.RemoveField(
            model_name="company",
            name="min_size_order",
        ),
        migrations.RemoveField(
            model_name="company",
            name="min_trade_increment",
        ),
        migrations.RemoveField(
            model_name="company",
            name="price_increment",
        ),
        migrations.RemoveField(
            model_name="company",
            name="shortable",
        ),
        migrations.RemoveField(
            model_name="company",
            name="tradable",
        ),
        migrations.RemoveField(
            model_name="company",
            name="uuid",
        ),
        migrations.DeleteModel(
            name="CompanyFinRatios",
        ),
        migrations.AddField(
            model_name="newscompanyconnection",
            name="company",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="investment.company"
            ),
        ),
        migrations.AddField(
            model_name="newscompanyconnection",
            name="news",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="investment.news"
            ),
        ),
        migrations.AddField(
            model_name="news",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="investment.newscategory",
            ),
        ),
        migrations.AddField(
            model_name="news",
            name="sentiment",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="investment.newssentiment",
            ),
        ),
        migrations.AddField(
            model_name="news",
            name="source",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="investment.sourcedomain",
            ),
        ),
        migrations.AddField(
            model_name="news",
            name="topic",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="investment.newstopics"
            ),
        ),
        migrations.AddField(
            model_name="indicatorvalue",
            name="interval",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="investment.priceperiod"
            ),
        ),
        migrations.AddField(
            model_name="indicatorvalue",
            name="maturity",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="investment.maturity"
            ),
        ),
        migrations.AddField(
            model_name="cryptoprice",
            name="digital",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="investment.digitalcurrency",
            ),
        ),
        migrations.AddField(
            model_name="cryptoprice",
            name="market",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="investment.physicalcurrency",
            ),
        ),
        migrations.AddField(
            model_name="cryptoprice",
            name="period",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="investment.priceperiod"
            ),
        ),
        migrations.AddField(
            model_name="companyratios",
            name="name",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="investment.company"
            ),
        ),
        migrations.AddField(
            model_name="stockprices",
            name="period",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="investment.priceperiod",
            ),
        ),
        migrations.AlterField(
            model_name="company",
            name="industry",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="investment.industry"
            ),
        ),
        migrations.AlterField(
            model_name="company",
            name="sector",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="investment.sector"
            ),
        ),
    ]