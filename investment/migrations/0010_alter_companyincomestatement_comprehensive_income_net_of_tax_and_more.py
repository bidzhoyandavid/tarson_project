# Generated by Django 4.1.7 on 2023-04-18 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("investment", "0009_alter_companyratios_date_at_findata"),
    ]

    operations = [
        migrations.AlterField(
            model_name="companyincomestatement",
            name="comprehensive_income_net_of_tax",
            field=models.FloatField(
                null=True, verbose_name="comprehensive_income_net_of_tax"
            ),
        ),
        migrations.AlterField(
            model_name="companyincomestatement",
            name="cost_of_goos_sold",
            field=models.FloatField(null=True, verbose_name="cost_of_goods_sold"),
        ),
        migrations.AlterField(
            model_name="companyincomestatement",
            name="cost_of_revenue",
            field=models.FloatField(null=True, verbose_name="cost_of_revenue"),
        ),
        migrations.AlterField(
            model_name="companyincomestatement",
            name="depreciation",
            field=models.FloatField(null=True, verbose_name="depreciation"),
        ),
        migrations.AlterField(
            model_name="companyincomestatement",
            name="depreciation_and_amortization",
            field=models.FloatField(
                null=True, verbose_name="depreciation_and_amortization"
            ),
        ),
        migrations.AlterField(
            model_name="companyincomestatement",
            name="ebit",
            field=models.FloatField(null=True, verbose_name="ebit"),
        ),
        migrations.AlterField(
            model_name="companyincomestatement",
            name="ebitda",
            field=models.FloatField(null=True, verbose_name="ebitda"),
        ),
        migrations.AlterField(
            model_name="companyincomestatement",
            name="gross_profit",
            field=models.FloatField(null=True, verbose_name="gross_profit"),
        ),
        migrations.AlterField(
            model_name="companyincomestatement",
            name="income_before_tax",
            field=models.FloatField(null=True, verbose_name="income_before_tax"),
        ),
        migrations.AlterField(
            model_name="companyincomestatement",
            name="income_tax_expense",
            field=models.FloatField(null=True, verbose_name="income_tax_expense"),
        ),
        migrations.AlterField(
            model_name="companyincomestatement",
            name="interest_debt_expense",
            field=models.FloatField(null=True, verbose_name="interest_debt_expense"),
        ),
        migrations.AlterField(
            model_name="companyincomestatement",
            name="interest_expense",
            field=models.FloatField(null=True, verbose_name="interest_expense"),
        ),
        migrations.AlterField(
            model_name="companyincomestatement",
            name="interest_income",
            field=models.FloatField(null=True, verbose_name="interest_income"),
        ),
        migrations.AlterField(
            model_name="companyincomestatement",
            name="investment_income_net",
            field=models.FloatField(null=True, verbose_name="investment_income_net"),
        ),
        migrations.AlterField(
            model_name="companyincomestatement",
            name="net_income",
            field=models.FloatField(null=True, verbose_name="net_income"),
        ),
        migrations.AlterField(
            model_name="companyincomestatement",
            name="net_income_from_contin_operations",
            field=models.FloatField(
                null=True, verbose_name="net_income_from_contin_operations"
            ),
        ),
        migrations.AlterField(
            model_name="companyincomestatement",
            name="net_interest_income",
            field=models.FloatField(null=True, verbose_name="net interest income"),
        ),
        migrations.AlterField(
            model_name="companyincomestatement",
            name="non_interest_income",
            field=models.FloatField(null=True, verbose_name="non_interest_income"),
        ),
        migrations.AlterField(
            model_name="companyincomestatement",
            name="operating_expenses",
            field=models.FloatField(null=True, verbose_name="operating_expenses"),
        ),
        migrations.AlterField(
            model_name="companyincomestatement",
            name="operating_income",
            field=models.FloatField(null=True, verbose_name="operating_income"),
        ),
        migrations.AlterField(
            model_name="companyincomestatement",
            name="other_nonoper_income",
            field=models.FloatField(null=True, verbose_name="other_nonoper_income"),
        ),
        migrations.AlterField(
            model_name="companyincomestatement",
            name="rnd",
            field=models.FloatField(null=True, verbose_name="rnd"),
        ),
        migrations.AlterField(
            model_name="companyincomestatement",
            name="selling_general_and_admin",
            field=models.FloatField(
                null=True, verbose_name="selling_general_and_admin"
            ),
        ),
        migrations.AlterField(
            model_name="companyincomestatement",
            name="total_revenue",
            field=models.FloatField(null=True, verbose_name="total_revenue"),
        ),
    ]
