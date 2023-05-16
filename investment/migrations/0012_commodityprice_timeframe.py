# Generated by Django 4.1.7 on 2023-04-18 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        (
            "investment",
            "0011_alter_companybalancesheet_accumulated_deprec_amort_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="commodityprice",
            name="timeframe",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="investment.priceperiod",
            ),
        ),
    ]
