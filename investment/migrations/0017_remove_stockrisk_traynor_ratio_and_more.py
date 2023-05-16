# Generated by Django 4.1.7 on 2023-04-28 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("investment", "0016_alter_company_sector"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="stockrisk",
            name="traynor_ratio",
        ),
        migrations.AddField(
            model_name="stockrisk",
            name="treynor_ratio",
            field=models.FloatField(null=True, verbose_name="trainor_ratio"),
        ),
        migrations.AlterField(
            model_name="stockrisk",
            name="ewma_var",
            field=models.FloatField(null=True, verbose_name="ewma_var"),
        ),
        migrations.AlterField(
            model_name="stockrisk",
            name="historical_var",
            field=models.FloatField(null=True, verbose_name="historical_var"),
        ),
        migrations.AlterField(
            model_name="stockrisk",
            name="parametric_var",
            field=models.FloatField(null=True, verbose_name="parametric_var"),
        ),
        migrations.AlterField(
            model_name="stockrisk",
            name="sharp_ratio",
            field=models.FloatField(null=True, verbose_name="sharp_ratio"),
        ),
        migrations.AlterField(
            model_name="stockrisk",
            name="sortino_ratio",
            field=models.FloatField(null=True, verbose_name="sortino_ratio"),
        ),
    ]