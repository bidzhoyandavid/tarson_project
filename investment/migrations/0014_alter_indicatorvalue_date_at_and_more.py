# Generated by Django 4.1.7 on 2023-04-19 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("investment", "0013_alter_commodityprice_date_at_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="indicatorvalue",
            name="date_at",
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name="indicatorvalue",
            name="interval",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="investment.priceperiod",
            ),
        ),
        migrations.AlterField(
            model_name="indicatorvalue",
            name="maturity",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="investment.maturity",
            ),
        ),
        migrations.AlterField(
            model_name="indicatorvalue",
            name="unit",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="indicatorvalue",
            name="value",
            field=models.FloatField(null=True),
        ),
    ]
