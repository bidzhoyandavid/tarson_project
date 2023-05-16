# Generated by Django 4.1.7 on 2023-04-26 05:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("investment", "0015_remove_stockprices_trade_count_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="company",
            name="sector",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="investment.sector",
            ),
        ),
    ]
